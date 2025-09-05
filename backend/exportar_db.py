# 📊 Script para exportar base de datos PostgreSQL - Smart Condominio

import os
import django
import json
from datetime import datetime

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core import serializers
from django.apps import apps

def exportar_base_datos():
    """Exportar toda la base de datos a JSON"""
    print("📊 EXPORTANDO BASE DE DATOS POSTGRESQL")
    print("=" * 50)
    
    # Obtener todos los modelos de la app comunidad
    modelos_comunidad = apps.get_app_config('comunidad').get_models()
    
    # Datos para exportar
    datos_exportados = []
    
    print("📋 Exportando modelos:")
    
    for modelo in modelos_comunidad:
        nombre_modelo = f"{modelo._meta.app_label}.{modelo._meta.model_name}"
        objetos = modelo.objects.all()
        
        if objetos.exists():
            print(f"   📄 {nombre_modelo}: {objetos.count()} registros")
            
            # Serializar objetos
            for obj in objetos:
                try:
                    serialized = serializers.serialize('json', [obj])
                    datos_exportados.extend(json.loads(serialized))
                except Exception as e:
                    print(f"   ⚠️  Error en {nombre_modelo}: {e}")
        else:
            print(f"   📭 {nombre_modelo}: Sin registros")
    
    # Exportar usuarios también
    from django.contrib.auth.models import User
    usuarios = User.objects.all()
    if usuarios.exists():
        print(f"   👥 auth.user: {usuarios.count()} usuarios")
        for user in usuarios:
            try:
                serialized = serializers.serialize('json', [user])
                datos_exportados.extend(json.loads(serialized))
            except Exception as e:
                print(f"   ⚠️  Error en usuarios: {e}")
    
    # Guardar archivo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"base_datos_postgresql_{timestamp}.json"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos_exportados, archivo, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Base de datos exportada a: {nombre_archivo}")
    print(f"📊 Total de registros: {len(datos_exportados)}")
    
    # Mostrar resumen por modelo
    print("\n📋 Resumen por modelo:")
    modelos_conteo = {}
    for item in datos_exportados:
        modelo = item['model']
        modelos_conteo[modelo] = modelos_conteo.get(modelo, 0) + 1
    
    for modelo, cantidad in sorted(modelos_conteo.items()):
        print(f"   {modelo}: {cantidad}")
    
    return nombre_archivo

def exportar_estructura_db():
    """Exportar solo la estructura de la base de datos"""
    print("\n🏗️  EXPORTANDO ESTRUCTURA DE BASE DE DATOS")
    print("=" * 50)
    
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Obtener todas las tablas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
            ORDER BY table_name;
        """)
        
        tablas = cursor.fetchall()
        
        estructura = {
            "database": "postgresql",
            "timestamp": datetime.now().isoformat(),
            "tables": {}
        }
        
        print("📋 Tablas encontradas:")
        
        for (tabla,) in tablas:
            print(f"   📄 {tabla}")
            
            # Obtener información de columnas
            cursor.execute("""
                SELECT 
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length
                FROM information_schema.columns 
                WHERE table_name = %s 
                ORDER BY ordinal_position;
            """, [tabla])
            
            columnas = cursor.fetchall()
            
            estructura["tables"][tabla] = {
                "columns": [
                    {
                        "name": col[0],
                        "type": col[1],
                        "nullable": col[2] == 'YES',
                        "default": col[3],
                        "max_length": col[4]
                    }
                    for col in columnas
                ]
            }
    
    # Guardar estructura
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"estructura_db_{timestamp}.json"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(estructura, archivo, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Estructura exportada a: {nombre_archivo}")
    print(f"📊 Total de tablas: {len(estructura['tables'])}")
    
    return nombre_archivo

def mostrar_estadisticas():
    """Mostrar estadísticas de la base de datos"""
    print("\n📊 ESTADÍSTICAS DE LA BASE DE DATOS")
    print("=" * 50)
    
    from django.contrib.auth.models import User
    from comunidad.models import (
        Condominio, PerfilUsuario, Unidad, AreaComun, 
        TipoUsuario, TipoUnidad, ResidenciaUnidad
    )
    
    stats = {
        "👥 Usuarios del sistema": User.objects.count(),
        "🏢 Condominios": Condominio.objects.count(),
        "👤 Perfiles de usuario": PerfilUsuario.objects.count(),
        "🏠 Unidades": Unidad.objects.count(),
        "🏊 Áreas comunes": AreaComun.objects.count(),
        "🔑 Residencias": ResidenciaUnidad.objects.count(),
        "📝 Tipos de usuario": TipoUsuario.objects.count(),
        "🏗️  Tipos de unidad": TipoUnidad.objects.count(),
    }
    
    for descripcion, cantidad in stats.items():
        print(f"   {descripcion}: {cantidad}")
    
    # Mostrar propietarios por condominio
    print("\n🏢 Propietarios por condominio:")
    for condominio in Condominio.objects.all():
        propietarios = PerfilUsuario.objects.filter(
            condominio=condominio,
            tipo_usuario__tipo='PROPIETARIO'
        ).count()
        print(f"   {condominio.nombre}: {propietarios} propietarios")

def main():
    """Función principal"""
    try:
        # Mostrar estadísticas
        mostrar_estadisticas()
        
        # Exportar datos
        archivo_datos = exportar_base_datos()
        
        # Exportar estructura
        archivo_estructura = exportar_estructura_db()
        
        print("\n" + "=" * 50)
        print("🎉 EXPORTACIÓN COMPLETADA")
        print("\n📁 Archivos generados:")
        print(f"   📊 Datos: {archivo_datos}")
        print(f"   🏗️  Estructura: {archivo_estructura}")
        
        print("\n💡 Para compartir:")
        print("   1. Comparte el archivo de datos para importar todo")
        print("   2. Comparte el archivo de estructura para ver la organización")
        print("   3. O comparte ambos para análisis completo")
        
    except Exception as e:
        print(f"❌ Error durante la exportación: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()