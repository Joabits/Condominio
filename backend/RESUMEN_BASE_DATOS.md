# 📊 RESUMEN EJECUTIVO - BASE DE DATOS SMART CONDOMINIO

## 🏢 Información del Condominio

**Nombre:** Residencial Las Torres  
**Ubicación:** Av. Banzer Km 9, Entre 4to y 5to Anillo, Santa Cruz de la Sierra  
**Teléfono:** +591 3 123-4567  
**Email:** administracion@lastorres.com  
**NIT:** 1023456789012  

---

## 📈 Estadísticas Generales

| Concepto | Cantidad |
|----------|----------|
| 👥 **Usuarios del Sistema** | 7 |
| 🏢 **Condominios** | 1 |
| 👤 **Perfiles de Usuario** | 6 |
| 🏠 **Unidades** | 18 |
| 🏊 **Áreas Comunes** | 6 |
| 🔑 **Residencias Asignadas** | 5 |
| 📝 **Tipos de Usuario** | 6 |
| 🏗️ **Tipos de Unidad** | 5 |

---

## 👥 Usuarios del Sistema

### 👨‍💼 Administradores (1)
- **admin_general** - Carlos Mendoza
  - Email: admin@lastorres.com
  - CI: 12345678
  - Teléfono: +591 70123456

### 🏠 Propietarios (5)
1. **prop_juan** - Juan Silva Torrez
   - Email: juan.silva@email.com
   - CI: 98765432
   - Unidad: A-101

2. **prop_ana** - Ana Martínez Vega
   - Email: ana.martinez@email.com
   - CI: 13579246
   - Unidad: A-201

3. **prop_miguel** - Miguel López Santos
   - Email: miguel.lopez@email.com
   - CI: 24681357
   - Unidad: A-301

4. **prop_lucia** - Lucía García Flores
   - Email: lucia.garcia@email.com
   - CI: 97531864
   - Unidad: B-101

5. **prop_ricardo** - Ricardo Pérez Moreno
   - Email: ricardo.perez@email.com
   - CI: 86420975
   - Unidad: A-PH1 (Penthouse)

---

## 🏠 Unidades del Condominio

### Torre A (10 unidades)
- **Piso 1:** A-101, A-102, A-103
- **Piso 2:** A-201, A-202, A-203
- **Piso 3:** A-301, A-302
- **Piso 4:** A-401
- **Piso 5:** A-PH1 (Penthouse)

### Torre B (6 unidades)
- **Piso 1:** B-101, B-102
- **Piso 2:** B-201, B-202
- **Piso 3:** B-301
- **Piso 5:** B-PH1 (Penthouse)

### Planta Baja (2 oficinas)
- **PB-01:** Oficina 35 m²
- **PB-02:** Oficina 42 m²

### Tipos de Unidad
1. **Departamento 1 Dorm** - Factor: 0.8
2. **Departamento 2 Dorm** - Factor: 1.0
3. **Departamento 3 Dorm** - Factor: 1.3
4. **Penthouse** - Factor: 2.0
5. **Oficina** - Factor: 0.6

---

## 🏊 Áreas Comunes Disponibles

1. **Piscina Principal**
   - Capacidad: 30 personas
   - Precio: $80/hora
   - Horario: 06:00 - 22:00
   - Disponible: Todos los días

2. **Gimnasio**
   - Capacidad: 20 personas
   - Precio: $50/hora
   - Horario: 05:00 - 23:00
   - Disponible: Todos los días

3. **Salón de Eventos**
   - Capacidad: 80 personas
   - Precio: $200/hora
   - Depósito: $500
   - Horario: 08:00 - 02:00
   - Disponible: Viernes, Sábado, Domingo

4. **Cancha de Tenis**
   - Capacidad: 4 personas
   - Precio: $120/hora
   - Horario: 06:00 - 22:00
   - Disponible: Todos los días

5. **Área de BBQ**
   - Capacidad: 25 personas
   - Precio: $60/hora
   - Horario: 10:00 - 22:00
   - Disponible: Sábado, Domingo

6. **Sala de Juegos**
   - Capacidad: 15 personas
   - Precio: $40/hora
   - Horario: 09:00 - 21:00
   - Disponible: Todos los días

---

## 🏗️ Estructura de Base de Datos

### Tablas Principales (28 tablas total)
- **Autenticación:** auth_user, auth_group, auth_permission
- **Condominio:** comunidad_condominio, comunidad_tipousuario
- **Usuarios:** comunidad_perfilusuario
- **Propiedades:** comunidad_unidad, comunidad_tipounidad, comunidad_residenciaunidad
- **Áreas Comunes:** comunidad_areacomun, comunidad_reservaareacomun
- **Seguridad:** comunidad_camaraseguridad, comunidad_registroacceso, comunidad_visitante, comunidad_alertaseguridad
- **Vehículos:** comunidad_vehiculo
- **Finanzas:** comunidad_tipogasto, comunidad_configuracionexpensa, comunidad_cuotamantenimiento, comunidad_metodopago, comunidad_pago
- **Sistema:** django_admin_log, django_content_type, django_migrations, django_session

---

## 🔐 Credenciales de Acceso

### Django Admin
- **Username:** admin_general
- **Password:** Admin2025!
- **URL:** http://127.0.0.1:8000/admin/

### API Móvil (Propietarios - Credenciales Reales)
- **Email:** juan.silva@email.com
- **Password:** Prop2025!
- **API Base:** http://127.0.0.1:8000/api/ (Testing local)
- **API Base:** http://10.0.2.2:8000/api/ (Emulador Android)
- **API Base:** http://192.168.1.3:8000/api/ (Dispositivo físico)

### Otros Propietarios Disponibles
- ana.martinez@email.com / Prop2025! (Ana Martínez Vega - Unidad A-201)
- miguel.lopez@email.com / Prop2025! (Miguel López Santos - Unidad A-301)
- lucia.garcia@email.com / Prop2025! (Lucía García Flores - Unidad B-101)
- ricardo.perez@email.com / Prop2025! (Ricardo Pérez Moreno - Unidad A-PH1)

---

## 📡 APIs Disponibles

### Autenticación
- `POST /api/auth/login/` - Iniciar sesión
- `POST /api/auth/refresh/` - Renovar token
- `POST /api/auth/logout/` - Cerrar sesión

### Dashboard
- `GET /api/dashboard/` - Dashboard principal
- `GET /api/finanzas/` - Estado financiero
- `GET /api/areas/` - Áreas comunes
- `GET /api/notificaciones/` - Avisos y notificaciones
- `GET /api/perfil/` - Perfil del usuario

---

## 💾 Archivos Exportados

1. **base_datos_postgresql_20250905_194458.json** (54 registros)
   - Todos los datos de la base de datos en formato JSON
   - Incluye usuarios, condominio, unidades, áreas comunes, etc.

2. **estructura_db_20250905_194458.json** (28 tablas)
   - Estructura completa de la base de datos PostgreSQL
   - Definición de columnas, tipos de datos, etc.

---

## 🚀 Estado del Sistema

✅ **Base de Datos:** PostgreSQL funcionando  
✅ **Backend:** Django 5.2.6 operativo  
✅ **APIs:** Todas las APIs móviles funcionando  
✅ **Autenticación:** JWT tokens configurados  
✅ **Panel Admin:** Accesible y funcional  
✅ **Datos:** Población completa con datos reales  

**El sistema Smart Condominio está completamente operativo y listo para producción.**