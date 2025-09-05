from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from comunidad.models import TipoUsuario, PerfilUsuario, Condominio


class Command(BaseCommand):
    help = 'Crea datos iniciales para el sistema Smart Condominium'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando configuración inicial del Smart Condominium...')
        
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@smartcondominio.com',
                password='admin123',
                first_name='Administrador',
                last_name='Sistema'
            )
            self.stdout.write(
                self.style.SUCCESS('✓ Superusuario creado: admin / admin123')
            )
        else:
            admin_user = User.objects.get(username='admin')
            self.stdout.write('✓ Superusuario ya existe')

        # Crear tipos de usuario
        tipos_usuario = [
            ('ADMINISTRADOR', 'Administrador del Condominio'),
            ('PROPIETARIO', 'Propietario de Unidad'),
            ('INQUILINO', 'Inquilino de Unidad'),
            ('SEGURIDAD', 'Personal de Seguridad'),
            ('MANTENIMIENTO', 'Personal de Mantenimiento'),
            ('VISITANTE', 'Visitante'),
        ]
        
        for tipo, descripcion in tipos_usuario:
            obj, created = TipoUsuario.objects.get_or_create(
                tipo=tipo,
                defaults={'descripcion': descripcion}
            )
            if created:
                self.stdout.write(f'✓ Tipo de usuario creado: {tipo}')

        # Crear condominio de ejemplo
        if not Condominio.objects.exists():
            condominio = Condominio.objects.create(
                nombre='Condominio Los Jardines',
                direccion='Av. Principal 123, Zona Norte',
                telefono='591-3-1234567',
                email='admin@losjardines.com',
                nit='123456789',
                ciudad='Santa Cruz',
                pais='Bolivia'
            )
            self.stdout.write(
                self.style.SUCCESS('✓ Condominio de ejemplo creado')
            )

            # Crear perfil para el admin
            tipo_admin = TipoUsuario.objects.get(tipo='ADMINISTRADOR')
            PerfilUsuario.objects.create(
                user=admin_user,
                condominio=condominio,
                tipo_usuario=tipo_admin,
                ci='12345678',
                telefono='591-3-1234567'
            )
            self.stdout.write('✓ Perfil de administrador creado')
        
        self.stdout.write(
            self.style.SUCCESS('\n🎉 Configuración inicial completada!')
        )
        self.stdout.write('Puedes acceder al admin en: http://localhost:8000/admin/')
        self.stdout.write('Usuario: admin')
        self.stdout.write('Contraseña: admin123')