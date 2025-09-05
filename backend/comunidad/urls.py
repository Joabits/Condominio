from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router para ViewSets de DRF
router = DefaultRouter()
# router.register(r'condominios', views.CondominioViewSet)
# router.register(r'unidades', views.UnidadViewSet)
# router.register(r'usuarios', views.PerfilUsuarioViewSet)
# Más ViewSets se agregarán aquí

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),
    
    # URLs específicas
    # path('api/auth/', include('rest_framework.urls')),
    # path('api/login/', views.LoginView.as_view(), name='login'),
    # path('api/logout/', views.LogoutView.as_view(), name='logout'),
    
    # URLs para IA
    # path('api/ia/reconocimiento-facial/', views.ReconocimientoFacialView.as_view()),
    # path('api/ia/deteccion-vehiculos/', views.DeteccionVehiculosView.as_view()),
    # path('api/ia/prediccion-morosidad/', views.PrediccionMorosidadView.as_view()),
    
    # URLs para notificaciones push
    # path('api/notificaciones/', views.NotificacionesView.as_view()),
    
    # URLs para reportes
    # path('api/reportes/financiero/', views.ReporteFinancieroView.as_view()),
    # path('api/reportes/seguridad/', views.ReporteSeguridadView.as_view()),
]