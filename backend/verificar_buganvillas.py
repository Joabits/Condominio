#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from comunidad.models import Condominio, PerfilUsuario, Unidad, AreaComun
from django.contrib.auth.models import User

print("🏢 === CONDOMINIO BUGANVILLAS - VERIFICACIÓN COMPLETA ===")
print()

# Información del condominio
condo = Condominio.objects.first()
if condo:
    print(f"🏠 CONDOMINIO: {condo.nombre}")
    print(f"📍 Dirección: {condo.direccion}")
    print(f"🌎 Ciudad: {condo.ciudad}, {condo.pais}")
    print(f"📧 Email: {condo.email}")
    print(f"📞 Teléfono: {condo.telefono}")
    print()

# Estadísticas de residentes
total_users = User.objects.count()
staff_users = User.objects.filter(is_staff=True).count()
perfiles = PerfilUsuario.objects.filter(condominio=condo).count()
activos = PerfilUsuario.objects.filter(condominio=condo, activo=True).count()

print(f"👥 RESIDENTES:")
print(f"   Total usuarios: {total_users}")
print(f"   Administradores: {staff_users}")
print(f"   Perfiles de residentes: {perfiles}")
print(f"   Residentes activos: {activos}")
print()

# Unidades
unidades = Unidad.objects.count()
unidades_activas = Unidad.objects.filter(activa=True).count()

print(f"🏘️ UNIDADES:")
print(f"   Total unidades: {unidades}")
print(f"   Unidades activas: {unidades_activas}")
print()

# Áreas comunes
areas = AreaComun.objects.count()
areas_activas = AreaComun.objects.filter(activa=True).count()

print(f"🌳 ÁREAS COMUNES:")
print(f"   Total áreas: {areas}")
print(f"   Áreas activas: {areas_activas}")
print()

print("✅ CREDENCIALES DE ACCESO:")
print("📱 APLICACIÓN MÓVIL (Residentes):")
print("   Email: juan.silva@email.com")
print("   Contraseña: Prop2025!")
print()
print("🌐 PANEL WEB DE ADMINISTRACIÓN:")
print("   URL: http://localhost:3001")
print()
print("🔧 ADMIN DJANGO:")
print("   URL: http://127.0.0.1:8000/admin/")
print("   Username: admin_general")
print("   Contraseña: Admin2025!")
print()

print("🚀 ESTADO: Condominio Buganvillas listo para usar!")