from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from .models import PerfilUsuario, CuotaMantenimiento


@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crear perfil de usuario automáticamente cuando se crea un usuario"""
    if created and not hasattr(instance, 'perfil'):
        # Solo crear perfil si no existe - evitar crear perfiles automáticos
        # El perfil se creará manualmente desde el admin o mediante API
        pass


@receiver(pre_save, sender=CuotaMantenimiento)
def actualizar_estado_cuota(sender, instance, **kwargs):
    """Actualizar automáticamente el estado de las cuotas"""
    if instance.monto_pendiente <= 0:
        instance.estado = 'PAGADA'
    elif instance.monto_pagado > 0:
        instance.estado = 'PAGADA_PARCIAL'
    elif instance.fecha_vencimiento < timezone.now().date():
        instance.estado = 'VENCIDA'
    else:
        instance.estado = 'PENDIENTE'


@receiver(post_save, sender=PerfilUsuario)
def actualizar_ultimo_acceso(sender, instance, **kwargs):
    """Actualizar último acceso del usuario"""
    if hasattr(instance, '_actualizar_acceso'):
        instance.ultimo_acceso = timezone.now()
        instance.save(update_fields=['ultimo_acceso'])