# 🏢 Script ejecutable para crear base de datos completa

import subprocess
import sys
import os

def ejecutar_script():
    """Ejecutar el script de población de base de datos"""
    
    # Cambiar al directorio correcto
    os.chdir(r'D:\condominio\backend')
    
    # Código Python para ejecutar
    codigo_python = '''
import os
import django
from datetime import datetime, date, timedelta
from decimal import Decimal
import random

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import transaction
from comunidad.models import (
    Condominio, TipoUsuario, PerfilUsuario, TipoUnidad, Unidad,
    ResidenciaUnidad, Vehiculo, AreaComun, ReservaAreaComun,
    CamaraSeguridad, RegistroAcceso, Visitante, AlertaSeguridad,
    TipoGasto, ConfiguracionExpensa, CuotaMantenimiento, MetodoPago, Pago
)

def limpiar_datos_demo():
    """Limpiar datos de demostración existentes"""
    print("🧹 Limpiando datos de demostración...")
    
    # Eliminar usuarios demo
    User.objects.filter(username__in=["demo", "admin"]).delete()
    
    # Limpiar todas las tablas principales
    Condominio.objects.all().delete()
    TipoUsuario.objects.all().delete()
    TipoUnidad.objects.all().delete()
    
    print("✅ Datos demo eliminados")

def crear_tipos_base():
    """Crear tipos y configuraciones base del sistema"""
    print("🔧 Creando tipos y configuraciones base...")
    
    # Tipos de usuario
    tipos_usuario = [
        ("ADMINISTRADOR", "Administrador del Condominio"),
        ("PROPIETARIO", "Propietario de Unidad"),
        ("INQUILINO", "Inquilino"),
        ("SEGURIDAD", "Personal de Seguridad"),
        ("MANTENIMIENTO", "Personal de Mantenimiento"),
        ("VISITANTE", "Visitante"),
    ]
    
    for tipo, desc in tipos_usuario:
        TipoUsuario.objects.get_or_create(
            tipo=tipo,
            defaults={"descripcion": desc}
        )
    
    # Tipos de unidad
    tipos_unidad = [
        ("Departamento 1 Dorm", "Departamento de 1 dormitorio", 0.8),
        ("Departamento 2 Dorm", "Departamento de 2 dormitorios", 1.0),
        ("Departamento 3 Dorm", "Departamento de 3 dormitorios", 1.3),
        ("Penthouse", "Penthouse de lujo", 2.0),
        ("Oficina", "Oficina comercial", 0.6),
        ("Local Comercial", "Local comercial", 1.5),
        ("Depósito", "Depósito de almacenamiento", 0.4),
    ]
    
    for nombre, desc, factor in tipos_unidad:
        TipoUnidad.objects.get_or_create(
            nombre=nombre,
            defaults={
                "descripcion": desc,
                "factor_costo": Decimal(str(factor))
            }
        )
    
    print("✅ Tipos base creados")

def crear_condominio_principal():
    """Crear el condominio principal"""
    print("🏢 Creando condominio principal...")
    
    condominio = Condominio.objects.create(
        nombre="Residencial Las Torres",
        direccion="Av. Banzer Km 9, Entre 4to y 5to Anillo, Santa Cruz de la Sierra",
        telefono="+591 3 123-4567",
        email="administracion@lastorres.com",
        nit="1023456789012",
        codigo_postal="0000",
        ciudad="Santa Cruz de la Sierra",
        pais="Bolivia"
    )
    
    print(f"✅ Condominio creado: {condominio.nombre}")
    return condominio

def crear_admin_principal():
    """Crear administrador principal del sistema"""
    print("👨‍💼 Creando administrador principal...")
    
    # Crear usuario admin
    admin_user = User.objects.create_user(
        username="admin_general",
        email="admin@lastorres.com",
        first_name="Carlos",
        last_name="Mendoza",
        password="Admin2025!"
    )
    
    print("✅ Administrador creado: admin_general / Admin2025!")
    return admin_user

def crear_usuarios_propietarios():
    """Crear usuarios propietarios de ejemplo"""
    print("🏠 Creando propietarios...")
    
    # Obtener condominio y tipo de usuario
    condominio = Condominio.objects.first()
    tipo_propietario = TipoUsuario.objects.get(tipo="PROPIETARIO")
    
    propietarios_data = [
        {
            "username": "prop_juan",
            "email": "juan.silva@email.com",
            "first_name": "Juan",
            "last_name": "Silva",
            "password": "Prop2025!",
            "ci": "12345678",
            "telefono": "+591 70111222"
        },
        {
            "username": "prop_ana",
            "email": "ana.martinez@email.com", 
            "first_name": "Ana",
            "last_name": "Martínez",
            "password": "Prop2025!",
            "ci": "87654321",
            "telefono": "+591 70222333"
        },
        {
            "username": "prop_miguel",
            "email": "miguel.lopez@email.com",
            "first_name": "Miguel", 
            "last_name": "López",
            "password": "Prop2025!",
            "ci": "11223344",
            "telefono": "+591 70333444"
        }
    ]
    
    propietarios_creados = []
    
    for prop_data in propietarios_data:
        # Crear usuario
        user = User.objects.create_user(
            username=prop_data["username"],
            email=prop_data["email"],
            first_name=prop_data["first_name"],
            last_name=prop_data["last_name"],
            password=prop_data["password"]
        )
        
        # Crear perfil
        perfil = PerfilUsuario.objects.create(
            user=user,
            condominio=condominio,
            tipo_usuario=tipo_propietario,
            ci=prop_data["ci"],
            telefono=prop_data["telefono"],
            fecha_nacimiento=date(1980, 1, 1)
        )
        
        propietarios_creados.append(perfil)
    
    print(f"✅ {len(propietarios_creados)} propietarios creados")
    return propietarios_creados

def crear_unidades_basicas():
    """Crear unidades básicas del condominio"""
    print("🏠 Creando unidades...")
    
    condominio = Condominio.objects.first()
    tipo_2dorm = TipoUnidad.objects.get(nombre="Departamento 2 Dorm")
    tipo_3dorm = TipoUnidad.objects.get(nombre="Departamento 3 Dorm")
    
    unidades_data = [
        ("101", tipo_2dorm, 1, "A", 75.5, 2, 2, 2.5),
        ("102", tipo_2dorm, 1, "A", 75.5, 2, 2, 2.5),
        ("201", tipo_3dorm, 2, "A", 95.0, 3, 2, 3.0),
        ("202", tipo_3dorm, 2, "A", 95.0, 3, 2, 3.0),
        ("301", tipo_3dorm, 3, "A", 95.0, 3, 2, 3.0),
    ]
    
    unidades_creadas = []
    
    for numero, tipo, piso, bloque, m2, dorm, banos, porcentaje in unidades_data:
        unidad = Unidad.objects.create(
            condominio=condominio,
            numero=numero,
            tipo_unidad=tipo,
            piso=piso,
            bloque=bloque,
            metros_cuadrados=Decimal(str(m2)),
            dormitorios=dorm,
            baños=banos,
            porcentaje_propiedad=Decimal(str(porcentaje))
        )
        unidades_creadas.append(unidad)
    
    print(f"✅ {len(unidades_creadas)} unidades creadas")
    return unidades_creadas

def crear_areas_comunes():
    """Crear áreas comunes del condominio"""
    print("🏊 Creando áreas comunes...")
    
    condominio = Condominio.objects.first()
    
    areas_data = [
        {
            "nombre": "Piscina Principal",
            "descripcion": "Piscina climatizada con área para niños",
            "capacidad_maxima": 30,
            "precio_por_hora": Decimal("80.00"),
            "hora_apertura": "06:00",
            "hora_cierre": "22:00",
            "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        },
        {
            "nombre": "Gimnasio",
            "descripcion": "Gimnasio completamente equipado con máquinas modernas",
            "capacidad_maxima": 20,
            "precio_por_hora": Decimal("50.00"),
            "hora_apertura": "05:00",
            "hora_cierre": "23:00",
            "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        },
        {
            "nombre": "Salón de Eventos",
            "descripcion": "Salón para celebraciones y eventos familiares",
            "capacidad_maxima": 80,
            "precio_por_hora": Decimal("200.00"),
            "requiere_deposito": True,
            "monto_deposito": Decimal("500.00"),
            "hora_apertura": "08:00",
            "hora_cierre": "02:00",
            "dias_disponibles": ["viernes", "sabado", "domingo"]
        },
        {
            "nombre": "Cancha de Tenis",
            "descripcion": "Cancha de tenis profesional con iluminación",
            "capacidad_maxima": 4,
            "precio_por_hora": Decimal("120.00"),
            "hora_apertura": "06:00",
            "hora_cierre": "22:00",
            "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        },
        {
            "nombre": "Área de BBQ",
            "descripcion": "Área de parrillas con mesas y sillas",
            "capacidad_maxima": 25,
            "precio_por_hora": Decimal("60.00"),
            "hora_apertura": "10:00",
            "hora_cierre": "22:00",
            "dias_disponibles": ["sabado", "domingo"]
        },
        {
            "nombre": "Sala de Juegos",
            "descripcion": "Sala con mesa de pool, ping pong y juegos",
            "capacidad_maxima": 15,
            "precio_por_hora": Decimal("40.00"),
            "hora_apertura": "09:00",
            "hora_cierre": "21:00",
            "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        }
    ]
    
    areas_creadas = []
    
    for area_data in areas_data:
        area = AreaComun.objects.create(
            condominio=condominio,
            **area_data
        )
        areas_creadas.append(area)
    
    print(f"✅ {len(areas_creadas)} áreas comunes creadas")
    return areas_creadas

def main():
    """Función principal"""
    print("🚀 INICIANDO CREACIÓN DE BASE DE DATOS COMPLETA")
    print("=" * 60)
    
    try:
        # Limpiar datos anteriores
        limpiar_datos_demo()
        
        # Crear tipos base
        crear_tipos_base()
        
        # Crear condominio
        condominio = crear_condominio_principal()
        
        # Crear administrador
        admin = crear_admin_principal()
        
        # Crear propietarios
        propietarios = crear_usuarios_propietarios()
        
        # Crear unidades
        unidades = crear_unidades_basicas()
        
        # Crear áreas comunes
        areas = crear_areas_comunes()
        
        print("\\n" + "=" * 60)
        print("🎉 ¡BASE DE DATOS CREADA EXITOSAMENTE!")
        print("📊 Resumen:")
        print(f"   🏢 Condominio: Residencial Las Torres")
        print(f"   👨‍💼 Administrador: admin_general")
        print(f"   🏠 Propietarios: {len(propietarios)}")
        print(f"   🏠 Unidades: {len(unidades)}")
        print(f"   🏊 Áreas comunes: {len(areas)}")
        
        print("\\n🔐 Credenciales principales:")
        print("   👨‍💼 Administrador:")
        print("     Username: admin_general")
        print("     Password: Admin2025!")
        print("   🏠 Propietario ejemplo:")
        print("     Username: prop_juan")
        print("     Password: Prop2025!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
'''
    
    # Ejecutar usando Python del entorno virtual
    python_exe = r'D:\condominio\backend\venv\Scripts\python.exe'
    
    try:
        # Ejecutar el código Python
        result = subprocess.run(
            [python_exe, '-c', codigo_python],
            cwd=r'D:\condominio\backend',
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("Errores:", result.stderr)
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("❌ El script tardó demasiado en ejecutarse")
        return False
    except Exception as e:
        print(f"❌ Error al ejecutar el script: {e}")
        return False

if __name__ == "__main__":
    exito = ejecutar_script()
    if exito:
        print("✅ Script completado exitosamente")
    else:
        print("❌ El script falló")