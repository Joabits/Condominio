# 🧪 Script de Pruebas de APIs - Smart Condominio

import requests
import json

# Configuración
BASE_URL = "http://127.0.0.1:8000"
DEMO_EMAIL = "demo@condominio.com"
DEMO_PASSWORD = "123456"

def test_api_connection():
    """Probar conexión básica al servidor"""
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Conexión al servidor exitosa")
            return True
        else:
            print(f"❌ Error de conexión: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ No se pudo conectar al servidor: {e}")
        return False

def test_login_api():
    """Probar API de login"""
    print("\n🔐 Probando API de Login...")
    
    login_data = {
        "email": DEMO_EMAIL,
        "password": DEMO_PASSWORD
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/auth/login/",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Login exitoso")
            print(f"   Token recibido: {data.get('access_token', 'N/A')[:20]}...")
            return data.get('access_token')
        else:
            print(f"❌ Error en login: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error en login: {e}")
        return None

def test_dashboard_api(token):
    """Probar API de dashboard"""
    print("\n📊 Probando API de Dashboard...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/dashboard/",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Dashboard API funcionando")
            print(f"   Usuario: {data.get('usuario', {}).get('user', {}).get('first_name', 'N/A')}")
            return True
        else:
            print(f"❌ Error en dashboard: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en dashboard: {e}")
        return False

def test_finanzas_api(token):
    """Probar API de finanzas"""
    print("\n💰 Probando API de Finanzas...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/finanzas/",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Finanzas API funcionando")
            print(f"   Saldo actual: ${data.get('saldo_actual', 'N/A')}")
            return True
        else:
            print(f"❌ Error en finanzas: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en finanzas: {e}")
        return False

def test_areas_api(token):
    """Probar API de áreas comunes"""
    print("\n🏊‍♂️ Probando API de Áreas Comunes...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/areas/",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Áreas API funcionando")
            areas_count = len(data.get('areas_comunes', []))
            print(f"   Áreas disponibles: {areas_count}")
            return True
        else:
            print(f"❌ Error en áreas: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en áreas: {e}")
        return False

def test_notificaciones_api(token):
    """Probar API de notificaciones"""
    print("\n🔔 Probando API de Notificaciones...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/notificaciones/",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Notificaciones API funcionando")
            avisos_count = len(data.get('avisos', []))
            print(f"   Avisos disponibles: {avisos_count}")
            return True
        else:
            print(f"❌ Error en notificaciones: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en notificaciones: {e}")
        return False

def test_perfil_api(token):
    """Probar API de perfil"""
    print("\n👤 Probando API de Perfil...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/perfil/",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Perfil API funcionando")
            user_name = data.get('perfil', {}).get('user', {}).get('first_name', 'N/A')
            print(f"   Usuario: {user_name}")
            return True
        else:
            print(f"❌ Error en perfil: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en perfil: {e}")
        return False

def main():
    """Ejecutar todas las pruebas"""
    print("🧪 INICIANDO PRUEBAS DE APIs - SMART CONDOMINIO")
    print("=" * 50)
    
    # Prueba de conexión básica
    if not test_api_connection():
        print("\n❌ No se puede conectar al servidor. Verifica que Django esté corriendo.")
        return
    
    # Prueba de login
    token = test_login_api()
    if not token:
        print("\n❌ No se pudo obtener token de autenticación.")
        return
    
    # Pruebas de APIs autenticadas
    results = []
    results.append(test_dashboard_api(token))
    results.append(test_finanzas_api(token))
    results.append(test_areas_api(token))
    results.append(test_notificaciones_api(token))
    results.append(test_perfil_api(token))
    
    # Resumen final
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    successful_tests = sum(results)
    total_tests = len(results) + 1  # +1 por el login
    
    print(f"✅ Pruebas exitosas: {successful_tests + 1}/{total_tests + 1}")
    
    if successful_tests == len(results):
        print("🎉 ¡TODAS LAS APIs ESTÁN FUNCIONANDO CORRECTAMENTE!")
        print("📱 La aplicación móvil puede conectarse sin problemas.")
    else:
        print("⚠️  Algunas APIs presentan problemas.")
    
    print("\n🔗 URLs importantes:")
    print(f"   🏠 Inicio: {BASE_URL}/")
    print(f"   🛠️  Admin: {BASE_URL}/admin/")
    print(f"   📊 Dashboard: {BASE_URL}/api/dashboard/")

if __name__ == "__main__":
    main()