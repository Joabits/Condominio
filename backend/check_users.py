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
from comunidad.models import PerfilUsuario

print('=== USUARIOS DISPONIBLES PARA LOGIN ===')
users = User.objects.all()
for user in users:
    try:
        perfil = PerfilUsuario.objects.get(user=user)
        print(f'Email: {user.email}')
        print(f'Nombre: {user.first_name} {user.last_name}')
        print(f'Tipo: {perfil.tipo_usuario.tipo}')
        print(f'Activo: {perfil.activo}')
        print(f'Contraseña: Prop2025!')
        print('---')
    except PerfilUsuario.DoesNotExist:
        print(f'Usuario sin perfil: {user.email}')
        print('---')

print('\n=== CREDENCIALES RECOMENDADAS PARA MOBILE APP ===')
print('Email: juan.silva@email.com')
print('Contraseña: Prop2025!')
print('Tipo: PROPIETARIO')
print('\nEmail: ana.rodriguez@email.com')
print('Contraseña: Prop2025!')
print('Tipo: PROPIETARIO')