from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from decimal import Decimal
import uuid
from .models import Condominio, PerfilUsuario, Unidad


class TipoGasto(models.Model):
    """Categorías de gastos del condominio"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='tipos_gasto')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    es_fijo = models.BooleanField(default=False, help_text="Si es un gasto fijo mensual")
    monto_fijo = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Tipo de Gasto"
        verbose_name_plural = "Tipos de Gastos"
        unique_together = ['condominio', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.condominio.nombre}"


class GastoComun(models.Model):
    """Gastos comunes del condominio"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='gastos_comunes')
    tipo_gasto = models.ForeignKey(TipoGasto, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_gasto = models.DateField()
    periodo_mes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    periodo_año = models.IntegerField(validators=[MinValueValidator(2020), MaxValueValidator(2050)])
    
    # Documentación
    factura = models.FileField(upload_to='gastos/facturas/', blank=True, null=True)
    comprobante = models.FileField(upload_to='gastos/comprobantes/', blank=True, null=True)
    
    proveedor = models.CharField(max_length=200, blank=True, null=True)
    numero_factura = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    
    registrado_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    aprobado_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, 
                                   null=True, blank=True, related_name='gastos_aprobados')
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Gasto Común"
        verbose_name_plural = "Gastos Comunes"
        ordering = ['-fecha_gasto']
    
    def __str__(self):
        return f"{self.descripcion} - {self.periodo_mes}/{self.periodo_año} - ${self.monto}"


class ConfiguracionExpensa(models.Model):
    """Configuración de expensas por período"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='configuraciones_expensa')
    periodo_mes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    periodo_año = models.IntegerField(validators=[MinValueValidator(2020), MaxValueValidator(2050)])
    
    # Montos base
    monto_base_administracion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_base_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_base_seguridad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_base_limpieza = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Configuración de multas
    multa_retraso_pago = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    dias_gracia = models.IntegerField(default=5, help_text="Días de gracia antes de aplicar multa")
    porcentaje_mora = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                         help_text="Porcentaje mensual de mora")
    
    fecha_vencimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Configuración de Expensa"
        verbose_name_plural = "Configuraciones de Expensas"
        unique_together = ['condominio', 'periodo_mes', 'periodo_año']
    
    def __str__(self):
        return f"Expensas {self.periodo_mes}/{self.periodo_año} - {self.condominio.nombre}"


class CuotaMantenimiento(models.Model):
    """Cuotas de mantenimiento por unidad"""
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADA', 'Pagada'),
        ('VENCIDA', 'Vencida'),
        ('PAGADA_PARCIAL', 'Pagada Parcial'),
        ('CONDONADA', 'Condonada'),
    ]
    
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='cuotas')
    configuracion = models.ForeignKey(ConfiguracionExpensa, on_delete=models.CASCADE, related_name='cuotas')
    
    # Montos calculados
    monto_administracion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_seguridad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_limpieza = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_gastos_extras = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_multas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_mora = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    estado = models.CharField(max_length=15, choices=ESTADOS, default='PENDIENTE')
    fecha_vencimiento = models.DateField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_pago = models.DateTimeField(null=True, blank=True)
    
    # Para IA - Predicción de morosidad
    riesgo_morosidad = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                          help_text="Porcentaje de riesgo predicho por IA")
    factores_riesgo = models.JSONField(blank=True, null=True,
                                      help_text="Factores considerados por IA para predicción")
    
    class Meta:
        verbose_name = "Cuota de Mantenimiento"
        verbose_name_plural = "Cuotas de Mantenimiento"
        unique_together = ['unidad', 'configuracion']
        ordering = ['-configuracion__periodo_año', '-configuracion__periodo_mes']
    
    def save(self, *args, **kwargs):
        # Calcular monto total
        self.monto_total = (self.monto_administracion + self.monto_mantenimiento + 
                           self.monto_seguridad + self.monto_limpieza + 
                           self.monto_gastos_extras + self.monto_multas + self.monto_mora)
        self.monto_pendiente = self.monto_total - self.monto_pagado
        
        # Actualizar estado
        if self.monto_pendiente <= 0:
            self.estado = 'PAGADA'
        elif self.monto_pagado > 0:
            self.estado = 'PAGADA_PARCIAL'
        elif self.fecha_vencimiento < timezone.now().date():
            self.estado = 'VENCIDA'
        else:
            self.estado = 'PENDIENTE'
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.unidad} - {self.configuracion.periodo_mes}/{self.configuracion.periodo_año}"


class MetodoPago(models.Model):
    """Métodos de pago disponibles"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='metodos_pago')
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    requiere_comprobante = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    
    # Configuración para pagos online
    es_online = models.BooleanField(default=False)
    proveedor_pago = models.CharField(max_length=50, blank=True, null=True)  # Ej: Stripe, PayPal, etc.
    configuracion_api = models.JSONField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Método de Pago"
        verbose_name_plural = "Métodos de Pago"
    
    def __str__(self):
        return f"{self.nombre} - {self.condominio.nombre}"


class Pago(models.Model):
    """Registro de pagos realizados"""
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PROCESANDO', 'Procesando'),
        ('COMPLETADO', 'Completado'),
        ('FALLIDO', 'Fallido'),
        ('REEMBOLSADO', 'Reembolsado'),
    ]
    
    cuota = models.ForeignKey(CuotaMantenimiento, on_delete=models.CASCADE, related_name='pagos')
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Datos del pago
    numero_transaccion = models.CharField(max_length=100, unique=True)
    numero_comprobante = models.CharField(max_length=50, blank=True, null=True)
    comprobante_imagen = models.ImageField(upload_to='pagos/comprobantes/', blank=True, null=True)
    
    fecha_pago = models.DateTimeField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=12, choices=ESTADOS_PAGO, default='PENDIENTE')
    
    # Para pagos online
    id_transaccion_externa = models.CharField(max_length=200, blank=True, null=True)
    datos_pago_online = models.JSONField(blank=True, null=True)
    
    observaciones = models.TextField(blank=True, null=True)
    registrado_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT)
    verificado_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, 
                                     null=True, blank=True, related_name='pagos_verificados')
    fecha_verificacion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"Pago ${self.monto_pagado} - {self.cuota} - {self.fecha_pago.strftime('%d/%m/%Y')}"


class Multa(models.Model):
    """Multas aplicadas a los residentes"""
    TIPOS_MULTA = [
        ('RETRASO_PAGO', 'Retraso en Pago'),
        ('RUIDO', 'Ruido Excesivo'),
        ('MASCOTA', 'Infracción con Mascota'),
        ('ESTACIONAMIENTO', 'Mal Estacionamiento'),
        ('AREA_COMUN', 'Mal Uso de Área Común'),
        ('OTRO', 'Otro'),
    ]
    
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADA', 'Pagada'),
        ('CONDONADA', 'Condonada'),
        ('APELADA', 'En Apelación'),
    ]
    
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='multas')
    tipo_multa = models.CharField(max_length=15, choices=TIPOS_MULTA)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_incidente = models.DateTimeField()
    fecha_aplicacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PENDIENTE')
    evidencia = models.FileField(upload_to='multas/evidencia/', blank=True, null=True)
    
    aplicada_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT, related_name='multas_aplicadas')
    pagada_en = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Para apelaciones
    apelacion_texto = models.TextField(blank=True, null=True)
    fecha_apelacion = models.DateTimeField(null=True, blank=True)
    apelacion_resuelta_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, 
                                             null=True, blank=True, related_name='apelaciones_resueltas')
    resultado_apelacion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Multa"
        verbose_name_plural = "Multas"
        ordering = ['-fecha_aplicacion']
    
    def __str__(self):
        return f"Multa {self.get_tipo_multa_display()} - {self.unidad} - ${self.monto}"


class ReporteFinanciero(models.Model):
    """Reportes financieros generados automáticamente"""
    TIPOS_REPORTE = [
        ('MENSUAL', 'Reporte Mensual'),
        ('TRIMESTRAL', 'Reporte Trimestral'),
        ('ANUAL', 'Reporte Anual'),
        ('MOROSIDAD', 'Reporte de Morosidad'),
        ('GASTOS', 'Reporte de Gastos'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='reportes_financieros')
    tipo_reporte = models.CharField(max_length=12, choices=TIPOS_REPORTE)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    
    # Datos calculados
    total_ingresos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_gastos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_pendiente = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    porcentaje_morosidad = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    # Datos de IA
    predicciones_ia = models.JSONField(blank=True, null=True)
    tendencias_ia = models.JSONField(blank=True, null=True)
    
    archivo_reporte = models.FileField(upload_to='reportes/', blank=True, null=True)
    datos_reporte = models.JSONField(blank=True, null=True)
    
    generado_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Reporte Financiero"
        verbose_name_plural = "Reportes Financieros"
        ordering = ['-fecha_generacion']
    
    def __str__(self):
        return f"{self.get_tipo_reporte_display()} - {self.periodo_inicio} a {self.periodo_fin}"