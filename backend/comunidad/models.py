from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from decimal import Decimal
import uuid


class Condominio(models.Model):
    """Modelo principal del condominio"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Condominio")
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nit = models.CharField(max_length=15, unique=True, verbose_name="NIT")
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=100, default="Santa Cruz")
    pais = models.CharField(max_length=100, default="Bolivia")
    logo = models.ImageField(upload_to='condominios/logos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Condominio"
        verbose_name_plural = "Condominios"
    
    def __str__(self):
        return self.nombre


class TipoUsuario(models.Model):
    """Tipos de usuarios del sistema"""
    TIPOS = [
        ('ADMINISTRADOR', 'Administrador'),
        ('PROPIETARIO', 'Propietario'),
        ('INQUILINO', 'Inquilino'),
        ('SEGURIDAD', 'Personal de Seguridad'),
        ('MANTENIMIENTO', 'Personal de Mantenimiento'),
        ('VISITANTE', 'Visitante'),
    ]
    
    tipo = models.CharField(max_length=15, choices=TIPOS, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    permisos_especiales = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = "Tipo de Usuario"
        verbose_name_plural = "Tipos de Usuario"
    
    def __str__(self):
        return self.get_tipo_display()


class PerfilUsuario(models.Model):
    """Perfil extendido para usuarios del sistema"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='usuarios')
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    ci = models.CharField(max_length=15, unique=True, verbose_name="Cédula de Identidad")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    telefono_emergencia = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    
    # Datos para reconocimiento facial
    facial_encoding = models.JSONField(blank=True, null=True, help_text="Encoding facial para IA")
    facial_images = models.JSONField(default=list, blank=True, help_text="URLs de imágenes para entrenamiento")
    
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_tipo_usuario_display()})"


class TipoUnidad(models.Model):
    """Tipos de unidades habitacionales"""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    factor_costo = models.DecimalField(max_digits=5, decimal_places=2, default=1.00,
                                      help_text="Factor multiplicador para costos")
    
    class Meta:
        verbose_name = "Tipo de Unidad"
        verbose_name_plural = "Tipos de Unidades"
    
    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    """Unidades habitacionales del condominio"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='unidades')
    numero = models.CharField(max_length=10, verbose_name="Número/Identificador")
    tipo_unidad = models.ForeignKey(TipoUnidad, on_delete=models.PROTECT)
    piso = models.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(100)])
    bloque = models.CharField(max_length=10, blank=True, null=True)
    metros_cuadrados = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    dormitorios = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    baños = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    
    # Para cálculo de expensas
    porcentaje_propiedad = models.DecimalField(
        max_digits=5, decimal_places=2, 
        validators=[MinValueValidator(0.01), MaxValueValidator(100.00)],
        help_text="Porcentaje para cálculo de gastos comunes"
    )
    
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
        unique_together = ['condominio', 'numero']
        ordering = ['bloque', 'piso', 'numero']
    
    def __str__(self):
        bloque_str = f"{self.bloque}-" if self.bloque else ""
        return f"{bloque_str}{self.numero}"


class ResidenciaUnidad(models.Model):
    """Relación entre usuarios y unidades"""
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='residencias')
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='residentes')
    es_propietario = models.BooleanField(default=False)
    porcentaje_propiedad = models.DecimalField(
        max_digits=5, decimal_places=2, default=100.00,
        validators=[MinValueValidator(0.01), MaxValueValidator(100.00)]
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Residencia en Unidad"
        verbose_name_plural = "Residencias en Unidades"
    
    def __str__(self):
        tipo = "Propietario" if self.es_propietario else "Inquilino"
        return f"{self.usuario.user.get_full_name()} - {self.unidad} ({tipo})"


class Vehiculo(models.Model):
    """Vehículos registrados de los residentes"""
    TIPOS_VEHICULO = [
        ('AUTO', 'Automóvil'),
        ('MOTO', 'Motocicleta'),
        ('CAMIONETA', 'Camioneta'),
        ('OTRO', 'Otro'),
    ]
    
    propietario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPOS_VEHICULO)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2030)])
    color = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
    
    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"


class AreaComun(models.Model):
    """Áreas comunes del condominio"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='areas_comunes')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    capacidad_maxima = models.IntegerField()
    precio_por_hora = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    requiere_deposito = models.BooleanField(default=False)
    monto_deposito = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    dias_disponibles = models.JSONField(default=list, help_text="Lista de días de la semana disponibles")
    equipamiento = models.TextField(blank=True, null=True)
    reglas = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='areas_comunes/', blank=True, null=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Área Común"
        verbose_name_plural = "Áreas Comunes"
    
    def __str__(self):
        return f"{self.nombre} - {self.condominio.nombre}"


class ReservaAreaComun(models.Model):
    """Reservas de áreas comunes"""
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('COMPLETADA', 'Completada'),
    ]
    
    area_comun = models.ForeignKey(AreaComun, on_delete=models.CASCADE, related_name='reservas')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    numero_personas = models.IntegerField(validators=[MinValueValidator(1)])
    proposito = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PENDIENTE')
    monto_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    deposito_pagado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Reserva de Área Común"
        verbose_name_plural = "Reservas de Áreas Comunes"
        ordering = ['-fecha_reserva', '-hora_inicio']
    
    def __str__(self):
        return f"{self.area_comun.nombre} - {self.fecha_reserva} - {self.usuario.user.get_full_name()}"


# Modelos para Seguridad e IA
class CamaraSeguridad(models.Model):
    """Cámaras de seguridad del condominio"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='camaras')
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    puerto = models.IntegerField(default=80)
    usuario_camara = models.CharField(max_length=50, blank=True, null=True)
    password_camara = models.CharField(max_length=100, blank=True, null=True)
    
    # Capacidades de IA
    reconocimiento_facial = models.BooleanField(default=False)
    deteccion_vehiculos = models.BooleanField(default=False)
    deteccion_anomalias = models.BooleanField(default=False)
    
    activa = models.BooleanField(default=True)
    fecha_instalacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cámara de Seguridad"
        verbose_name_plural = "Cámaras de Seguridad"
    
    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"


class RegistroAcceso(models.Model):
    """Registro de accesos al condominio"""
    TIPOS_ACCESO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    
    METODOS_IDENTIFICACION = [
        ('FACIAL', 'Reconocimiento Facial'),
        ('TARJETA', 'Tarjeta de Acceso'),
        ('CODIGO', 'Código de Acceso'),
        ('MANUAL', 'Registro Manual'),
        ('VEHICULAR', 'Placa Vehicular'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='registros_acceso')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='accesos', null=True, blank=True)
    visitante = models.ForeignKey('Visitante', on_delete=models.CASCADE, related_name='accesos', null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    camara = models.ForeignKey(CamaraSeguridad, on_delete=models.SET_NULL, null=True, blank=True)
    
    tipo_acceso = models.CharField(max_length=10, choices=TIPOS_ACCESO)
    metodo_identificacion = models.CharField(max_length=15, choices=METODOS_IDENTIFICACION)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    foto_capturada = models.ImageField(upload_to='accesos/', blank=True, null=True)
    confianza_ia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                      help_text="Nivel de confianza del reconocimiento IA (0-100)")
    observaciones = models.TextField(blank=True, null=True)
    autorizado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Registro de Acceso"
        verbose_name_plural = "Registros de Acceso"
        ordering = ['-fecha_hora']
    
    def __str__(self):
        persona = self.usuario.user.get_full_name() if self.usuario else (self.visitante.nombre if self.visitante else "Desconocido")
        return f"{self.get_tipo_acceso_display()} - {persona} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"


class Visitante(models.Model):
    """Registro de visitantes"""
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    motivo_visita = models.CharField(max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='visitantes')
    autorizado_por = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='visitantes_autorizados')
    
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)
    foto_entrada = models.ImageField(upload_to='visitantes/', blank=True, null=True)
    vehiculo_placa = models.CharField(max_length=10, blank=True, null=True)
    
    # Para IA
    facial_encoding = models.JSONField(blank=True, null=True)
    
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        ordering = ['-fecha_hora_entrada']
    
    def __str__(self):
        return f"{self.nombre} - {self.unidad_destino}"


class AlertaSeguridad(models.Model):
    """Alertas generadas por el sistema de IA"""
    TIPOS_ALERTA = [
        ('ACCESO_NO_AUTORIZADO', 'Acceso No Autorizado'),
        ('PERSONA_DESCONOCIDA', 'Persona Desconocida'),
        ('VEHICULO_NO_AUTORIZADO', 'Vehículo No Autorizado'),
        ('COMPORTAMIENTO_SOSPECHOSO', 'Comportamiento Sospechoso'),
        ('MASCOTA_SUELTA', 'Mascota Suelta'),
        ('VEHICULO_MAL_ESTACIONADO', 'Vehículo Mal Estacionado'),
        ('OTRO', 'Otro'),
    ]
    
    NIVELES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='alertas')
    camara = models.ForeignKey(CamaraSeguridad, on_delete=models.CASCADE, related_name='alertas')
    tipo_alerta = models.CharField(max_length=25, choices=TIPOS_ALERTA)
    nivel = models.CharField(max_length=10, choices=NIVELES)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    imagen_evidencia = models.ImageField(upload_to='alertas/', blank=True, null=True)
    video_evidencia = models.FileField(upload_to='alertas/videos/', blank=True, null=True)
    
    # Datos de IA
    datos_ia = models.JSONField(blank=True, null=True, help_text="Datos adicionales del análisis de IA")
    confianza_deteccion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    revisada = models.BooleanField(default=False)
    revisada_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='alertas_revisadas')
    fecha_revision = models.DateTimeField(null=True, blank=True)
    accion_tomada = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Alerta de Seguridad"
        verbose_name_plural = "Alertas de Seguridad"
        ordering = ['-fecha_hora']
    
    def __str__(self):
        return f"{self.get_tipo_alerta_display()} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"


# =========================
# MODELOS FINANCIEROS
# =========================

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
    proveedor_pago = models.CharField(max_length=50, blank=True, null=True)
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
