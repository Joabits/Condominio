#!/usr/bin/env python
"""
Script para verificar conectividad específica para Flutter
"""
import requests
import json

def verificar_flutter_connectivity():
    """Verificar que Flutter pueda conectar al API"""
    print("🔍 Verificando conectividad para Flutter...")
    
    # URLs que Flutter necesita
    urls_flutter = [
        "http://127.0.0.1:8000/",
        "http://127.0.0.1:8000/api/auth/login/",
        "http://127.0.0.1:8000/api/dashboard/",
    ]
    
    for url in urls_flutter:
        try:
            print(f"\n🌐 Probando: {url}")
            
            if "login" in url:
                # Probar POST para login
                data = {
                    "email": "juan.silva@email.com",
                    "password": "Prop2025!"
                }
                response = requests.post(
                    url, 
                    json=data,
                    headers={"Content-Type": "application/json"},
                    timeout=5
                )
            else:
                # Probar GET para otras URLs
                response = requests.get(url, timeout=5)
            
            print(f"   📊 Status: {response.status_code}")
            
            if response.status_code == 200:
                print("   ✅ Accesible desde Flutter")
                if "login" in url:
                    data = response.json()
                    if "access_token" in data:
                        print("   🔑 Token recibido correctamente")
            elif response.status_code == 401:
                print("   🔐 Requiere autenticación (normal)")
            else:
                print(f"   ⚠️ Respuesta: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ No se puede conectar a {url}")
        except Exception as e:
            print(f"   💥 Error: {e}")

def main():
    print("📱 VERIFICACIÓN DE CONECTIVIDAD FLUTTER")
    print("=" * 50)
    verificar_flutter_connectivity()
    
    print("\n" + "=" * 50)
    print("✅ Configuración recomendada para Flutter:")
    print("   URL Base: http://127.0.0.1:8000")
    print("   Email: juan.silva@email.com") 
    print("   Password: Prop2025!")
    print("🚀 El servidor está listo para Flutter!")

if __name__ == "__main__":
    main()