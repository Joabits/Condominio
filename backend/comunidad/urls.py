from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import api_home, home_view

# Router para ViewSets de DRF
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'unidades', views.UnidadViewSet)
router.register(r'areas-comunes', views.AreaComunViewSet)
router.register(r'camaras', views.CamaraSeguridadViewSet)
router.register(r'alertas', views.AlertaSeguridadViewSet)
router.register(r'pagos', views.PagoViewSet)
router.register(r'reservas', views.ReservaAreaComunViewSet)
router.register(r'visitantes', views.VisitanteViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),
    
    # =====================================
    # PÁGINA DE INICIO
    # =====================================
    path('', home_view, name='home'),  # Vista HTML de bienvenida
    path('api/', api_home, name='api-home'),  # Vista JSON de la API
    
    # =====================================
    # AUTENTICACIÓN
    # =====================================
    path('api/auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('api/auth/registro/', views.RegistroAPIView.as_view(), name='registro'),
    
    # =====================================
    # DASHBOARD MÓVIL
    # =====================================
    path('api/dashboard/', views.DashboardMovilAPIView.as_view(), name='dashboard-movil'),
    path('api/quick-actions/', views.QuickActionsAPIView.as_view(), name='quick-actions'),
    
    # =====================================
    # GESTIÓN FINANCIERA
    # =====================================
    path('api/finanzas/', views.FinanzasAPIView.as_view(), name='finanzas'),
    path('api/finanzas/pagar/', views.ProcesarPagoAPIView.as_view(), name='procesar-pago'),
    
    # =====================================
    # ÁREAS COMUNES Y RESERVAS
    # =====================================
    path('api/areas/', views.AreasAPIView.as_view(), name='areas'),
    path('api/areas/reservar/', views.CrearReservaAPIView.as_view(), name='crear-reserva'),
    
    # =====================================
    # NOTIFICACIONES
    # =====================================
    path('api/notificaciones/', views.NotificacionesAPIView.as_view(), name='notificaciones'),
    
    # =====================================
    # PERFIL DE USUARIO
    # =====================================
    path('api/perfil/', views.PerfilAPIView.as_view(), name='perfil'),
    
    # =====================================
    # ESTADÍSTICAS (PARA FRONTEND WEB)
    # =====================================
    path('api/estadisticas/', views.EstadisticasAPIView.as_view(), name='estadisticas'),
    
    # =====================================
    # URLS PARA FUTURAS IMPLEMENTACIONES
    # =====================================
    # path('api/ia/reconocimiento-facial/', views.ReconocimientoFacialView.as_view()),
    # path('api/ia/deteccion-vehiculos/', views.DeteccionVehiculosView.as_view()),
    # path('api/ia/prediccion-morosidad/', views.PrediccionMorosidadView.as_view()),
    # path('api/reportes/financiero/', views.ReporteFinancieroView.as_view()),
    # path('api/reportes/seguridad/', views.ReporteSeguridadView.as_view()),
    # path('api/incidentes/', views.IncidentesAPIView.as_view()),
    # path('api/mensajes/', views.MensajesAPIView.as_view()),
]