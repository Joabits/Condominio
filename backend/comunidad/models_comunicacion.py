from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Condominio, PerfilUsuario, Unidad, AreaComun
import uuid


class TipoComunicado(models.Model):
    """Tipos de comunicados"""
    TIPOS = [
        ('GENERAL', 'General'),
        ('URGENTE', 'Urgente'),
        ('MANTENIMIENTO', 'Mantenimiento'),
        ('REUNION', 'Reunión'),
        ('AVISO', 'Aviso'),
        ('FINANCIERO', 'Financiero'),
        ('SEGURIDAD', 'Seguridad'),
    ]
    
    tipo = models.CharField(max_length=15, choices=TIPOS, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    color_badge = models.CharField(max_length=7, default='#007bff', help_text="Color hexadecimal para el badge")
    requiere_confirmacion = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Tipo de Comunicado"
        verbose_name_plural = "Tipos de Comunicados"
    
    def __str__(self):
        return self.get_tipo_display()


class Comunicado(models.Model):
    """Comunicados y anuncios para los residentes"""
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('PUBLICADO', 'Publicado'),
        ('ARCHIVADO', 'Archivado'),
    ]
    
    AUDIENCIAS = [
        ('TODOS', 'Todos los Residentes'),
        ('PROPIETARIOS', 'Solo Propietarios'),
        ('INQUILINOS', 'Solo Inquilinos'),
        ('ADMINISTRACION', 'Solo Administración'),
        ('PERSONALIZADA', 'Audiencia Personalizada'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='comunicados')
    tipo = models.ForeignKey(TipoComunicado, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    resumen = models.CharField(max_length=300, blank=True, null=True, 
                              help_text="Resumen para notificaciones push")
    
    audiencia = models.CharField(max_length=15, choices=AUDIENCIAS, default='TODOS')
    unidades_especificas = models.ManyToManyField(Unidad, blank=True, 
                                                 help_text="Para audiencia personalizada")
    
    estado = models.CharField(max_length=10, choices=ESTADOS, default='BORRADOR')
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_programada = models.DateTimeField(null=True, blank=True, 
                                           help_text="Para programar publicación")
    fecha_expiracion = models.DateTimeField(null=True, blank=True)
    
    # Archivos adjuntos
    imagen_destacada = models.ImageField(upload_to='comunicados/imagenes/', blank=True, null=True)
    archivo_adjunto = models.FileField(upload_to='comunicados/archivos/', blank=True, null=True)
    
    # Interacción
    permite_comentarios = models.BooleanField(default=True)
    es_urgente = models.BooleanField(default=False)
    requiere_confirmacion_lectura = models.BooleanField(default=False)
    
    # Estadísticas
    veces_visto = models.IntegerField(default=0)
    confirmaciones_lectura = models.IntegerField(default=0)
    
    autor = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT, related_name='comunicados_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"
        ordering = ['-fecha_publicacion', '-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.condominio.nombre}"


class LecturaComunicado(models.Model):
    """Registro de lecturas de comunicados"""
    comunicado = models.ForeignKey(Comunicado, on_delete=models.CASCADE, related_name='lecturas')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='comunicados_leidos')
    fecha_lectura = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Lectura de Comunicado"
        verbose_name_plural = "Lecturas de Comunicados"
        unique_together = ['comunicado', 'usuario']
    
    def __str__(self):
        return f"{self.usuario.user.get_full_name()} - {self.comunicado.titulo}"


class ComentarioComunicado(models.Model):
    """Comentarios en comunicados"""
    comunicado = models.ForeignKey(Comunicado, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    moderado = models.BooleanField(default=True)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, 
                             related_name='respuestas')
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['fecha_creacion']
    
    def __str__(self):
        return f"Comentario de {self.usuario.user.get_full_name()} en {self.comunicado.titulo}"


class TipoMantenimiento(models.Model):
    """Tipos de mantenimiento"""
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='tipos_mantenimiento')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    es_preventivo = models.BooleanField(default=False)
    frecuencia_dias = models.IntegerField(null=True, blank=True, 
                                         help_text="Días entre mantenimientos preventivos")
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requiere_personal_externo = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Tipo de Mantenimiento"
        verbose_name_plural = "Tipos de Mantenimiento"
    
    def __str__(self):
        return f"{self.nombre} - {self.condominio.nombre}"


class PersonalMantenimiento(models.Model):
    """Personal de mantenimiento interno y externo"""
    TIPOS_PERSONAL = [
        ('INTERNO', 'Personal Interno'),
        ('EXTERNO', 'Proveedor Externo'),
        ('CONTRATISTA', 'Contratista'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='personal_mantenimiento')
    usuario = models.OneToOneField(PerfilUsuario, on_delete=models.CASCADE, null=True, blank=True)
    tipo_personal = models.CharField(max_length=12, choices=TIPOS_PERSONAL)
    
    # Para personal externo
    nombre_empresa = models.CharField(max_length=200, blank=True, null=True)
    nombre_contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    nit = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    
    especialidades = models.JSONField(default=list, help_text="Lista de especialidades")
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, default=0,
                                      help_text="Calificación promedio del 1 al 5")
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Personal de Mantenimiento"
        verbose_name_plural = "Personal de Mantenimiento"
    
    def __str__(self):
        if self.usuario:
            return f"{self.usuario.user.get_full_name()} ({self.get_tipo_personal_display()})"
        return f"{self.nombre_contacto} - {self.nombre_empresa or 'Independiente'}"


class SolicitudMantenimiento(models.Model):
    """Solicitudes de mantenimiento"""
    PRIORIDADES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]
    
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ASIGNADA', 'Asignada'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='solicitudes_mantenimiento')
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT)
    solicitante = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='solicitudes_mantenimiento')
    unidad_relacionada = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True, blank=True)
    area_comun_relacionada = models.ForeignKey(AreaComun, on_delete=models.SET_NULL, null=True, blank=True)
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion_especifica = models.CharField(max_length=200, blank=True, null=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='MEDIA')
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PENDIENTE')
    
    # Archivos adjuntos
    fotos_problema = models.JSONField(default=list, blank=True, help_text="URLs de fotos del problema")
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField(null=True, blank=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    
    # Asignación
    asignado_a = models.ForeignKey(PersonalMantenimiento, on_delete=models.SET_NULL, 
                                  null=True, blank=True, related_name='tareas_asignadas')
    asignado_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, 
                                   null=True, blank=True, related_name='mantenimientos_asignados')
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    
    # Costo
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo_real = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Calificación del servicio
    calificacion = models.IntegerField(null=True, blank=True, 
                                      validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario_calificacion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Solicitud de Mantenimiento"
        verbose_name_plural = "Solicitudes de Mantenimiento"
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.titulo} - {self.get_prioridad_display()} - {self.get_estado_display()}"


class MantenimientoPreventivo(models.Model):
    """Programa de mantenimientos preventivos"""
    ESTADOS = [
        ('PROGRAMADO', 'Programado'),
        ('COMPLETADO', 'Completado'),
        ('POSTPONED', 'Pospuesto'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='mantenimientos_preventivos')
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    area_comun = models.ForeignKey(AreaComun, on_delete=models.CASCADE, null=True, blank=True)
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_programada = models.DateTimeField()
    fecha_completada = models.DateTimeField(null=True, blank=True)
    frecuencia_dias = models.IntegerField(help_text="Días hasta el próximo mantenimiento")
    
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PROGRAMADO')
    personal_asignado = models.ForeignKey(PersonalMantenimiento, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Seguimiento automático
    proxima_fecha = models.DateTimeField(null=True, blank=True)
    recordatorio_enviado = models.BooleanField(default=False)
    
    # Costos
    costo_programado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo_real = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Documentación
    reporte_trabajo = models.TextField(blank=True, null=True)
    fotos_antes = models.JSONField(default=list, blank=True)
    fotos_despues = models.JSONField(default=list, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Mantenimiento Preventivo"
        verbose_name_plural = "Mantenimientos Preventivos"
        ordering = ['fecha_programada']
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_programada.strftime('%d/%m/%Y')}"


class NotificacionPush(models.Model):
    """Notificaciones push para la aplicación móvil"""
    TIPOS = [
        ('SEGURIDAD', 'Alerta de Seguridad'),
        ('COMUNICADO', 'Nuevo Comunicado'),
        ('PAGO', 'Recordatorio de Pago'),
        ('MANTENIMIENTO', 'Mantenimiento'),
        ('RESERVA', 'Reserva de Área Común'),
        ('GENERAL', 'General'),
    ]
    
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ENVIADA', 'Enviada'),
        ('FALLIDA', 'Fallida'),
    ]
    
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=15, choices=TIPOS)
    titulo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=200)
    datos_adicionales = models.JSONField(blank=True, null=True, 
                                        help_text="Datos para deep linking y acciones")
    
    # Audiencia
    usuarios_destino = models.ManyToManyField(PerfilUsuario, blank=True, related_name='notificaciones_recibidas')
    enviar_a_todos = models.BooleanField(default=False)
    
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')
    fecha_programada = models.DateTimeField(null=True, blank=True)
    fecha_enviada = models.DateTimeField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estadísticas
    total_enviadas = models.IntegerField(default=0)
    total_entregadas = models.IntegerField(default=0)
    total_leidas = models.IntegerField(default=0)
    
    creada_por = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT, related_name='notificaciones_creadas')
    
    class Meta:
        verbose_name = "Notificación Push"
        verbose_name_plural = "Notificaciones Push"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"


class ConfiguracionNotificaciones(models.Model):
    """Configuración de notificaciones por usuario"""
    usuario = models.OneToOneField(PerfilUsuario, on_delete=models.CASCADE, related_name='config_notificaciones')
    
    # Tipos de notificaciones habilitadas
    alertas_seguridad = models.BooleanField(default=True)
    comunicados_urgentes = models.BooleanField(default=True)
    comunicados_generales = models.BooleanField(default=True)
    recordatorios_pago = models.BooleanField(default=True)
    mantenimiento = models.BooleanField(default=True)
    reservas = models.BooleanField(default=True)
    
    # Configuración de horarios
    no_molestar_inicio = models.TimeField(default='22:00')
    no_molestar_fin = models.TimeField(default='07:00')
    
    # Tokens para notificaciones push
    token_firebase = models.CharField(max_length=500, blank=True, null=True)
    token_apns = models.CharField(max_length=500, blank=True, null=True)
    
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Configuración de Notificaciones"
        verbose_name_plural = "Configuraciones de Notificaciones"
    
    def __str__(self):
        return f"Config. Notif. - {self.usuario.user.get_full_name()}"