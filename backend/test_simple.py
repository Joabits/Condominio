# 🧪 Prueba Simple de API - Smart Condominio

import requests
import sys

def test_simple():
    """Prueba simple de conectividad"""
    try:
        print("🔍 Probando conexión básica...")
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"✅ Conexión exitosa - Status: {response.status_code}")
        print(f"📄 Título de la página: {response.text[:100]}...")
        
        print("\n🔐 Probando API de login...")
        login_data = {
            "email": "demo@condominio.com",
            "password": "123456"
        }
        
        response = requests.post(
            "http://127.0.0.1:8000/api/auth/login/",
            json=login_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"📊 Status de login: {response.status_code}")
        print(f"📋 Respuesta: {response.text}")
        
        if response.status_code == 200:
            print("🎉 ¡API de login funciona correctamente!")
        else:
            print("⚠️  La API de login tiene problemas")
            
    except requests.exceptions.ConnectinError as e:
        print(f"❌ Error de conexión: {e}")
    except requests.exceptions.Timeout as e:
        print(f"⏰ Timeout: {e}")
    except Exception as e:
        print(f"💥 Error inesperado: {e}")

if __name__ == "__main__":
    test_simple()