from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *


# Inline para PerfilUsuario
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil'


# Extender UserAdmin para incluir perfil
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)


# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Condominio)
class CondominioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nit', 'ciudad', 'activo', 'fecha_creacion', 'total_unidades']
    list_filter = ['activo', 'ciudad', 'fecha_creacion']
    search_fields = ['nombre', 'nit', 'direccion']
    readonly_fields = ['id', 'fecha_creacion']
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'nit', 'direccion', 'ciudad', 'pais', 'codigo_postal')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email')
        }),
        ('Configuración', {
            'fields': ('logo', 'activo')
        }),
        ('Metadata', {
            'fields': ('id', 'fecha_creacion'),
            'classes': ('collapse',)
        })
    )
    
    def total_unidades(self, obj):
        return obj.unidades.count()
    total_unidades.short_description = 'Total Unidades'


@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'descripcion']
    search_fields = ['tipo']


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['get_nombre_completo', 'ci', 'tipo_usuario', 'condominio', 'activo', 'ultimo_acceso']
    list_filter = ['tipo_usuario', 'condominio', 'activo', 'fecha_registro']
    search_fields = ['ci', 'user__first_name', 'user__last_name', 'user__email', 'telefono']
    readonly_fields = ['fecha_registro', 'ultimo_acceso']
    
    def get_nombre_completo(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_nombre_completo.short_description = 'Nombre Completo'


@admin.register(TipoUnidad)
class TipoUnidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'factor_costo', 'descripcion']
    search_fields = ['nombre']


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tipo_unidad', 'piso', 'metros_cuadrados', 'porcentaje_propiedad', 'activa']
    list_filter = ['condominio', 'tipo_unidad', 'activa', 'piso']
    search_fields = ['numero', 'condominio__nombre']
    ordering = ['condominio', 'bloque', 'piso', 'numero']


@admin.register(ResidenciaUnidad)
class ResidenciaUnidadAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'unidad', 'es_propietario', 'porcentaje_propiedad', 'activa']
    list_filter = ['es_propietario', 'activa', 'unidad__condominio']
    search_fields = ['usuario__user__first_name', 'usuario__user__last_name', 'unidad__numero']


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'propietario', 'tipo', 'marca', 'modelo', 'año', 'activo']
    list_filter = ['tipo', 'marca', 'activo', 'año']
    search_fields = ['placa', 'marca', 'modelo', 'propietario__user__first_name']


@admin.register(AreaComun)
class AreaComunAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'condominio', 'capacidad_maxima', 'precio_por_hora', 'activa']
    list_filter = ['condominio', 'activa', 'requiere_deposito']
    search_fields = ['nombre', 'descripcion']


@admin.register(ReservaAreaComun)
class ReservaAreaComunAdmin(admin.ModelAdmin):
    list_display = ['area_comun', 'usuario', 'fecha_reserva', 'hora_inicio', 'estado', 'monto_total']
    list_filter = ['estado', 'area_comun__condominio', 'fecha_reserva']
    search_fields = ['area_comun__nombre', 'usuario__user__first_name']
    date_hierarchy = 'fecha_reserva'


@admin.register(CamaraSeguridad)
class CamaraSeguridadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'ip_address', 'reconocimiento_facial', 
                   'deteccion_vehiculos', 'activa']
    list_filter = ['condominio', 'activa', 'reconocimiento_facial', 'deteccion_vehiculos']
    search_fields = ['nombre', 'ubicacion', 'ip_address']


@admin.register(RegistroAcceso)
class RegistroAccesoAdmin(admin.ModelAdmin):
    list_display = ['get_persona', 'tipo_acceso', 'metodo_identificacion', 'fecha_hora', 
                   'autorizado', 'confianza_ia']
    list_filter = ['tipo_acceso', 'metodo_identificacion', 'autorizado', 'condominio']
    search_fields = ['usuario__user__first_name', 'visitante__nombre']
    date_hierarchy = 'fecha_hora'
    readonly_fields = ['fecha_hora']
    
    def get_persona(self, obj):
        if obj.usuario:
            return obj.usuario.user.get_full_name()
        elif obj.visitante:
            return obj.visitante.nombre
        return "Desconocido"
    get_persona.short_description = 'Persona'


@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ci', 'unidad_destino', 'autorizado_por', 'fecha_hora_entrada', 
                   'fecha_hora_salida']
    list_filter = ['unidad_destino__condominio', 'fecha_hora_entrada']
    search_fields = ['nombre', 'ci', 'telefono']
    date_hierarchy = 'fecha_hora_entrada'


@admin.register(AlertaSeguridad)
class AlertaSeguridadAdmin(admin.ModelAdmin):
    list_display = ['tipo_alerta', 'nivel', 'camara', 'fecha_hora', 'revisada', 'confianza_deteccion']
    list_filter = ['tipo_alerta', 'nivel', 'revisada', 'condominio']
    search_fields = ['descripcion']
    date_hierarchy = 'fecha_hora'
    actions = ['marcar_como_revisada']
    
    def marcar_como_revisada(self, request, queryset):
        queryset.update(revisada=True, revisada_por=request.user.perfil)
    marcar_como_revisada.short_description = "Marcar alertas seleccionadas como revisadas"


# Configuración del sitio admin
admin.site.site_header = "Smart Condominium - Administración"
admin.site.site_title = "Smart Condominium"
admin.site.index_title = "Panel de Administración"
