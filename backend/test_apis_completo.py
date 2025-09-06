#!/usr/bin/env python
"""
Script de prueba para verificar las APIs del proyecto Smart Condominio
Versión actualizada para trabajar con usuarios existentes
"""
import requests
import json
from datetime import datetime

def imprimir_separador(titulo):
    """Imprimir un separador visual"""
    print("\n" + "=" * 60)
    print(f"🏠 {titulo}")
    print("=" * 60)

def probar_conexion_basica():
    """Probar conexión básica al servidor Django"""
    imprimir_separador("PRUEBA DE CONEXIÓN BÁSICA")
    
    try:
        print("🔍 Probando conexión al servidor Django...")
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"✅ Conexión exitosa - Status: {response.status_code}")
        
        # Verificar que sea Django
        if "Django" in response.text:
            print("🎯 Servidor Django detectado correctamente")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor")
        print("   Asegúrate de que Django esté corriendo en: python manage.py runserver")
        return False
    except requests.exceptions.Timeout:
        print("⏰ Error: Timeout de conexión")
        return False
    except Exception as e:
        print(f"💥 Error inesperado: {e}")
        return False

def probar_api_login():
    """Probar la API de login con usuarios existentes"""
    imprimir_separador("PRUEBA DE API DE LOGIN")
    
    # Lista de usuarios para probar
    usuarios_prueba = [
        {
            "email": "juan.silva@email.com", 
            "password": "Prop2025!",
            "nombre": "Juan Silva Torrez"
        },
        {
            "email": "ana.martinez@email.com", 
            "password": "Prop2025!",
            "nombre": "Ana Martínez Vega"
        },
        {
            "email": "admin@lastorres.com", 
            "password": "Admin2025!",
            "nombre": "Carlos Mendoza (Admin)"
        }
    ]
    
    for usuario in usuarios_prueba:
        print(f"\n🔐 Probando login: {usuario['nombre']}")
        print(f"   Email: {usuario['email']}")
        
        try:
            login_data = {
                "email": usuario["email"],
                "password": usuario["password"]
            }
            
            response = requests.post(
                "http://127.0.0.1:8000/api/auth/login/",
                json=login_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            print(f"   📊 Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Login exitoso!")
                print(f"   🔑 Token obtenido: {data.get('access_token', '')[:50]}...")
                
                # Probar una API autenticada
                probar_api_dashboard(data.get('access_token'))
                break  # Salir después del primer login exitoso
                
            elif response.status_code == 401:
                print("   ❌ Credenciales incorrectas")
                print(f"   📄 Respuesta: {response.text}")
            elif response.status_code == 400:
                print("   ⚠️ Error en datos enviados")
                print(f"   📄 Respuesta: {response.text}")
            else:
                print(f"   ❓ Respuesta inesperada: {response.status_code}")
                print(f"   📄 Respuesta: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("   ❌ Error de conexión")
        except Exception as e:
            print(f"   💥 Error: {e}")

def probar_api_dashboard(access_token):
    """Probar la API del dashboard con token válido"""
    print("\n📊 Probando API de Dashboard...")
    
    try:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(
            "http://127.0.0.1:8000/api/dashboard/",
            headers=headers,
            timeout=10
        )
        
        print(f"   📊 Status Dashboard: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("   ✅ Dashboard API funciona correctamente")
            print(f"   📋 Datos recibidos: {json.dumps(data, indent=2)[:200]}...")
        else:
            print(f"   ❌ Error en Dashboard: {response.status_code}")
            print(f"   📄 Respuesta: {response.text}")
            
    except Exception as e:
        print(f"   💥 Error en Dashboard: {e}")

def probar_urls_disponibles():
    """Probar diferentes URLs del proyecto"""
    imprimir_separador("PRUEBA DE URLs DISPONIBLES")
    
    urls_prueba = [
        ("/admin/", "Panel de Administración"),
        ("/api/", "API Root"),
        ("/api/auth/", "API Auth"),
        ("/api/dashboard/", "API Dashboard (sin auth)"),
    ]
    
    for url, descripcion in urls_prueba:
        print(f"\n🌐 Probando {descripcion}: {url}")
        try:
            response = requests.get(f"http://127.0.0.1:8000{url}", timeout=5)
            print(f"   📊 Status: {response.status_code}")
            
            if response.status_code in [200, 301, 302]:
                print("   ✅ URL accesible")
            elif response.status_code == 401:
                print("   🔐 Requiere autenticación (normal)")
            elif response.status_code == 403:
                print("   🚫 Acceso prohibido (normal)")
            elif response.status_code == 404:
                print("   ❌ URL no encontrada")
            else:
                print(f"   ❓ Respuesta: {response.status_code}")
                
        except Exception as e:
            print(f"   💥 Error: {e}")

def verificar_configuracion_cors():
    """Verificar configuración CORS"""
    imprimir_separador("VERIFICACIÓN DE CORS")
    
    try:
        print("🔍 Verificando headers CORS...")
        response = requests.options(
            "http://127.0.0.1:8000/api/auth/login/",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST"
            },
            timeout=5
        )
        
        print(f"📊 Status OPTIONS: {response.status_code}")
        
        cors_headers = [
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Methods", 
            "Access-Control-Allow-Headers"
        ]
        
        for header in cors_headers:
            value = response.headers.get(header)
            if value:
                print(f"✅ {header}: {value}")
            else:
                print(f"❌ {header}: No configurado")
                
    except Exception as e:
        print(f"💥 Error verificando CORS: {e}")

def main():
    """Función principal"""
    print("🏠 SMART CONDOMINIO - TEST DE APIs")
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ejecutar todas las pruebas
    if probar_conexion_basica():
        probar_api_login()
        probar_urls_disponibles()
        verificar_configuracion_cors()
    
    imprimir_separador("RESUMEN FINAL")
    print("🎯 Pruebas completadas")
    print("📱 Si el login funciona, la app móvil debería conectar correctamente")
    print("🔧 Si hay errores, revisa la configuración del servidor Django")

if __name__ == "__main__":
    main()