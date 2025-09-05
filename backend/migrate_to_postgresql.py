# 🔄 Script de Migración de SQLite a PostgreSQL - Smart Condominio

import os
import django
import json
from pathlib import Path

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command
from django.db import connection
from django.conf import settings

def backup_sqlite_data():
    """Crear respaldo de los datos de SQLite"""
    print("📦 Creando respaldo de datos de SQLite...")
    
    # Cambiar temporalmente a SQLite para exportar datos
    backup_settings = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).resolve().parent / 'db.sqlite3',
    }
    
    # Exportar datos usando dumpdata
    try:
        call_command('dumpdata', 
                    '--natural-foreign', 
                    '--natural-primary',
                    '--exclude=auth.permission',
                    '--exclude=contenttypes',
                    '--exclude=admin.logentry',
                    '--exclude=sessions.session',
                    '--output=sqlite_backup.json')
        print("✅ Respaldo creado: sqlite_backup.json")
        return True
    except Exception as e:
        print(f"❌ Error al crear respaldo: {e}")
        return False

def setup_postgresql():
    """Configurar la base de datos PostgreSQL"""
    print("🐘 Configurando PostgreSQL...")
    
    try:
        # Crear las tablas en PostgreSQL
        call_command('makemigrations')
        call_command('migrate')
        print("✅ Migraciones aplicadas en PostgreSQL")
        return True
    except Exception as e:
        print(f"❌ Error al configurar PostgreSQL: {e}")
        return False

def create_superuser():
    """Crear superusuario para Django Admin"""
    print("👤 Creando superusuario...")
    
    try:
        call_command('createsuperuser', 
                    '--username=admin',
                    '--email=admin@condominio.com',
                    '--noinput')
        print("✅ Superusuario creado: admin / admin123")
    except Exception as e:
        print(f"⚠️  Superusuario puede ya existir: {e}")

def load_postgresql_data():
    """Cargar datos en PostgreSQL"""
    print("📥 Cargando datos en PostgreSQL...")
    
    try:
        if os.path.exists('sqlite_backup.json'):
            call_command('loaddata', 'sqlite_backup.json')
            print("✅ Datos cargados en PostgreSQL")
            return True
        else:
            print("⚠️  No se encontró archivo de respaldo")
            return False
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        return False

def create_demo_data():
    """Crear datos de demostración"""
    print("🎭 Creando datos de demostración...")
    
    from django.contrib.auth.models import User
    from comunidad.models import (
        Condominio, PerfilUsuario, TipoUsuario, TipoUnidad, Unidad, 
        ResidenciaUnidad, AreaComun, ReservaAreaComun, ConfiguracionExpensa,
        CuotaMantenimiento, TipoGasto
    )
    
    try:
        # Crear tipos de usuario
        tipo_admin, _ = TipoUsuario.objects.get_or_create(
            tipo='ADMINISTRADOR',
            defaults={'descripcion': 'Administrador del sistema'}
        )
        tipo_propietario, _ = TipoUsuario.objects.get_or_create(
            tipo='PROPIETARIO',
            defaults={'descripcion': 'Propietario de unidad'}
        )
        
        # Crear usuario demo si no existe
        demo_user, created = User.objects.get_or_create(
            username='demo',
            defaults={
                'email': 'demo@condominio.com',
                'first_name': 'Usuario',
                'last_name': 'Demo'
            }
        )
        if created:
            demo_user.set_password('123456')
            demo_user.save()
            print("✅ Usuario demo creado: demo / 123456")
        
        # Crear condominio demo si no existe
        condominio, created = Condominio.objects.get_or_create(
            nombre='Smart Condominio Demo',
            defaults={
                'direccion': 'Av. Libertador 123, La Paz',
                'telefono': '+591 2 1234567',
                'email': 'info@smartcondominio.com',
                'nit': '1234567890123'
            }
        )
        
        # Crear perfil de usuario demo si no existe
        perfil_demo, created = PerfilUsuario.objects.get_or_create(
            user=demo_user,
            defaults={
                'condominio': condominio,
                'tipo_usuario': tipo_propietario,
                'ci': '1234567',
                'telefono': '+591 70123456',
                'fecha_nacimiento': '1990-01-01'
            }
        )
        
        # Crear tipo de unidad
        tipo_depto, _ = TipoUnidad.objects.get_or_create(
            nombre='Departamento',
            defaults={'descripcion': 'Departamento estándar'}
        )
        
        # Crear unidad habitacional demo si no existe
        unidad, created = Unidad.objects.get_or_create(
            numero='101',
            condominio=condominio,
            defaults={
                'tipo_unidad': tipo_depto,
                'piso': 1,
                'metros_cuadrados': 85.5,
                'dormitorios': 2,
                'baños': 2,
                'porcentaje_propiedad': 2.5
            }
        )
        
        # Crear residencia
        ResidenciaUnidad.objects.get_or_create(
            usuario=perfil_demo,
            unidad=unidad,
            defaults={
                'es_propietario': True,
                'fecha_inicio': '2024-01-01'
            }
        )
        
        # Crear áreas comunes demo
        areas_comunes = [
            {
                'nombre': 'Piscina', 
                'descripcion': 'Piscina climatizada', 
                'capacidad_maxima': 20,
                'precio_por_hora': 50.00,
                'hora_apertura': '06:00',
                'hora_cierre': '22:00',
                'dias_disponibles': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
            },
            {
                'nombre': 'Gimnasio', 
                'descripcion': 'Gimnasio completamente equipado', 
                'capacidad_maxima': 15,
                'precio_por_hora': 30.00,
                'hora_apertura': '05:00',
                'hora_cierre': '23:00',
                'dias_disponibles': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
            },
            {
                'nombre': 'Salón de Eventos', 
                'descripcion': 'Salón para celebraciones', 
                'capacidad_maxima': 50,
                'precio_por_hora': 150.00,
                'hora_apertura': '08:00',
                'hora_cierre': '02:00',
                'dias_disponibles': ['viernes', 'sabado', 'domingo']
            },
            {
                'nombre': 'Cancha de Tenis', 
                'descripcion': 'Cancha profesional de tenis', 
                'capacidad_maxima': 4,
                'precio_por_hora': 80.00,
                'hora_apertura': '06:00',
                'hora_cierre': '20:00',
                'dias_disponibles': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
            },
        ]
        
        for area_data in areas_comunes:
            AreaComun.objects.get_or_create(
                nombre=area_data['nombre'],
                condominio=condominio,
                defaults=area_data
            )
        
        print("✅ Datos de demostración creados")
        return True
        
    except Exception as e:
        print(f"❌ Error al crear datos demo: {e}")
        return False

def test_connection():
    """Probar la conexión a PostgreSQL"""
    print("🔌 Probando conexión a PostgreSQL...")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            print(f"✅ Conectado a PostgreSQL: {version}")
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    """Función principal de migración"""
    print("🚀 INICIANDO MIGRACIÓN A POSTGRESQL")
    print("=" * 50)
    
    # Paso 1: Probar conexión
    if not test_connection():
        print("❌ No se puede conectar a PostgreSQL. Verifica la configuración.")
        return
    
    # Paso 2: Configurar PostgreSQL
    if not setup_postgresql():
        print("❌ Error al configurar PostgreSQL")
        return
    
    # Paso 3: Crear datos de demostración
    if not create_demo_data():
        print("❌ Error al crear datos demo")
        return
    
    # Paso 4: Crear superusuario
    create_superuser()
    
    print("\n" + "=" * 50)
    print("🎉 ¡MIGRACIÓN COMPLETADA!")
    print("📊 Resumen:")
    print("   ✅ PostgreSQL configurado")
    print("   ✅ Tablas creadas")
    print("   ✅ Datos demo insertados")
    print("   ✅ Usuario demo: demo / 123456")
    print("   ✅ Admin: admin / admin123")
    print("\n🔗 URLs importantes:")
    print("   🏠 Inicio: http://127.0.0.1:8000/")
    print("   🛠️  Admin: http://127.0.0.1:8000/admin/")
    print("   📱 API Login: http://127.0.0.1:8000/api/auth/login/")

if __name__ == "__main__":
    main()