# 🏢 Script de Población de Base de Datos - Smart Condominio
# Datos reales y profesionales para el sistema

import os
import django
from datetime import datetime, date, timedelta
from decimal import Decimal
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
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
    User.objects.filter(username__in=['demo', 'admin']).delete()
    
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
        ('ADMINISTRADOR', 'Administrador del Condominio'),
        ('PROPIETARIO', 'Propietario de Unidad'),
        ('INQUILINO', 'Inquilino'),
        ('SEGURIDAD', 'Personal de Seguridad'),
        ('MANTENIMIENTO', 'Personal de Mantenimiento'),
        ('VISITANTE', 'Visitante'),
    ]
    
    for tipo, desc in tipos_usuario:
        TipoUsuario.objects.get_or_create(
            tipo=tipo,
            defaults={'descripcion': desc}
        )
    
    # Tipos de unidad
    tipos_unidad = [
        ('Departamento 1 Dorm', 'Departamento de 1 dormitorio', 0.8),
        ('Departamento 2 Dorm', 'Departamento de 2 dormitorios', 1.0),
        ('Departamento 3 Dorm', 'Departamento de 3 dormitorios', 1.3),
        ('Penthouse', 'Penthouse de lujo', 2.0),
        ('Oficina', 'Oficina comercial', 0.6),
        ('Local Comercial', 'Local comercial', 1.5),
        ('Depósito', 'Depósito de almacenamiento', 0.4),
    ]
    
    for nombre, desc, factor in tipos_unidad:
        TipoUnidad.objects.get_or_create(
            nombre=nombre,
            defaults={
                'descripcion': desc,
                'factor_costo': Decimal(str(factor))
            }
        )
    
    print("✅ Tipos base creados")

def crear_condominio_principal():
    """Crear el condominio principal"""
    print("🏢 Creando condominio principal...")
    
    condominio = Condominio.objects.create(
        nombre='Residencial Las Torres',
        direccion='Av. Banzer Km 9, Entre 4to y 5to Anillo, Santa Cruz de la Sierra',
        telefono='+591 3 123-4567',
        email='administracion@lastorres.com',
        nit='1023456789012',
        codigo_postal='0000',
        ciudad='Santa Cruz de la Sierra',
        pais='Bolivia'
    )
    
    print(f"✅ Condominio creado: {condominio.nombre}")
    return condominio

def crear_usuarios_sistema(condominio):
    """Crear usuarios del sistema"""
    print("👥 Creando usuarios del sistema...")
    
    usuarios_data = [
        # Administradores
        {
            'username': 'admin_general',
            'email': 'admin@lastorres.com',
            'first_name': 'Carlos',
            'last_name': 'Mendoza',
            'password': 'Admin2025!',
            'tipo': 'ADMINISTRADOR',
            'ci': '12345678',
            'telefono': '+591 70123456',
            'fecha_nacimiento': date(1985, 5, 15)
        },
        {
            'username': 'admin_finanzas',
            'email': 'finanzas@lastorres.com',
            'first_name': 'María',
            'last_name': 'Rodríguez',
            'password': 'Finanzas2025!',
            'tipo': 'ADMINISTRADOR',
            'ci': '87654321',
            'telefono': '+591 70234567',
            'fecha_nacimiento': date(1990, 8, 22)
        },
        
        # Personal de Seguridad
        {
            'username': 'seguridad_dia',
            'email': 'seguridad.dia@lastorres.com',
            'first_name': 'Roberto',
            'last_name': 'Chávez',
            'password': 'Seguridad2025!',
            'tipo': 'SEGURIDAD',
            'ci': '11223344',
            'telefono': '+591 70345678',
            'fecha_nacimiento': date(1988, 3, 10)
        },
        {
            'username': 'seguridad_noche',
            'email': 'seguridad.noche@lastorres.com',
            'first_name': 'Luis',
            'last_name': 'Morales',
            'password': 'Seguridad2025!',
            'tipo': 'SEGURIDAD',
            'ci': '44332211',
            'telefono': '+591 70456789',
            'fecha_nacimiento': date(1982, 11, 5)
        },
        
        # Personal de Mantenimiento
        {
            'username': 'mantenimiento',
            'email': 'mantenimiento@lastorres.com',
            'first_name': 'Pedro',
            'last_name': 'Vargas',
            'password': 'Manten2025!',
            'tipo': 'MANTENIMIENTO',
            'ci': '55667788',
            'telefono': '+591 70567890',
            'fecha_nacimiento': date(1975, 7, 18)
        },
        
        # Propietarios
        {
            'username': 'prop_101',
            'email': 'juan.silva@email.com',
            'first_name': 'Juan',
            'last_name': 'Silva Torrez',
            'password': 'Prop2025!',
            'tipo': 'PROPIETARIO',
            'ci': '98765432',
            'telefono': '+591 70111222',
            'fecha_nacimiento': date(1978, 4, 12)
        },
        {
            'username': 'prop_201',
            'email': 'ana.martinez@email.com',
            'first_name': 'Ana',
            'last_name': 'Martínez Vega',
            'password': 'Prop2025!',
            'tipo': 'PROPIETARIO',
            'ci': '13579246',
            'telefono': '+591 70222333',
            'fecha_nacimiento': date(1983, 9, 28)
        },
        {
            'username': 'prop_301',
            'email': 'miguel.lopez@email.com',
            'first_name': 'Miguel',
            'last_name': 'López Santos',
            'password': 'Prop2025!',
            'tipo': 'PROPIETARIO',
            'ci': '24681357',
            'telefono': '+591 70333444',
            'fecha_nacimiento': date(1980, 12, 3)
        },
        {
            'username': 'prop_401',
            'email': 'lucia.garcia@email.com',
            'first_name': 'Lucía',
            'last_name': 'García Flores',
            'password': 'Prop2025!',
            'tipo': 'PROPIETARIO',
            'ci': '97531864',
            'telefono': '+591 70444555',
            'fecha_nacimiento': date(1985, 2, 17)
        },
        {
            'username': 'prop_ph1',
            'email': 'ricardo.perez@email.com',
            'first_name': 'Ricardo',
            'last_name': 'Pérez Moreno',
            'password': 'Prop2025!',
            'tipo': 'PROPIETARIO',
            'ci': '86420975',
            'telefono': '+591 70555666',
            'fecha_nacimiento': date(1976, 6, 9)
        },
        
        # Inquilinos
        {
            'username': 'inq_102',
            'email': 'sofia.ramirez@email.com',
            'first_name': 'Sofía',
            'last_name': 'Ramírez Cruz',
            'password': 'Inq2025!',
            'tipo': 'INQUILINO',
            'ci': '75319864',
            'telefono': '+591 70666777',
            'fecha_nacimiento': date(1992, 1, 25)
        },
        {
            'username': 'inq_202',
            'email': 'carlos.herrera@email.com',
            'first_name': 'Carlos',
            'last_name': 'Herrera Paz',
            'password': 'Inq2025!',
            'tipo': 'INQUILINO',
            'ci': '64208531',
            'telefono': '+591 70777888',
            'fecha_nacimiento': date(1987, 10, 14)
        }
    ]
    
    perfiles_creados = []
    
    with transaction.atomic():
        for user_data in usuarios_data:
            # Crear usuario Django
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password']
            )
            
            # Crear perfil
            tipo_usuario = TipoUsuario.objects.get(tipo=user_data['tipo'])
            perfil = PerfilUsuario.objects.create(
                user=user,
                condominio=condominio,
                tipo_usuario=tipo_usuario,
                ci=user_data['ci'],
                telefono=user_data['telefono'],
                fecha_nacimiento=user_data['fecha_nacimiento']
            )
            
            perfiles_creados.append(perfil)
    
    print(f"✅ {len(perfiles_creados)} usuarios creados")
    return perfiles_creados

def crear_unidades(condominio):
    """Crear unidades del condominio"""
    print("🏠 Creando unidades del condominio...")
    
    # Obtener tipos de unidad
    tipo_1dorm = TipoUnidad.objects.get(nombre='Departamento 1 Dorm')
    tipo_2dorm = TipoUnidad.objects.get(nombre='Departamento 2 Dorm')
    tipo_3dorm = TipoUnidad.objects.get(nombre='Departamento 3 Dorm')
    tipo_ph = TipoUnidad.objects.get(nombre='Penthouse')
    tipo_oficina = TipoUnidad.objects.get(nombre='Oficina')
    tipo_local = TipoUnidad.objects.get(nombre='Local Comercial')
    tipo_deposito = TipoUnidad.objects.get(nombre='Depósito')
    
    unidades_data = [
        # Torre A - Departamentos
        ('A-101', tipo_2dorm, 1, 'A', 75.5, 2, 2, 2.5),
        ('A-102', tipo_1dorm, 1, 'A', 55.0, 1, 1, 1.8),
        ('A-103', tipo_2dorm, 1, 'A', 80.0, 2, 2, 2.6),
        ('A-201', tipo_2dorm, 2, 'A', 75.5, 2, 2, 2.5),
        ('A-202', tipo_1dorm, 2, 'A', 55.0, 1, 1, 1.8),
        ('A-203', tipo_2dorm, 2, 'A', 80.0, 2, 2, 2.6),
        ('A-301', tipo_3dorm, 3, 'A', 110.0, 3, 3, 3.5),
        ('A-302', tipo_2dorm, 3, 'A', 75.5, 2, 2, 2.5),
        ('A-401', tipo_3dorm, 4, 'A', 110.0, 3, 3, 3.5),
        ('A-402', tipo_2dorm, 4, 'A', 75.5, 2, 2, 2.5),
        ('A-PH1', tipo_ph, 5, 'A', 180.0, 4, 4, 6.0),
        
        # Torre B - Departamentos
        ('B-101', tipo_2dorm, 1, 'B', 78.0, 2, 2, 2.6),
        ('B-102', tipo_3dorm, 1, 'B', 105.0, 3, 2, 3.4),
        ('B-201', tipo_2dorm, 2, 'B', 78.0, 2, 2, 2.6),
        ('B-202', tipo_3dorm, 2, 'B', 105.0, 3, 2, 3.4),
        ('B-301', tipo_3dorm, 3, 'B', 115.0, 3, 3, 3.7),
        ('B-302', tipo_2dorm, 3, 'B', 78.0, 2, 2, 2.6),
        ('B-401', tipo_3dorm, 4, 'B', 115.0, 3, 3, 3.7),
        ('B-PH1', tipo_ph, 5, 'B', 200.0, 4, 4, 6.5),
        
        # Planta Baja - Comercial
        ('PB-01', tipo_oficina, 0, 'PB', 35.0, 0, 1, 1.2),
        ('PB-02', tipo_oficina, 0, 'PB', 42.0, 0, 1, 1.4),
        ('PB-03', tipo_local, 0, 'PB', 65.0, 0, 1, 2.2),
        ('PB-04', tipo_local, 0, 'PB', 85.0, 0, 2, 2.8),
        
        # Subsuelo - Depósitos
        ('SS-01', tipo_deposito, -1, 'SS', 8.0, 0, 0, 0.3),
        ('SS-02', tipo_deposito, -1, 'SS', 12.0, 0, 0, 0.4),
        ('SS-03', tipo_deposito, -1, 'SS', 10.0, 0, 0, 0.35),
        ('SS-04', tipo_deposito, -1, 'SS', 15.0, 0, 0, 0.5),
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

def asignar_residencias(unidades, perfiles):
    """Asignar propietarios e inquilinos a las unidades"""
    print("🔑 Asignando residencias...")
    
    # Filtrar por tipo de usuario
    propietarios = [p for p in perfiles if p.tipo_usuario.tipo == 'PROPIETARIO']
    inquilinos = [p for p in perfiles if p.tipo_usuario.tipo == 'INQUILINO']
    
    residencias_data = [
        # Propietarios
        ('A-101', 'prop_101', True),
        ('A-201', 'prop_201', True),
        ('A-301', 'prop_301', True),
        ('A-401', 'prop_401', True),
        ('A-PH1', 'prop_ph1', True),
        
        # Inquilinos
        ('A-102', 'inq_102', False),
        ('B-202', 'inq_202', False),
    ]
    
    residencias_creadas = []
    
    for numero_unidad, username, es_propietario in residencias_data:
        try:
            unidad = next(u for u in unidades if u.numero == numero_unidad)
            perfil = next(p for p in perfiles if p.user.username == username)
            
            residencia = ResidenciaUnidad.objects.create(
                usuario=perfil,
                unidad=unidad,
                es_propietario=es_propietario,
                porcentaje_propiedad=Decimal('100.00') if es_propietario else Decimal('0.00'),
                fecha_inicio=date(2024, 1, 1)
            )
            residencias_creadas.append(residencia)
        except StopIteration:
            continue
    
    print(f"✅ {len(residencias_creadas)} residencias asignadas")
    return residencias_creadas

def main():
    """Función principal"""
    print("🚀 INICIANDO CREACIÓN DE BASE DE DATOS COMPLETA")
    print("=" * 60)
    
    try:
        # Paso 1: Limpiar datos demo
        limpiar_datos_demo()
        
        # Paso 2: Crear tipos base
        crear_tipos_base()
        
        # Paso 3: Crear condominio
        condominio = crear_condominio_principal()
        
        # Paso 4: Crear usuarios
        perfiles = crear_usuarios_sistema(condominio)
        
        # Paso 5: Crear unidades
        unidades = crear_unidades(condominio)
        
        # Paso 6: Asignar residencias
        residencias = asignar_residencias(unidades, perfiles)
        
        print("\n" + "=" * 60)
        print("🎉 ¡BASE DE DATOS CREADA EXITOSAMENTE!")
        print("📊 Resumen:")
        print(f"   🏢 Condominio: {condominio.nombre}")
        print(f"   👥 Usuarios: {len(perfiles)}")
        print(f"   🏠 Unidades: {len(unidades)}")
        print(f"   🔑 Residencias: {len(residencias)}")
        
        print("\n🔐 Credenciales de acceso:")
        print("   Administrador General:")
        print("     Username: admin_general")
        print("     Password: Admin2025!")
        print("   Propietario Torre A-101:")
        print("     Username: prop_101")
        print("     Password: Prop2025!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == "__main__":
    main()