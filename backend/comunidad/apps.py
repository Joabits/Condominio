from django.apps import AppConfig


class ComunidadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comunidad'
    verbose_name = 'Smart Condominium - Gestión de Comunidad'
    
    def ready(self):
        import comunidad.signals
