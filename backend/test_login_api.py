#!/usr/bin/env python
import os
import sys
import django
import requests
import json

# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Test the login API
def test_login_api():
    url = 'http://127.0.0.1:8000/api/auth/login/'
    
    # Test data
    test_credentials = {
        'email': 'juan.silva@email.com',
        'password': 'Prop2025!'
    }
    
    print("=== TESTING LOGIN API ===")
    print(f"URL: {url}")
    print(f"Data: {test_credentials}")
    
    try:
        # Make the request
        response = requests.post(
            url,
            data=json.dumps(test_credentials),
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"Response Body: {json.dumps(response_data, indent=2)}")
        except:
            print(f"Response Text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: No se pudo conectar al servidor. ¿Está ejecutándose Django?")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    test_login_api()