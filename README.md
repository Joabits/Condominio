# 🏢 Smart Condominium - Sistema Inteligente de Administración de Condominios

## 📖 Descripción del Proyecto

Smart Condominium es una aplicación web y móvil completa para la gestión de condominios residenciales que incorpora **Inteligencia Artificial** y **Visión Artificial** para mejorar la seguridad, automatizar procesos y optimizar la experiencia de los residentes.

### 🎯 Características Principales

- **🧠 Inteligencia Artificial Integrada**
  - Reconocimiento facial para control de acceso
  - Detección automática de vehículos (OCR de placas)
  - Predicción de morosidad financiera
  - Detección de anomalías y comportamientos sospechosos

- **🔐 Seguridad Avanzada**
  - Control de acceso automatizado
  - Cámaras con visión artificial
  - Alertas en tiempo real
  - Registro automático de visitantes

- **💰 Gestión Financiera Completa**
  - Pagos online integrados
  - Recordatorios automáticos
  - Reportes financieros con IA
  - Control de morosidad

- **📱 Aplicación Móvil**
  - Notificaciones push en tiempo real
  - Reservas de áreas comunes
  - Consulta y pago de expensas
  - Comunicación con administración

## 🛠️ Stack Tecnológico

### Backend
- **Framework**: Django 5.2.6
- **API**: Django REST Framework
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Autenticación**: JWT Tokens

### Frontend Web
- **Framework**: React 19.1.0
- **Build Tool**: Next.js 15.5.2
- **Styling**: Tailwind CSS 4
- **TypeScript**: Soporte completo

### Aplicación Móvil
- **Framework**: Flutter
- **Notificaciones**: Firebase Cloud Messaging

### Servicios de IA
- **Proveedores**: Microsoft Azure / Amazon AWS / Google Cloud
- **Reconocimiento Facial**: Azure Face API
- **OCR**: Azure Computer Vision
- **Machine Learning**: TensorFlow / PyTorch

## 📋 Funcionalidades Implementadas

### ✅ Sistema Base Completado

#### Modelos de Datos
- [x] **Condominio**: Información principal del condominio
- [x] **Usuarios**: Sistema de roles (Administrador, Propietario, Inquilino, Seguridad, Mantenimiento)
- [x] **Unidades**: Gestión de apartamentos/casas
- [x] **Vehículos**: Registro de vehículos de residentes
- [x] **Áreas Comunes**: Espacios compartidos del condominio

#### Seguridad e IA
- [x] **Cámaras de Seguridad**: Gestión de cámaras con capacidades de IA
- [x] **Registro de Accesos**: Control de entradas y salidas
- [x] **Visitantes**: Gestión automática de visitantes
- [x] **Alertas de Seguridad**: Sistema de alertas con IA

#### Sistema Financiero
- [x] **Configuración de Expensas**: Setup de costos por período
- [x] **Cuotas de Mantenimiento**: Generación automática de cuotas
- [x] **Métodos de Pago**: Configuración de formas de pago
- [x] **Pagos**: Registro y seguimiento de pagos
- [x] **Predicción de Morosidad**: IA para predecir riesgos de pago

#### Comunicación
- [x] **Comunicados**: Sistema de anuncios y noticias
- [x] **Notificaciones Push**: Alertas en tiempo real
- [x] **Configuración de Notificaciones**: Preferencias por usuario

#### Mantenimiento
- [x] **Tipos de Mantenimiento**: Categorización de servicios
- [x] **Personal de Mantenimiento**: Gestión de staff interno y externo
- [x] **Solicitudes de Mantenimiento**: Sistema de tickets
- [x] **Mantenimiento Preventivo**: Programación automática

### 🚀 Configuración Completada

- [x] **Base de Datos**: Modelos y migraciones creadas
- [x] **Panel de Administración**: Django Admin configurado
- [x] **Datos Iniciales**: Comando de setup automático
- [x] **Servidor de Desarrollo**: Funcionando correctamente

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.13+
- Node.js 18+
- Git

### Backend (Django)

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Joabits/Condominio.git
   cd Condominio/backend
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py migrate
   ```

5. **Crear datos iniciales**
   ```bash
   python manage.py setup_initial_data
   ```

6. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

### Frontend (Next.js)

1. **Navegar al directorio frontend**
   ```bash
   cd ../frontend
   ```

2. **Instalar dependencias**
   ```bash
   npm install
   ```

3. **Ejecutar servidor de desarrollo**
   ```bash
   npm run dev
   ```

## 🔐 Acceso al Sistema

### Panel de Administración
- **URL**: http://localhost:8000/admin/
- **Usuario**: admin
- **Contraseña**: admin123

### Aplicación Web
- **URL**: http://localhost:3000/

## 📊 Estructura del Proyecto

```
Condominio/
├── backend/                 # Django Backend
│   ├── core/               # Configuración principal
│   ├── comunidad/          # App principal
│   │   ├── models.py       # Modelos de datos
│   │   ├── admin.py        # Configuración del admin
│   │   ├── views.py        # Vistas y API endpoints
│   │   └── management/     # Comandos personalizados
│   ├── media/              # Archivos multimedia
│   ├── static/             # Archivos estáticos
│   └── requirements.txt    # Dependencias Python
├── frontend/               # Next.js Frontend
│   ├── src/app/           # Páginas de la aplicación
│   ├── public/            # Recursos públicos
│   └── package.json       # Dependencias Node.js
└── README.md              # Este archivo
```

## 🔧 Próximas Implementaciones

### 📱 Aplicación Móvil
- [ ] Desarrollo en Flutter
- [ ] Integración con APIs del backend
- [ ] Notificaciones push
- [ ] Funcionalidades offline

### 🤖 Servicios de IA
- [ ] Configuración de Azure Face API
- [ ] Implementación de reconocimiento facial
- [ ] OCR para lectura de placas
- [ ] Algoritmos de detección de anomalías
- [ ] Predicción de morosidad con ML

### 🌐 APIs REST
- [ ] Endpoints para aplicación móvil
- [ ] Autenticación JWT
- [ ] Documentación con Swagger
- [ ] Rate limiting y seguridad

### 🎨 Frontend Web
- [ ] Dashboard administrativo
- [ ] Portal de residentes
- [ ] Reportes interactivos
- [ ] Integración con servicios de pago

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **Joabits** - *Desarrollo inicial* - [Joabits](https://github.com/Joabits)

## 🙏 Agradecimientos

- Universidad Autónoma Gabriel René Moreno (UAGRM)
- Facultad de Ciencias de la Computación y Telecomunicaciones (FICCT)
- MSC. Ing. Angélica Garzón Cuéllar - Docente de Sistemas de Información II

---

**📞 Contacto**: Para preguntas sobre el proyecto, por favor crea un issue en GitHub.

**🌟 ¡No olvides dar una estrella al proyecto si te resulta útil!**