# 🏢 Comando Django para poblar la base de datos - Smart Condominio

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from datetime import date
from decimal import Decimal

from comunidad.models import (
    Condominio, TipoUsuario, PerfilUsuario, TipoUnidad, Unidad,
    ResidenciaUnidad, AreaComun
)

class Command(BaseCommand):
    help = 'Poblar la base de datos con datos reales del condominio'

    def handle(self, *args, **options):
        self.stdout.write("🚀 INICIANDO POBLACIÓN DE BASE DE DATOS")
        self.stdout.write("=" * 60)
        
        try:
            with transaction.atomic():
                # Limpiar datos anteriores
                self.limpiar_datos()
                
                # Crear tipos base
                self.crear_tipos_base()
                
                # Crear condominio
                condominio = self.crear_condominio()
                
                # Crear administrador
                self.crear_administrador(condominio)
                
                # Crear propietarios
                propietarios = self.crear_propietarios(condominio)
                
                # Crear unidades
                unidades = self.crear_unidades(condominio)
                
                # Asignar residencias
                self.asignar_residencias(unidades, propietarios)
                
                # Crear áreas comunes
                areas = self.crear_areas_comunes(condominio)
                
                self.stdout.write("\\n" + "=" * 60)
                self.stdout.write(self.style.SUCCESS("🎉 ¡BASE DE DATOS POBLADA EXITOSAMENTE!"))
                self.stdout.write("📊 Resumen:")
                self.stdout.write(f"   🏢 Condominio: Residencial Las Torres")
                self.stdout.write(f"   🏠 Propietarios: {len(propietarios)}")
                self.stdout.write(f"   🏠 Unidades: {len(unidades)}")
                self.stdout.write(f"   🏊 Áreas comunes: {len(areas)}")
                
                self.stdout.write("\\n🔐 Credenciales principales:")
                self.stdout.write("   👨‍💼 Administrador:")
                self.stdout.write("     Username: admin_general")
                self.stdout.write("     Password: Admin2025!")
                self.stdout.write("   🏠 Propietario ejemplo:")
                self.stdout.write("     Username: prop_juan")
                self.stdout.write("     Password: Prop2025!")
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error: {e}"))
            raise

    def limpiar_datos(self):
        """Limpiar datos existentes"""
        self.stdout.write("🧹 Limpiando datos anteriores...")
        
        # Eliminar usuarios que no sean superusuarios
        User.objects.filter(is_superuser=False).delete()
        
        # Limpiar tablas principales (el cascade se encarga del resto)
        Condominio.objects.all().delete()
        TipoUsuario.objects.all().delete()
        TipoUnidad.objects.all().delete()
        
        self.stdout.write("✅ Datos anteriores eliminados")

    def crear_tipos_base(self):
        """Crear tipos base del sistema"""
        self.stdout.write("🔧 Creando tipos base...")
        
        # Tipos de usuario
        tipos_usuario = [
            ("ADMINISTRADOR", "Administrador del Condominio"),
            ("PROPIETARIO", "Propietario de Unidad"),
            ("INQUILINO", "Inquilino"),
            ("SEGURIDAD", "Personal de Seguridad"),
            ("MANTENIMIENTO", "Personal de Mantenimiento"),
            ("VISITANTE", "Visitante"),
        ]
        
        for tipo, desc in tipos_usuario:
            TipoUsuario.objects.get_or_create(
                tipo=tipo,
                defaults={"descripcion": desc}
            )
        
        # Tipos de unidad
        tipos_unidad = [
            ("Departamento 1 Dorm", "Departamento de 1 dormitorio", "0.8"),
            ("Departamento 2 Dorm", "Departamento de 2 dormitorios", "1.0"),
            ("Departamento 3 Dorm", "Departamento de 3 dormitorios", "1.3"),
            ("Penthouse", "Penthouse de lujo", "2.0"),
            ("Oficina", "Oficina comercial", "0.6"),
        ]
        
        for nombre, desc, factor in tipos_unidad:
            TipoUnidad.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "descripcion": desc,
                    "factor_costo": Decimal(factor)
                }
            )
        
        self.stdout.write("✅ Tipos base creados")

    def crear_condominio(self):
        """Crear condominio principal"""
        self.stdout.write("🏢 Creando condominio...")
        
        condominio = Condominio.objects.create(
            nombre="Residencial Las Torres",
            direccion="Av. Banzer Km 9, Entre 4to y 5to Anillo, Santa Cruz de la Sierra",
            telefono="+591 3 123-4567",
            email="administracion@lastorres.com",
            nit="1023456789012",
            codigo_postal="0000",
            ciudad="Santa Cruz de la Sierra",
            pais="Bolivia"
        )
        
        self.stdout.write(f"✅ Condominio creado: {condominio.nombre}")
        return condominio

    def crear_administrador(self, condominio):
        """Crear administrador principal"""
        self.stdout.write("👨‍💼 Creando administrador...")
        
        # Crear usuario admin
        admin_user = User.objects.create_user(
            username="admin_general",
            email="admin@lastorres.com",
            first_name="Carlos",
            last_name="Mendoza",
            password="Admin2025!"
        )
        
        # Crear perfil admin
        tipo_admin = TipoUsuario.objects.get(tipo="ADMINISTRADOR")
        PerfilUsuario.objects.create(
            user=admin_user,
            condominio=condominio,
            tipo_usuario=tipo_admin,
            ci="12345678",
            telefono="+591 70123456",
            fecha_nacimiento=date(1985, 5, 15)
        )
        
        self.stdout.write("✅ Administrador creado")
        return admin_user

    def crear_propietarios(self, condominio):
        """Crear propietarios"""
        self.stdout.write("🏠 Creando propietarios...")
        
        tipo_propietario = TipoUsuario.objects.get(tipo="PROPIETARIO")
        
        propietarios_data = [
            {
                "username": "prop_juan",
                "email": "juan.silva@email.com",
                "first_name": "Juan",
                "last_name": "Silva Torrez",
                "password": "Prop2025!",
                "ci": "98765432",
                "telefono": "+591 70111222",
                "fecha_nacimiento": date(1978, 4, 12)
            },
            {
                "username": "prop_ana",
                "email": "ana.martinez@email.com",
                "first_name": "Ana",
                "last_name": "Martínez Vega",
                "password": "Prop2025!",
                "ci": "13579246",
                "telefono": "+591 70222333",
                "fecha_nacimiento": date(1983, 9, 28)
            },
            {
                "username": "prop_miguel",
                "email": "miguel.lopez@email.com",
                "first_name": "Miguel",
                "last_name": "López Santos",
                "password": "Prop2025!",
                "ci": "24681357",
                "telefono": "+591 70333444",
                "fecha_nacimiento": date(1980, 12, 3)
            },
            {
                "username": "prop_lucia",
                "email": "lucia.garcia@email.com",
                "first_name": "Lucía",
                "last_name": "García Flores",
                "password": "Prop2025!",
                "ci": "97531864",
                "telefono": "+591 70444555",
                "fecha_nacimiento": date(1985, 2, 17)
            },
            {
                "username": "prop_ricardo",
                "email": "ricardo.perez@email.com",
                "first_name": "Ricardo",
                "last_name": "Pérez Moreno",
                "password": "Prop2025!",
                "ci": "86420975",
                "telefono": "+591 70555666",
                "fecha_nacimiento": date(1976, 6, 9)
            }
        ]
        
        propietarios_creados = []
        
        for prop_data in propietarios_data:
            # Crear usuario
            user = User.objects.create_user(
                username=prop_data["username"],
                email=prop_data["email"],
                first_name=prop_data["first_name"],
                last_name=prop_data["last_name"],
                password=prop_data["password"]
            )
            
            # Crear perfil
            perfil = PerfilUsuario.objects.create(
                user=user,
                condominio=condominio,
                tipo_usuario=tipo_propietario,
                ci=prop_data["ci"],
                telefono=prop_data["telefono"],
                fecha_nacimiento=prop_data["fecha_nacimiento"]
            )
            
            propietarios_creados.append(perfil)
        
        self.stdout.write(f"✅ {len(propietarios_creados)} propietarios creados")
        return propietarios_creados

    def crear_unidades(self, condominio):
        """Crear unidades del condominio"""
        self.stdout.write("🏠 Creando unidades...")
        
        # Obtener tipos de unidad
        tipo_1dorm = TipoUnidad.objects.get(nombre="Departamento 1 Dorm")
        tipo_2dorm = TipoUnidad.objects.get(nombre="Departamento 2 Dorm")
        tipo_3dorm = TipoUnidad.objects.get(nombre="Departamento 3 Dorm")
        tipo_ph = TipoUnidad.objects.get(nombre="Penthouse")
        tipo_oficina = TipoUnidad.objects.get(nombre="Oficina")
        
        unidades_data = [
            # Torre A
            ("A-101", tipo_2dorm, 1, "A", "75.5", 2, 2, "2.5"),
            ("A-102", tipo_1dorm, 1, "A", "55.0", 1, 1, "1.8"),
            ("A-103", tipo_2dorm, 1, "A", "80.0", 2, 2, "2.6"),
            ("A-201", tipo_2dorm, 2, "A", "75.5", 2, 2, "2.5"),
            ("A-202", tipo_1dorm, 2, "A", "55.0", 1, 1, "1.8"),
            ("A-203", tipo_2dorm, 2, "A", "80.0", 2, 2, "2.6"),
            ("A-301", tipo_3dorm, 3, "A", "110.0", 3, 3, "3.5"),
            ("A-302", tipo_2dorm, 3, "A", "75.5", 2, 2, "2.5"),
            ("A-401", tipo_3dorm, 4, "A", "110.0", 3, 3, "3.5"),
            ("A-PH1", tipo_ph, 5, "A", "180.0", 4, 4, "6.0"),
            
            # Torre B
            ("B-101", tipo_2dorm, 1, "B", "78.0", 2, 2, "2.6"),
            ("B-102", tipo_3dorm, 1, "B", "105.0", 3, 2, "3.4"),
            ("B-201", tipo_2dorm, 2, "B", "78.0", 2, 2, "2.6"),
            ("B-202", tipo_3dorm, 2, "B", "105.0", 3, 2, "3.4"),
            ("B-301", tipo_3dorm, 3, "B", "115.0", 3, 3, "3.7"),
            ("B-PH1", tipo_ph, 5, "B", "200.0", 4, 4, "6.5"),
            
            # Planta Baja
            ("PB-01", tipo_oficina, 0, "PB", "35.0", 0, 1, "1.2"),
            ("PB-02", tipo_oficina, 0, "PB", "42.0", 0, 1, "1.4"),
        ]
        
        unidades_creadas = []
        
        for numero, tipo, piso, bloque, m2, dorm, banos, porcentaje in unidades_data:
            unidad = Unidad.objects.create(
                condominio=condominio,
                numero=numero,
                tipo_unidad=tipo,
                piso=piso,
                bloque=bloque,
                metros_cuadrados=Decimal(m2),
                dormitorios=dorm,
                baños=banos,
                porcentaje_propiedad=Decimal(porcentaje)
            )
            unidades_creadas.append(unidad)
        
        self.stdout.write(f"✅ {len(unidades_creadas)} unidades creadas")
        return unidades_creadas

    def asignar_residencias(self, unidades, propietarios):
        """Asignar propietarios a unidades"""
        self.stdout.write("🔑 Asignando residencias...")
        
        # Asignaciones específicas
        asignaciones = [
            ("A-101", "prop_juan"),
            ("A-201", "prop_ana"),
            ("A-301", "prop_miguel"),
            ("B-101", "prop_lucia"),
            ("A-PH1", "prop_ricardo"),
        ]
        
        residencias_creadas = 0
        
        for numero_unidad, username in asignaciones:
            try:
                unidad = next(u for u in unidades if u.numero == numero_unidad)
                propietario = next(p for p in propietarios if p.user.username == username)
                
                ResidenciaUnidad.objects.create(
                    usuario=propietario,
                    unidad=unidad,
                    es_propietario=True,
                    porcentaje_propiedad=Decimal("100.00"),
                    fecha_inicio=date(2024, 1, 1)
                )
                residencias_creadas += 1
                
            except StopIteration:
                continue
        
        self.stdout.write(f"✅ {residencias_creadas} residencias asignadas")

    def crear_areas_comunes(self, condominio):
        """Crear áreas comunes"""
        self.stdout.write("🏊 Creando áreas comunes...")
        
        areas_data = [
            {
                "nombre": "Piscina Principal",
                "descripcion": "Piscina climatizada con área para niños y adultos",
                "capacidad_maxima": 30,
                "precio_por_hora": Decimal("80.00"),
                "requiere_deposito": False,
                "monto_deposito": Decimal("0.00"),
                "hora_apertura": "06:00",
                "hora_cierre": "22:00",
                "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"],
                "equipamiento": "Piscina climatizada, área para niños, duchas, vestidores",
                "reglas": "No se permite comida dentro del área de piscina. Uso de gorra obligatorio."
            },
            {
                "nombre": "Gimnasio",
                "descripcion": "Gimnasio completamente equipado con máquinas modernas",
                "capacidad_maxima": 20,
                "precio_por_hora": Decimal("50.00"),
                "requiere_deposito": False,
                "monto_deposito": Decimal("0.00"),
                "hora_apertura": "05:00",
                "hora_cierre": "23:00",
                "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"],
                "equipamiento": "Máquinas de cardio, pesas libres, máquinas de musculación, espejos",
                "reglas": "Uso de toalla obligatorio. Máximo 1 hora por sesión en horarios pico."
            },
            {
                "nombre": "Salón de Eventos",
                "descripcion": "Salón elegante para celebraciones y eventos familiares",
                "capacidad_maxima": 80,
                "precio_por_hora": Decimal("200.00"),
                "requiere_deposito": True,
                "monto_deposito": Decimal("500.00"),
                "hora_apertura": "08:00",
                "hora_cierre": "02:00",
                "dias_disponibles": ["viernes", "sabado", "domingo"],
                "equipamiento": "Mesas, sillas, equipo de sonido, cocina equipada, aire acondicionado",
                "reglas": "Prohibido fumar. Música hasta las 24:00. Limpieza obligatoria al finalizar."
            },
            {
                "nombre": "Cancha de Tenis",
                "descripcion": "Cancha de tenis profesional con iluminación nocturna",
                "capacidad_maxima": 4,
                "precio_por_hora": Decimal("120.00"),
                "requiere_deposito": False,
                "monto_deposito": Decimal("0.00"),
                "hora_apertura": "06:00",
                "hora_cierre": "22:00",
                "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"],
                "equipamiento": "Cancha reglamentaria, iluminación LED, red profesional",
                "reglas": "Calzado deportivo obligatorio. Reservas máximo con 7 días de anticipación."
            },
            {
                "nombre": "Área de BBQ",
                "descripcion": "Área de parrillas al aire libre con vista al jardín",
                "capacidad_maxima": 25,
                "precio_por_hora": Decimal("60.00"),
                "requiere_deposito": False,
                "monto_deposito": Decimal("0.00"),
                "hora_apertura": "10:00",
                "hora_cierre": "22:00",
                "dias_disponibles": ["sabado", "domingo"],
                "equipamiento": "Parrillas a gas, mesas, sillas, fregadero, área verde",
                "reglas": "Prohibido carbón. Limpieza de parrillas obligatoria. No se permite música alta."
            },
            {
                "nombre": "Sala de Juegos",
                "descripcion": "Sala recreativa con juegos para toda la familia",
                "capacidad_maxima": 15,
                "precio_por_hora": Decimal("40.00"),
                "requiere_deposito": False,
                "monto_deposito": Decimal("0.00"),
                "hora_apertura": "09:00",
                "hora_cierre": "21:00",
                "dias_disponibles": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"],
                "equipamiento": "Mesa de pool, ping pong, futbolín, juegos de mesa, TV",
                "reglas": "Niños menores de 12 años deben estar acompañados. Cuidar el mobiliario."
            }
        ]
        
        areas_creadas = []
        
        for area_data in areas_data:
            area = AreaComun.objects.create(
                condominio=condominio,
                **area_data
            )
            areas_creadas.append(area)
        
        self.stdout.write(f"✅ {len(areas_creadas)} áreas comunes creadas")
        return areas_creadas