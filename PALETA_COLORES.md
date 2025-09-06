# 🎨 Paleta de Colores Resolution Blue - Condominio Buganvillas

## 📋 Resumen

La paleta **Resolution Blue** proporciona una identidad visual consistente y profesional para el sistema de gestión del Condominio Buganvillas. Esta documentación describe la implementación completa de la paleta en las plataformas web (Next.js) y móvil (Flutter).

## 🎯 Colores principales

### Resolution Blue Palette
| Shade | Hex Code | RGB | Uso recomendado |
|-------|----------|-----|-----------------|
| 50    | #e4f4ff | rgb(228, 244, 255) | Fondos muy suaves |
| 100   | #cee9ff | rgb(206, 233, 255) | Fondos suaves |
| 200   | #a4d3ff | rgb(164, 211, 255) | Elementos secundarios |
| 300   | #6bb5ff | rgb(107, 181, 255) | Bordes y separadores |
| 400   | #1485ff | rgb(20, 133, 255) | Elementos interactivos |
| 500   | #0066ff | rgb(0, 102, 255) | **Color principal** |
| 600   | #0052d6 | rgb(0, 82, 214) | Estados hover |
| 700   | #0047c7 | rgb(0, 71, 199) | Elementos activos |
| 800   | #0439a1 | rgb(4, 57, 161) | Textos importantes |
| 900   | #0a3680 | rgb(10, 54, 128) | Textos principales |
| 950   | #001a80 | rgb(0, 26, 128) | Textos muy oscuros |

## 🌐 Implementación Web (Next.js + Tailwind CSS)

### Configuración
El archivo `frontend/tailwind.config.js` contiene la configuración completa de la paleta:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        50: '#e4f4ff',
        100: '#cee9ff',
        200: '#a4d3ff',
        300: '#6bb5ff',
        400: '#1485ff',
        500: '#0066ff', // Color principal
        600: '#0052d6',
        700: '#0047c7',
        800: '#0439a1',
        900: '#0a3680',
        950: '#001a80',
      }
    }
  }
}
```

### CSS Variables
En `frontend/src/app/globals.css`:

```css
:root {
  --primary-50: 228 244 255;
  --primary-100: 206 233 255;
  --primary-200: 164 211 255;
  --primary-300: 107 181 255;
  --primary-400: 20 133 255;
  --primary-500: 0 102 255;
  --primary-600: 0 82 214;
  --primary-700: 0 71 199;
  --primary-800: 4 57 161;
  --primary-900: 10 54 128;
  --primary-950: 0 26 128;
}
```

### Uso en componentes
```jsx
// Botones
<button className="bg-primary-500 hover:bg-primary-600 text-white">
  Iniciar Sesión
</button>

// Cards
<div className="bg-primary-50 border border-primary-200">
  Contenido
</div>

// Texto
<h1 className="text-primary-900">Título principal</h1>
<p className="text-primary-700">Texto secundario</p>
```

## 📱 Implementación Mobile (Flutter)

### Configuración de colores
El archivo `mobile/lib/constants/colors.dart` define todas las constantes:

```dart
class AppColors {
  // Resolution Blue Palette
  static const Color primary50 = Color(0xFFE4F4FF);
  static const Color primary100 = Color(0xFFCEE9FF);
  static const Color primary200 = Color(0xFFA4D3FF);
  static const Color primary300 = Color(0xFF6BB5FF);
  static const Color primary400 = Color(0xFF1485FF);
  static const Color primary500 = Color(0xFF0066FF); // Principal
  static const Color primary600 = Color(0xFF0052D6);
  static const Color primary700 = Color(0xFF0047C7);
  static const Color primary800 = Color(0xFF0439A1);
  static const Color primary900 = Color(0xFF0A3680);
  static const Color primary950 = Color(0xFF001A80);
}
```

### Theme configuration
El archivo `mobile/lib/constants/theme.dart` configura Material 3:

```dart
class AppTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSwatch(
        primarySwatch: _createMaterialColor(AppColors.primary500),
      ).copyWith(
        primary: AppColors.primary500,
        onPrimary: Colors.white,
        secondary: AppColors.primary300,
        onSecondary: AppColors.primary900,
      ),
    );
  }
}
```

### Uso en widgets
```dart
// Botones
ElevatedButton(
  style: ElevatedButton.styleFrom(
    backgroundColor: AppColors.primary500,
    foregroundColor: Colors.white,
  ),
  onPressed: () {},
  child: Text('Iniciar Sesión'),
)

// Cards
Card(
  elevation: 4,
  shadowColor: AppColors.primary500.withOpacity(0.2),
  child: Container(
    decoration: BoxDecoration(
      gradient: AppColors.primaryGradientSoft,
    ),
    child: Content(),
  ),
)

// Texto
Text(
  'Título principal',
  style: TextStyle(
    color: AppColors.primary900,
    fontWeight: FontWeight.bold,
  ),
)
```

## 🎨 Gradientes incluidos

### Web (CSS)
```css
.gradient-primary {
  background: linear-gradient(135deg, rgb(0, 102, 255), rgb(0, 71, 199));
}

.gradient-soft {
  background: linear-gradient(135deg, rgb(228, 244, 255), rgb(164, 211, 255));
}
```

### Mobile (Flutter)
```dart
static const LinearGradient primaryGradient = LinearGradient(
  begin: Alignment.topLeft,
  end: Alignment.bottomRight,
  colors: [primary500, primary700],
);

static const LinearGradient primaryGradientSoft = LinearGradient(
  begin: Alignment.topLeft,
  end: Alignment.bottomRight,
  colors: [primary50, primary200],
);
```

## 📱 Ejemplos de uso

### Frontend Web (Next.js)
Ve el archivo `frontend/src/app/color-example/page.tsx` para ejemplos completos de:
- Cards con gradientes Resolution Blue
- Botones con diferentes estados
- Campos de entrada con focus states
- Paleta completa de colores
- Mejores prácticas de implementación

Para ver los ejemplos: `http://localhost:3000/color-example`

### Mobile (Flutter)
Ve el archivo `mobile/lib/screens/color_example_screen.dart` para ejemplos de:
- Material 3 theming con Resolution Blue
- Cards con gradientes nativos
- Botones ElevatedButton, OutlinedButton y TextButton
- TextFields con theming consistente
- Widgets con la paleta completa

### Comandos de ejemplo

**Web (Next.js):**
```bash
cd frontend
npm run dev
# Navega a http://localhost:3000/color-example
```

**Mobile (Flutter):**
```bash
cd mobile
flutter run
# Navega a ColorExampleScreen en la app
```

## 🎯 Guías de uso

### Jerarquía de colores
- **primary-950 a primary-800**: Textos principales y encabezados importantes
- **primary-700 a primary-600**: Estados activos y hover
- **primary-500**: Color principal para CTAs y elementos destacados
- **primary-400 a primary-300**: Elementos interactivos secundarios
- **primary-200 a primary-50**: Fondos suaves y elementos de soporte

### Accesibilidad
- Contraste mínimo AA: 4.5:1 para texto normal
- Contraste AAA: 7:1 para texto importante
- Todos los colores principales cumplen estándares WCAG

### Consistencia entre plataformas
- Los valores hexadecimales son idénticos en web y mobile
- Los gradientes mantienen las mismas proporciones
- Las jerarquías de color son consistentes

## 🔧 Archivos modificados

### Frontend (Web)
- `frontend/tailwind.config.js` - Configuración de Tailwind CSS
- `frontend/src/app/globals.css` - Variables CSS y estilos globales
- `frontend/src/app/color-example/page.tsx` - Página de ejemplos

### Mobile (Flutter)
- `mobile/lib/constants/colors.dart` - Constantes de colores
- `mobile/lib/constants/theme.dart` - Configuración del tema Material 3
- `mobile/lib/main.dart` - Aplicación del tema
- `mobile/lib/screens/color_example_screen.dart` - Pantalla de ejemplos

## 🔄 Actualización de componentes existentes

Para aplicar la nueva paleta a componentes existentes:

### Web
1. Reemplaza clases de color existentes por las nuevas (ej: `bg-blue-500` → `bg-primary-500`)
2. Actualiza variables CSS personalizadas
3. Verifica el contraste en textos

### Mobile
1. Reemplaza `Colors.blue` por `AppColors.primary500`
2. Actualiza themes personalizados
3. Verifica que Material 3 esté habilitado

## 🔗 Enlaces útiles

- [Documentación de Tailwind CSS Colors](https://tailwindcss.com/docs/customizing-colors)
- [Material 3 Color System](https://m3.material.io/styles/color/system/overview)
- [Flutter Theme Documentation](https://docs.flutter.dev/ui/design/material)
- [WCAG Color Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)

---

**Implementado por:** GitHub Copilot  
**Fecha:** Diciembre 2024  
**Proyecto:** Condominio Buganvillas - Sistema de Gestión Inteligente