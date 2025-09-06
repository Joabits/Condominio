# 🔐 CREDENCIALES DE ACCESO CORREGIDAS - CONDOMINIO BUGANVILLAS

## ⚠️ CORRECCIÓN CRÍTICA DE SEGURIDAD

**PROBLEMA IDENTIFICADO:** Los propietarios podían acceder a la aplicación web de administración.

**SOLUCIÓN IMPLEMENTADA:** Separación de endpoints y validación de roles por plataforma.

---

## 📱 **APLICACIÓN MÓVIL** (Solo Residentes)
**Usuarios autorizados:** Propietarios, Inquilinos, Personal de Mantenimiento/Seguridad

### 🏠 **Propietarios - Credenciales Válidas:**
```
Email: juan.silva@email.com
Contraseña: Prop2025!
Rol: PROPIETARIO (Unidad A-101)

Email: ana.martinez@email.com
Contraseña: Prop2025!
Rol: PROPIETARIO (Unidad A-201)

Email: miguel.lopez@email.com
Contraseña: Prop2025!
Rol: PROPIETARIO (Unidad A-301)

Email: lucia.garcia@email.com
Contraseña: Prop2025!
Rol: PROPIETARIO (Unidad B-101)

Email: ricardo.perez@email.com
Contraseña: Prop2025!
Rol: PROPIETARIO (Unidad A-PH1)
```

**Endpoint:** `POST /api/auth/mobile/login/`
**URLs de la API:**
- Testing local: `http://127.0.0.1:8000/api/`
- Emulador Android: `http://10.0.2.2:8000/api/`
- Dispositivo físico: `http://192.168.1.3:8000/api/`

---

## 💻 **APLICACIÓN WEB** (Solo Administración)
**Usuarios autorizados:** ÚNICAMENTE ADMINISTRADORES

### 👨‍💼 **Administradores - Credenciales Válidas:**
```
Email: admin@lastorres.com
Contraseña: Prop2025!
Rol: ADMINISTRADOR
Nombre: Carlos Mendoza
```

**Endpoint:** `POST /api/auth/web/login/`
**URL Web:** `http://localhost:3001/`

---

## 🚫 **VALIDACIONES DE SEGURIDAD IMPLEMENTADAS**

### ✅ Aplicación Móvil:
- **Permite:** PROPIETARIO, INQUILINO, SEGURIDAD, MANTENIMIENTO
- **Bloquea:** ADMINISTRADOR
- **Mensaje:** "Este tipo de usuario no tiene acceso a la aplicación móvil"

### ✅ Aplicación Web:
- **Permite:** ADMINISTRADOR
- **Bloquea:** PROPIETARIO, INQUILINO, SEGURIDAD, MANTENIMIENTO
- **Mensaje:** "Solo administradores pueden acceder a la aplicación web"
- **Redirección:** `/access-denied` (página explicativa)

---

## 🛠️ **PANEL DE ADMINISTRACIÓN DJANGO**
**Para desarrolladores y administración técnica**

```
Username: admin_general
Password: Admin2025!
URL: http://127.0.0.1:8000/admin/
```

---

## 🔍 **TESTING DE SEGURIDAD**

### ❌ **Tests que DEBEN FALLAR:**
1. **Propietario en Web:**
   - Email: `juan.silva@email.com` en `http://localhost:3001/login`
   - **Resultado esperado:** Error 403 + redirección a `/access-denied`

2. **Administrador en Móvil:**
   - Email: `admin@lastorres.com` en app móvil
   - **Resultado esperado:** Error 403 + mensaje de error

### ✅ **Tests que DEBEN FUNCIONAR:**
1. **Propietario en Móvil:**
   - Email: `juan.silva@email.com` en app móvil
   - **Resultado esperado:** Login exitoso + dashboard móvil

2. **Administrador en Web:**
   - Email: `admin@lastorres.com` en `http://localhost:3001/login`
   - **Resultado esperado:** Login exitoso + dashboard web

---

## 📊 **FUNCIONALIDADES POR PLATAFORMA**

### 📱 **Móvil (Residentes):**
- ✅ Consulta y pago de cuotas
- ✅ Historial de pagos
- ✅ Reservas de áreas comunes
- ✅ Notificaciones push
- ✅ Avisos de administración
- ✅ Perfil de usuario
- ❌ **NO TIENE:** Gestión administrativa, reportes, configuración del sistema

### 💻 **Web (Administración):**
- ✅ Gestión de usuarios y roles
- ✅ Administración financiera
- ✅ Control de cámaras con IA
- ✅ Gestión de áreas comunes
- ✅ Reportes y estadísticas
- ✅ Configuración del sistema
- ❌ **NO TIENE:** Funcionalidades de residente (por seguridad)

---

## 🔗 **URLs DE ACCESO ACTUALIZADAS:**

| Plataforma | URL | Estado | Usuarios Autorizados |
|------------|-----|--------|---------------------|
| **Backend Django** | http://127.0.0.1:8000/ | ✅ Activo | Todos |
| **Frontend Web** | http://localhost:3001/ | ✅ Activo | Solo ADMINISTRADORES |
| **Admin Django** | http://127.0.0.1:8000/admin/ | ✅ Activo | Solo desarrolladores |
| **API Móvil** | http://127.0.0.1:8000/api/auth/mobile/login/ | ✅ Activo | Solo RESIDENTES |
| **API Web** | http://127.0.0.1:8000/api/auth/web/login/ | ✅ Activo | Solo ADMINISTRADORES |

---

## 🚨 **IMPORTANTE:**

1. **Los propietarios YA NO PUEDEN acceder a la aplicación web**
2. **Los administradores YA NO PUEDEN acceder a la aplicación móvil**
3. **Cada plataforma tiene endpoints específicos con validación de roles**
4. **Errores 403 redirigen a páginas explicativas apropiadas**
5. **Sistema completamente seguro según especificaciones del proyecto**

¡El sistema ahora cumple correctamente con la separación de roles especificada en el documento del proyecto! 🎯