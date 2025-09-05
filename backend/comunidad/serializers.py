from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
import uuid


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    condominio = CondominioSerializer(read_only=True)
    tipo_usuario = TipoUsuarioSerializer(read_only=True)
    
    class Meta:
        model = PerfilUsuario
        fields = '__all__'


class TipoUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = '__all__'


class UnidadSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    tipo_unidad = TipoUnidadSerializer(read_only=True)
    
    class Meta:
        model = Unidad
        fields = '__all__'


class ResidenciaUnidadSerializer(serializers.ModelSerializer):
    usuario = PerfilUsuarioSerializer(read_only=True)
    unidad = UnidadSerializer(read_only=True)
    
    class Meta:
        model = ResidenciaUnidad
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    propietario = PerfilUsuarioSerializer(read_only=True)
    
    class Meta:
        model = Vehiculo
        fields = '__all__'


class AreaComunSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    
    class Meta:
        model = AreaComun
        fields = '__all__'


class ReservaAreaComunSerializer(serializers.ModelSerializer):
    area_comun = AreaComunSerializer(read_only=True)
    usuario = PerfilUsuarioSerializer(read_only=True)
    
    class Meta:
        model = ReservaAreaComun
        fields = '__all__'


class CamaraSeguridadSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    
    class Meta:
        model = CamaraSeguridad
        fields = '__all__'


class RegistroAccesoSerializer(serializers.ModelSerializer):
    usuario = PerfilUsuarioSerializer(read_only=True)
    vehiculo = VehiculoSerializer(read_only=True)
    camara = CamaraSeguridadSerializer(read_only=True)
    
    class Meta:
        model = RegistroAcceso
        fields = '__all__'


class VisitanteSerializer(serializers.ModelSerializer):
    unidad_destino = UnidadSerializer(read_only=True)
    autorizado_por = PerfilUsuarioSerializer(read_only=True)
    
    class Meta:
        model = Visitante
        fields = '__all__'


class AlertaSeguridadSerializer(serializers.ModelSerializer):
    camara = CamaraSeguridadSerializer(read_only=True)
    revisada_por = PerfilUsuarioSerializer(read_only=True)
    
    class Meta:
        model = AlertaSeguridad
        fields = '__all__'


# =====================================
# SERIALIZERS FINANCIEROS
# =====================================

class TipoGastoSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    
    class Meta:
        model = TipoGasto
        fields = '__all__'


class ConfiguracionExpensaSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    
    class Meta:
        model = ConfiguracionExpensa
        fields = '__all__'


class CuotaMantenimientoSerializer(serializers.ModelSerializer):
    unidad = UnidadSerializer(read_only=True)
    configuracion = ConfiguracionExpensaSerializer(read_only=True)
    
    class Meta:
        model = CuotaMantenimiento
        fields = '__all__'


class MetodoPagoSerializer(serializers.ModelSerializer):
    condominio = CondominioSerializer(read_only=True)
    
    class Meta:
        model = MetodoPago
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    cuota = CuotaMantenimientoSerializer(read_only=True)
    metodo_pago = MetodoPagoSerializer(read_only=True)
    registrado_por = PerfilUsuarioSerializer(read_only=True)
    verificado_por = PerfilUsuarioSerializer(read_only=True)
    
    class Meta:
        model = Pago
        fields = '__all__'


# =====================================
# SERIALIZERS PARA AUTENTICACIÓN
# =====================================

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=128)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                if user:
                    if user.is_active:
                        data['user'] = user
                    else:
                        raise serializers.ValidationError('La cuenta está desactivada.')
                else:
                    raise serializers.ValidationError('Credenciales inválidas.')
            except User.DoesNotExist:
                raise serializers.ValidationError('Usuario no encontrado.')
        else:
            raise serializers.ValidationError('Email y contraseña son requeridos.')
        
        return data


class RegistroSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=128)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    ci = serializers.CharField(max_length=15)
    telefono = serializers.CharField(max_length=20, required=False)
    unidad_numero = serializers.CharField(max_length=10)
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email ya está registrado.')
        return value
    
    def validate_ci(self, value):
        if PerfilUsuario.objects.filter(ci=value).exists():
            raise serializers.ValidationError('Esta cédula ya está registrada.')
        return value


# =====================================
# SERIALIZERS PARA DASHBOARD MÓVIL
# =====================================

class DashboardMovilSerializer(serializers.Serializer):
    """Serializer para datos del dashboard móvil"""
    usuario = PerfilUsuarioSerializer()
    unidad_principal = UnidadSerializer()
    cuota_pendiente = CuotaMantenimientoSerializer()
    reservas_activas = ReservaAreaComunSerializer(many=True)
    alertas_recientes = AlertaSeguridadSerializer(many=True)
    accesos_recientes = RegistroAccesoSerializer(many=True)
    balance_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    proximos_vencimientos = serializers.ListField()


class NotificacionMovilSerializer(serializers.Serializer):
    """Serializer para notificaciones móviles"""
    id = serializers.UUIDField(default=uuid.uuid4)
    tipo = serializers.ChoiceField(choices=[
        ('AVISO', 'Aviso Administrativo'),
        ('ALERTA', 'Alerta de Seguridad'),
        ('EMERGENCIA', 'Emergencia'),
        ('PAGO', 'Notificación de Pago'),
        ('RESERVA', 'Reserva de Área'),
    ])
    titulo = serializers.CharField(max_length=200)
    mensaje = serializers.CharField()
    fecha = serializers.DateTimeField()
    leida = serializers.BooleanField(default=False)
    prioridad = serializers.ChoiceField(choices=[
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ])
    datos_adicionales = serializers.JSONField(required=False)


class EstadisticasFinancierasSerializer(serializers.Serializer):
    """Serializer para estadísticas financieras del usuario"""
    saldo_actual = serializers.DecimalField(max_digits=10, decimal_places=2)
    cuotas_pendientes = serializers.IntegerField()
    total_pendiente = serializers.DecimalField(max_digits=10, decimal_places=2)
    pagos_realizados_mes = serializers.IntegerField()
    total_pagado_año = serializers.DecimalField(max_digits=10, decimal_places=2)
    proxima_cuota = CuotaMantenimientoSerializer()
    historial_pagos = PagoSerializer(many=True)


class QuickActionSerializer(serializers.Serializer):
    """Serializer para acciones rápidas del dashboard"""
    id = serializers.CharField()
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    icono = serializers.CharField()
    color = serializers.CharField()
    disponible = serializers.BooleanField()
    url = serializers.CharField(required=False)


# =====================================
# SERIALIZERS PARA CREAR DATOS
# =====================================

class CrearReservaSerializer(serializers.Serializer):
    area_comun_id = serializers.UUIDField()
    fecha_reserva = serializers.DateField()
    hora_inicio = serializers.TimeField()
    hora_fin = serializers.TimeField()
    numero_personas = serializers.IntegerField(min_value=1)
    proposito = serializers.CharField(max_length=200)
    observaciones = serializers.CharField(required=False, allow_blank=True)
    
    def validate(self, data):
        # Validar que la fecha no sea en el pasado
        from datetime import date
        if data['fecha_reserva'] < date.today():
            raise serializers.ValidationError('No se puede reservar para fechas pasadas.')
        
        # Validar que hora_fin sea mayor que hora_inicio
        if data['hora_fin'] <= data['hora_inicio']:
            raise serializers.ValidationError('La hora de fin debe ser mayor que la hora de inicio.')
        
        return data


class CrearPagoSerializer(serializers.Serializer):
    cuota_id = serializers.UUIDField()
    metodo_pago_id = serializers.UUIDField()
    monto_pagado = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    numero_comprobante = serializers.CharField(required=False, allow_blank=True)
    comprobante_imagen = serializers.ImageField(required=False)
    observaciones = serializers.CharField(required=False, allow_blank=True)


class ActualizarPerfilSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    telefono = serializers.CharField(max_length=20, required=False)
    telefono_emergencia = serializers.CharField(max_length=20, required=False)
    foto_perfil = serializers.ImageField(required=False)