# Smart Condominio - Aplicación Móvil

Aplicación móvil Flutter para la gestión inteligente de condominios con tecnología de inteligencia artificial.

## Características Principales

### 🏠 Dashboard Principal
- Vista general del estado del condominio
- Accesos rápidos a funciones principales
- Feed de actividades recientes
- Navegación intuitiva con pestañas

### 💰 Gestión Financiera
- Consulta de balance y cuotas
- Histórico de pagos
- Procesamiento de pagos con múltiples métodos
- Notificaciones de vencimientos

### 🎯 Reserva de Áreas Comunes
- Vista de áreas disponibles
- Sistema de reservas con calendario
- Gestión de reservas activas
- Precios y disponibilidad en tiempo real

### 🔔 Centro de Notificaciones
- **Avisos Administrativos**: Comunicados oficiales del condominio
- **Alertas de Seguridad**: Notificaciones de IA sobre incidentes
- **Emergencias**: Alertas críticas con prioridad alta
- Sistema de notificaciones push

### 👤 Perfil de Usuario
- Información personal y de residencia
- Configuraciones de la aplicación
- Gestión de familia, vehículos y mascotas
- Configuraciones de privacidad y seguridad

## Tecnologías Utilizadas

- **Flutter 3.1+**: Framework de desarrollo multiplataforma
- **Material Design 3**: Sistema de diseño moderno
- **Dart**: Lenguaje de programación
- **HTTP**: Comunicación con API backend
- **Shared Preferences**: Almacenamiento local
- **Local Notifications**: Notificaciones locales
- **QR Scanner**: Escaneo de códigos QR
- **Image Picker**: Selección de imágenes

## Estructura del Proyecto

```
lib/
├── main.dart                 # Punto de entrada de la aplicación
└── screens/
    ├── splash_screen.dart    # Pantalla de carga inicial
    ├── login_screen.dart     # Autenticación de usuarios
    ├── home_screen.dart      # Dashboard principal con navegación
    ├── finance_screen.dart   # Gestión financiera
    ├── areas_screen.dart     # Reserva de áreas comunes
    ├── notifications_screen.dart # Centro de notificaciones
    └── profile_screen.dart   # Perfil y configuraciones
```

## Instalación y Configuración

### Prerrequisitos
- Flutter SDK 3.1.0 o superior
- Dart SDK
- Android Studio / VS Code
- Dispositivo Android o iOS para pruebas

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd smart-condominio/mobile
   ```

2. **Instalar dependencias**
   ```bash
   flutter pub get
   ```

3. **Verificar instalación de Flutter**
   ```bash
   flutter doctor
   ```

4. **Ejecutar la aplicación**
   ```bash
   flutter run
   ```

### Configuración de Assets

1. Crear directorios de assets:
   ```bash
   mkdir -p assets/images
   mkdir -p assets/icons
   ```

2. Agregar icono de la aplicación en `assets/icons/app_icon.png`

3. Generar iconos para todas las plataformas:
   ```bash
   flutter pub run flutter_launcher_icons:main
   ```

## Credenciales de Demo

Para probar la aplicación, utiliza las siguientes credenciales:

- **Usuario**: demo@condominio.com
- **Contraseña**: 123456

## Funcionalidades Implementadas

### ✅ Completadas
- [x] Pantalla de splash con animaciones
- [x] Sistema de autenticación
- [x] Dashboard principal con navegación por pestañas
- [x] Gestión financiera completa
- [x] Sistema de reservas de áreas comunes
- [x] Centro de notificaciones tri-panel
- [x] Perfil de usuario con configuraciones
- [x] Diseño responsivo con Material Design 3
- [x] Navegación fluida entre pantallas

### 🔄 En Desarrollo
- [ ] Integración con API del backend Django
- [ ] Notificaciones push con Firebase
- [ ] Escaneo de códigos QR
- [ ] Procesamiento real de pagos
- [ ] Sincronización en tiempo real
- [ ] Modo offline

### 🎯 Próximas Mejoras
- [ ] Biometría para autenticación
- [ ] Chat integrado con administración
- [ ] Mapa interactivo del condominio
- [ ] Reportes de incidentes
- [ ] Sistema de votaciones
- [ ] Integración con IoT

## Arquitectura de la Aplicación

### Patrón de Diseño
- **Stateful Widgets**: Para manejo de estado local
- **Navigator 2.0**: Para navegación avanzada
- **Provider/Riverpod**: Para gestión de estado global (próximo)

### Comunicación con Backend
- **REST API**: Comunicación HTTP con Django backend
- **JSON**: Formato de intercambio de datos
- **JWT**: Autenticación basada en tokens
- **WebSockets**: Para notificaciones en tiempo real (próximo)

## Testing

### Ejecutar Tests
```bash
# Tests unitarios
flutter test

# Tests de integración
flutter test integration_test/

# Tests de UI
flutter drive --target=test_driver/app.dart
```

## Build y Distribución

### Android
```bash
# Debug APK
flutter build apk --debug

# Release APK
flutter build apk --release

# App Bundle para Play Store
flutter build appbundle --release
```

### iOS
```bash
# Debug
flutter build ios --debug

# Release
flutter build ios --release
```

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Equipo de Desarrollo

- **Desarrollador Principal**: [Tu Nombre]
- **UI/UX Designer**: [Nombre del Diseñador]
- **Backend Developer**: [Nombre del Backend Dev]

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para detalles.

## Contacto

- **Email**: desarrollo@smartcondominio.com
- **Sitio Web**: https://smartcondominio.com
- **Documentación**: https://docs.smartcondominio.com

---

**Smart Condominio** - Transformando la gestión residencial con tecnología inteligente 🏢✨
