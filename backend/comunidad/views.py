from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db.models import Q, Sum, Count
from django.utils import timezone
from datetime import date, timedelta, datetime
import uuid

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *


# =====================================
# AUTENTICACIÓN
# =====================================

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generar tokens JWT
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            
            # Obtener perfil del usuario
            try:
                perfil = PerfilUsuario.objects.get(user=user)
                perfil_data = PerfilUsuarioSerializer(perfil).data
            except PerfilUsuario.DoesNotExist:
                return Response({
                    'error': 'Perfil de usuario no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Actualizar último acceso
            perfil.ultimo_acceso = timezone.now()
            perfil.save()
            
            return Response({
                'access_token': str(access_token),
                'refresh_token': str(refresh),
                'user': perfil_data,
                'message': 'Inicio de sesión exitoso'
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({
                'message': 'Sesión cerrada exitosamente'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'error': 'Token inválido'
            }, status=status.HTTP_400_BAD_REQUEST)


class RegistroAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Crear usuario
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            
            # Crear perfil
            # Por defecto, asignar al primer condominio y como propietario
            condominio = Condominio.objects.first()
            tipo_usuario = TipoUsuario.objects.get(tipo='PROPIETARIO')
            
            perfil = PerfilUsuario.objects.create(
                user=user,
                condominio=condominio,
                tipo_usuario=tipo_usuario,
                ci=data['ci'],
                telefono=data.get('telefono', '')
            )
            
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================
# DASHBOARD MÓVIL
# =====================================

class DashboardMovilAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            
            # Unidad principal del usuario
            residencia_principal = ResidenciaUnidad.objects.filter(
                usuario=perfil, 
                activa=True
            ).first()
            
            # Cuota pendiente más próxima
            cuota_pendiente = None
            if residencia_principal:
                cuota_pendiente = CuotaMantenimiento.objects.filter(
                    unidad=residencia_principal.unidad,
                    estado__in=['PENDIENTE', 'VENCIDA']
                ).order_by('fecha_vencimiento').first()
            
            # Reservas activas
            reservas_activas = ReservaAreaComun.objects.filter(
                usuario=perfil,
                estado='CONFIRMADA',
                fecha_reserva__gte=date.today()
            ).order_by('fecha_reserva')[:3]
            
            # Alertas recientes
            alertas_recientes = AlertaSeguridad.objects.filter(
                condominio=perfil.condominio,
                revisada=False
            ).order_by('-fecha_hora')[:5]
            
            # Accesos recientes del usuario
            accesos_recientes = RegistroAcceso.objects.filter(
                usuario=perfil
            ).order_by('-fecha_hora')[:5]
            
            # Calcular balance total
            balance_total = 0
            if residencia_principal:
                cuotas_pendientes = CuotaMantenimiento.objects.filter(
                    unidad=residencia_principal.unidad,
                    estado__in=['PENDIENTE', 'VENCIDA']
                )
                balance_total = cuotas_pendientes.aggregate(
                    total=Sum('monto_pendiente')
                )['total'] or 0
            
            # Próximos vencimientos
            proximos_vencimientos = []
            if residencia_principal:
                cuotas_proximas = CuotaMantenimiento.objects.filter(
                    unidad=residencia_principal.unidad,
                    estado='PENDIENTE',
                    fecha_vencimiento__lte=date.today() + timedelta(days=30)
                ).order_by('fecha_vencimiento')[:3]
                
                for cuota in cuotas_proximas:
                    dias_restantes = (cuota.fecha_vencimiento - date.today()).days
                    proximos_vencimientos.append({
                        'id': str(cuota.id),
                        'descripcion': f"Cuota {cuota.configuracion.periodo_mes}/{cuota.configuracion.periodo_año}",
                        'monto': cuota.monto_total,
                        'fecha_vencimiento': cuota.fecha_vencimiento,
                        'dias_restantes': dias_restantes
                    })
            
            dashboard_data = {
                'usuario': PerfilUsuarioSerializer(perfil).data,
                'unidad_principal': UnidadSerializer(residencia_principal.unidad).data if residencia_principal else None,
                'cuota_pendiente': CuotaMantenimientoSerializer(cuota_pendiente).data if cuota_pendiente else None,
                'reservas_activas': ReservaAreaComunSerializer(reservas_activas, many=True).data,
                'alertas_recientes': AlertaSeguridadSerializer(alertas_recientes, many=True).data,
                'accesos_recientes': RegistroAccesoSerializer(accesos_recientes, many=True).data,
                'balance_total': balance_total,
                'proximos_vencimientos': proximos_vencimientos
            }
            
            return Response(dashboard_data, status=status.HTTP_200_OK)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# =====================================
# GESTIÓN FINANCIERA
# =====================================

class FinanzasAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            residencia = ResidenciaUnidad.objects.filter(
                usuario=perfil, 
                activa=True
            ).first()
            
            if not residencia:
                return Response({
                    'error': 'No se encontró unidad asociada'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Estadísticas financieras
            cuotas_pendientes = CuotaMantenimiento.objects.filter(
                unidad=residencia.unidad,
                estado__in=['PENDIENTE', 'VENCIDA']
            )
            
            cuotas_pagadas = CuotaMantenimiento.objects.filter(
                unidad=residencia.unidad,
                estado='PAGADA'
            )
            
            saldo_actual = cuotas_pendientes.aggregate(
                total=Sum('monto_pendiente')
            )['total'] or 0
            
            total_pagado_año = cuotas_pagadas.filter(
                configuracion__periodo_año=date.today().year
            ).aggregate(
                total=Sum('monto_pagado')
            )['total'] or 0
            
            # Próxima cuota
            proxima_cuota = cuotas_pendientes.order_by('fecha_vencimiento').first()
            
            # Historial de pagos recientes
            pagos_recientes = Pago.objects.filter(
                cuota__unidad=residencia.unidad,
                estado='COMPLETADO'
            ).order_by('-fecha_pago')[:10]
            
            # Métodos de pago disponibles
            metodos_pago = MetodoPago.objects.filter(
                condominio=perfil.condominio,
                activo=True
            )
            
            datos_financieros = {
                'saldo_actual': saldo_actual,
                'cuotas_pendientes': cuotas_pendientes.count(),
                'total_pendiente': saldo_actual,
                'pagos_realizados_mes': cuotas_pagadas.filter(
                    fecha_ultimo_pago__month=date.today().month,
                    fecha_ultimo_pago__year=date.today().year
                ).count(),
                'total_pagado_año': total_pagado_año,
                'proxima_cuota': CuotaMantenimientoSerializer(proxima_cuota).data if proxima_cuota else None,
                'historial_pagos': PagoSerializer(pagos_recientes, many=True).data,
                'metodos_pago': MetodoPagoSerializer(metodos_pago, many=True).data,
                'cuotas_pendientes_detalle': CuotaMantenimientoSerializer(cuotas_pendientes, many=True).data
            }
            
            return Response(datos_financieros, status=status.HTTP_200_OK)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


class ProcesarPagoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CrearPagoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                perfil = PerfilUsuario.objects.get(user=request.user)
                data = serializer.validated_data
                
                cuota = get_object_or_404(CuotaMantenimiento, id=data['cuota_id'])
                metodo_pago = get_object_or_404(MetodoPago, id=data['metodo_pago_id'])
                
                # Crear el pago
                pago = Pago.objects.create(
                    cuota=cuota,
                    metodo_pago=metodo_pago,
                    monto_pagado=data['monto_pagado'],
                    numero_transaccion=str(uuid.uuid4()),
                    numero_comprobante=data.get('numero_comprobante', ''),
                    comprobante_imagen=data.get('comprobante_imagen'),
                    fecha_pago=timezone.now(),
                    estado='COMPLETADO',  # En producción, sería 'PENDIENTE' para verificación
                    registrado_por=perfil,
                    observaciones=data.get('observaciones', '')
                )
                
                # Actualizar la cuota
                cuota.monto_pagado += data['monto_pagado']
                cuota.fecha_ultimo_pago = timezone.now()
                cuota.save()  # El save() actualiza automáticamente el estado
                
                return Response({
                    'message': 'Pago procesado exitosamente',
                    'pago': PagoSerializer(pago).data
                }, status=status.HTTP_201_CREATED)
                
            except PerfilUsuario.DoesNotExist:
                return Response({
                    'error': 'Perfil de usuario no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================
# ÁREAS COMUNES Y RESERVAS
# =====================================

class AreasAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            
            # Áreas comunes disponibles
            areas_comunes = AreaComun.objects.filter(
                condominio=perfil.condominio,
                activa=True
            )
            
            # Reservas del usuario
            reservas_usuario = ReservaAreaComun.objects.filter(
                usuario=perfil
            ).order_by('-fecha_reserva')[:10]
            
            return Response({
                'areas_comunes': AreaComunSerializer(areas_comunes, many=True).data,
                'mis_reservas': ReservaAreaComunSerializer(reservas_usuario, many=True).data
            }, status=status.HTTP_200_OK)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


class CrearReservaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CrearReservaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                perfil = PerfilUsuario.objects.get(user=request.user)
                data = serializer.validated_data
                
                area_comun = get_object_or_404(AreaComun, id=data['area_comun_id'])
                
                # Verificar disponibilidad
                reservas_existentes = ReservaAreaComun.objects.filter(
                    area_comun=area_comun,
                    fecha_reserva=data['fecha_reserva'],
                    estado__in=['PENDIENTE', 'CONFIRMADA'],
                    hora_inicio__lt=data['hora_fin'],
                    hora_fin__gt=data['hora_inicio']
                )
                
                if reservas_existentes.exists():
                    return Response({
                        'error': 'El área no está disponible en ese horario'
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                # Calcular costo
                horas = (datetime.combine(date.today(), data['hora_fin']) - 
                        datetime.combine(date.today(), data['hora_inicio'])).seconds / 3600
                monto_total = area_comun.precio_por_hora * horas
                
                # Crear reserva
                reserva = ReservaAreaComun.objects.create(
                    area_comun=area_comun,
                    usuario=perfil,
                    fecha_reserva=data['fecha_reserva'],
                    hora_inicio=data['hora_inicio'],
                    hora_fin=data['hora_fin'],
                    numero_personas=data['numero_personas'],
                    proposito=data['proposito'],
                    observaciones=data.get('observaciones', ''),
                    estado='CONFIRMADA',
                    monto_total=monto_total
                )
                
                return Response({
                    'message': 'Reserva creada exitosamente',
                    'reserva': ReservaAreaComunSerializer(reserva).data
                }, status=status.HTTP_201_CREATED)
                
            except PerfilUsuario.DoesNotExist:
                return Response({
                    'error': 'Perfil de usuario no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================
# NOTIFICACIONES
# =====================================

class NotificacionesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            
            # Avisos administrativos (simulados)
            avisos = [
                {
                    'id': str(uuid.uuid4()),
                    'tipo': 'AVISO',
                    'titulo': 'Corte de agua programado',
                    'mensaje': 'Se realizará mantenimiento del sistema de agua el próximo martes de 8:00 AM a 12:00 PM.',
                    'fecha': timezone.now() - timedelta(hours=2),
                    'leida': False,
                    'prioridad': 'MEDIA'
                },
                {
                    'id': str(uuid.uuid4()),
                    'tipo': 'AVISO',
                    'titulo': 'Asamblea General Ordinaria',
                    'mensaje': 'Se convoca a todos los propietarios a la asamblea que se realizará el 15 de diciembre a las 19:00 horas.',
                    'fecha': timezone.now() - timedelta(days=1),
                    'leida': True,
                    'prioridad': 'ALTA'
                }
            ]
            
            # Alertas de seguridad reales
            alertas_seguridad = AlertaSeguridad.objects.filter(
                condominio=perfil.condominio
            ).order_by('-fecha_hora')[:10]
            
            alertas = []
            for alerta in alertas_seguridad:
                alertas.append({
                    'id': str(alerta.id),
                    'tipo': 'ALERTA',
                    'titulo': alerta.get_tipo_alerta_display(),
                    'mensaje': alerta.descripcion,
                    'fecha': alerta.fecha_hora,
                    'leida': alerta.revisada,
                    'prioridad': alerta.nivel
                })
            
            # Emergencias (simuladas)
            emergencias = [
                {
                    'id': str(uuid.uuid4()),
                    'tipo': 'EMERGENCIA',
                    'titulo': 'Falla en el ascensor principal',
                    'mensaje': 'El ascensor principal está fuera de servicio. Se recomienda usar las escaleras.',
                    'fecha': timezone.now() - timedelta(minutes=30),
                    'leida': False,
                    'prioridad': 'CRITICA'
                }
            ]
            
            # Notificaciones de pagos
            pagos = []
            residencia = ResidenciaUnidad.objects.filter(
                usuario=perfil, 
                activa=True
            ).first()
            
            if residencia:
                cuotas_vencen_pronto = CuotaMantenimiento.objects.filter(
                    unidad=residencia.unidad,
                    estado='PENDIENTE',
                    fecha_vencimiento__lte=date.today() + timedelta(days=7)
                )
                
                for cuota in cuotas_vencen_pronto:
                    days_until = (cuota.fecha_vencimiento - date.today()).days
                    pagos.append({
                        'id': str(cuota.id),
                        'tipo': 'PAGO',
                        'titulo': f'Cuota próxima a vencer',
                        'mensaje': f'Su cuota vence en {days_until} días. Monto: ${cuota.monto_total}',
                        'fecha': timezone.now(),
                        'leida': False,
                        'prioridad': 'ALTA' if days_until <= 3 else 'MEDIA'
                    })
            
            return Response({
                'avisos': avisos,
                'alertas': alertas,
                'emergencias': emergencias,
                'pagos': pagos
            }, status=status.HTTP_200_OK)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# =====================================
# PERFIL DE USUARIO
# =====================================

class PerfilAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            
            # Información adicional
            vehiculos = Vehiculo.objects.filter(propietario=perfil, activo=True)
            residencias = ResidenciaUnidad.objects.filter(usuario=perfil, activa=True)
            
            return Response({
                'perfil': PerfilUsuarioSerializer(perfil).data,
                'vehiculos': VehiculoSerializer(vehiculos, many=True).data,
                'residencias': ResidenciaUnidadSerializer(residencias, many=True).data
            }, status=status.HTTP_200_OK)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            serializer = ActualizarPerfilSerializer(data=request.data)
            
            if serializer.is_valid():
                data = serializer.validated_data
                
                # Actualizar usuario
                if 'first_name' in data:
                    perfil.user.first_name = data['first_name']
                if 'last_name' in data:
                    perfil.user.last_name = data['last_name']
                perfil.user.save()
                
                # Actualizar perfil
                if 'telefono' in data:
                    perfil.telefono = data['telefono']
                if 'telefono_emergencia' in data:
                    perfil.telefono_emergencia = data['telefono_emergencia']
                if 'foto_perfil' in data:
                    perfil.foto_perfil = data['foto_perfil']
                
                perfil.save()
                
                return Response({
                    'message': 'Perfil actualizado exitosamente',
                    'perfil': PerfilUsuarioSerializer(perfil).data
                }, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except PerfilUsuario.DoesNotExist:
            return Response({
                'error': 'Perfil de usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# =====================================
# QUICK ACTIONS
# =====================================

class QuickActionsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        actions = [
            {
                'id': 'pagar_cuota',
                'titulo': 'Pagar Cuota',
                'descripcion': 'Realizar pago de cuota mensual',
                'icono': 'payment',
                'color': '#4CAF50',
                'disponible': True,
                'url': '/api/finanzas/'
            },
            {
                'id': 'reservar_area',
                'titulo': 'Reservar Área',
                'descripcion': 'Reservar área común',
                'icono': 'event',
                'color': '#2196F3',
                'disponible': True,
                'url': '/api/areas/'
            },
            {
                'id': 'reportar_incidente',
                'titulo': 'Reportar Incidente',
                'descripcion': 'Reportar problema o incidente',
                'icono': 'report_problem',
                'color': '#FF9800',
                'disponible': True,
                'url': '/api/incidentes/'
            },
            {
                'id': 'contactar_admin',
                'titulo': 'Contactar Admin',
                'descripcion': 'Enviar mensaje a administración',
                'icono': 'message',
                'color': '#9C27B0',
                'disponible': True,
                'url': '/api/mensajes/'
            }
        ]
        
        return Response(actions, status=status.HTTP_200_OK)


# =====================================
# VIEWSETS PARA FRONTEND WEB
# =====================================

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = PerfilUsuario.objects.select_related('user', 'condominio', 'tipo_usuario').all()
        return queryset

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [IsAuthenticated]

class AreaComunViewSet(viewsets.ModelViewSet):
    queryset = AreaComun.objects.all()
    serializer_class = AreaComunSerializer
    permission_classes = [IsAuthenticated]

class CamaraSeguridadViewSet(viewsets.ModelViewSet):
    queryset = CamaraSeguridad.objects.all()
    serializer_class = CamaraSeguridadSerializer
    permission_classes = [IsAuthenticated]

class AlertaSeguridadViewSet(viewsets.ModelViewSet):
    queryset = AlertaSeguridad.objects.all()
    serializer_class = AlertaSeguridadSerializer
    permission_classes = [IsAuthenticated]

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]

class ReservaAreaComunViewSet(viewsets.ModelViewSet):
    queryset = ReservaAreaComun.objects.all()
    serializer_class = ReservaAreaComunSerializer
    permission_classes = [IsAuthenticated]

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

# =====================================
# API PARA ESTADÍSTICAS
# =====================================

class EstadisticasAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Estadísticas de residentes
        total_residentes = PerfilUsuario.objects.count()
        residentes_activos = PerfilUsuario.objects.filter(activo=True).count()
        
        # Estadísticas de unidades
        total_unidades = Unidad.objects.count()
        unidades_ocupadas = Unidad.objects.filter(activa=True).count()
        
        # Estadísticas de pagos
        pagos_mes_actual = Pago.objects.filter(
            fecha_pago__month=timezone.now().month,
            fecha_pago__year=timezone.now().year
        ).count()
        
        total_ingresos_mes = Pago.objects.filter(
            fecha_pago__month=timezone.now().month,
            fecha_pago__year=timezone.now().year
        ).aggregate(total=Sum('monto'))['total'] or 0
        
        # Estadísticas de seguridad
        alertas_mes = AlertaSeguridad.objects.filter(
            fecha_hora__month=timezone.now().month,
            fecha_hora__year=timezone.now().year
        ).count()
        
        # Estadísticas de mantenimiento
        solicitudes_abiertas = 0  # Sin modelo de SolicitudMantenimiento por ahora
        
        return Response({
            'residentes': {
                'total': total_residentes,
                'activos': residentes_activos,
                'nuevos_mes': 0,  # Calcular nuevos del mes si es necesario
                'tasa_ocupacion': (unidades_ocupadas / total_unidades * 100) if total_unidades > 0 else 0
            },
            'unidades': {
                'total': total_unidades,
                'ocupadas': unidades_ocupadas,
                'disponibles': total_unidades - unidades_ocupadas
            },
            'finanzas': {
                'pagos_mes': pagos_mes_actual,
                'ingresos_mes': float(total_ingresos_mes),
                'morosidad': 0  # Calcular si es necesario
            },
            'seguridad': {
                'alertas_mes': alertas_mes,
                'camaras_activas': CamaraSeguridad.objects.filter(activa=True).count()
            },
            'mantenimiento': {
                'solicitudes_abiertas': solicitudes_abiertas
            }
        }, status=status.HTTP_200_OK)
