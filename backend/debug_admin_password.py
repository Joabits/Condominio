#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print('=== DEBUGGING LOGIN ISSUES ===')

# Buscar el usuario administrador
admin_user = User.objects.get(email='admin@lastorres.com')
print(f'Usuario encontrado: {admin_user.username}')
print(f'Email: {admin_user.email}')
print(f'Activo: {admin_user.is_active}')
print(f'Password hash: {admin_user.password[:50]}...')

# Probar diferentes contraseñas
test_passwords = ['Prop2025!', 'Admin2025!', 'admin123', 'admin', '123456']

for password in test_passwords:
    auth_result = authenticate(username=admin_user.username, password=password)
    print(f'Password "{password}": {"✅ CORRECTO" if auth_result else "❌ INCORRECTO"}')

# Cambiar la contraseña a la esperada
print('\n=== RESETEANDO CONTRASEÑA ===')
admin_user.set_password('Prop2025!')
admin_user.save()
print('Contraseña cambiada a: Prop2025!')

# Verificar que funciona
auth_result = authenticate(username=admin_user.username, password='Prop2025!')
print(f'Verificación final: {"✅ FUNCIONA" if auth_result else "❌ SIGUE FALLANDO"}')