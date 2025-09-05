from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_home(request):
    """Vista de bienvenida para la API"""
    api_info = {
        'nombre': 'Smart Condominio API',
        'version': '1.0.0',
        'descripcion': 'API REST para la gestión inteligente de condominios',
        'estado': 'Activo',
        'endpoints': {
            'autenticacion': {
                'login': '/api/auth/login/',
                'logout': '/api/auth/logout/',
                'registro': '/api/auth/registro/',
                'token': '/api/token/',
                'refresh_token': '/api/token/refresh/',
            },
            'dashboard': {
                'dashboard_movil': '/api/dashboard/',
                'quick_actions': '/api/quick-actions/',
            },
            'finanzas': {
                'consultar': '/api/finanzas/',
                'pagar': '/api/finanzas/pagar/',
            },
            'areas_comunes': {
                'listar': '/api/areas/',
                'reservar': '/api/areas/reservar/',
            },
            'notificaciones': {
                'obtener': '/api/notificaciones/',
            },
            'perfil': {
                'consultar': '/api/perfil/',
                'actualizar': '/api/perfil/ (PUT)',
            },
            'admin': {
                'panel': '/admin/',
            }
        },
        'credenciales_demo': {
            'email': 'demo@condominio.com',
            'password': '123456'
        },
        'documentacion': {
            'admin_panel': 'http://localhost:8000/admin/',
            'api_auth': 'http://localhost:8000/api-auth/',
        }
    }
    
    return Response(api_info)


def home_view(request):
    """Vista HTML de bienvenida"""
    context = {
        'title': 'Smart Condominio - Backend API',
        'version': '1.0.0',
    }
    return render(request, 'home.html', context)