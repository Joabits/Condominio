# Paleta de Colores - Condominio Buganvillas

## Nueva Paleta Aplicada: Resolution Blue

La nueva paleta de colores "Resolution Blue" ha sido implementada en todo el sistema para dar una apariencia más moderna y cohesiva.

### Colores Principales (Primary)
```css
primary-50:  #e4f4ff  /* Fondo muy claro */
primary-100: #cfeaff  /* Fondo claro */
primary-200: #a8d6ff  /* Bordes suaves */
primary-300: #74b9ff  /* Texto secundario */
primary-400: #3e88ff  /* Iconos */
primary-500: #135fff  /* Color principal */
primary-600: #0044ff  /* Hover states */
primary-700: #0044ff  /* Texto importante */
primary-800: #003de4  /* Elementos oscuros */
primary-900: #0029b0  /* Texto principal */
primary-950: #001a80  /* Fondos oscuros */
```

### Colores de Estado
```css
success-50:  #f0fdf4
success-500: #22c55e
success-600: #16a34a

warning-50:  #fffbeb
warning-500: #f59e0b
warning-600: #d97706

error-50:    #fef2f2
error-500:   #ef4444
error-600:   #dc2626
```

### Gradientes Personalizados
```css
.primary-gradient: linear-gradient(135deg, #135fff 0%, #0044ff 100%)
.primary-gradient-soft: linear-gradient(135deg, #cfeaff 0%, #a8d6ff 100%)
```

## Archivos Actualizados

### Frontend Web (Next.js/React)
### 1. `tailwind.config.js`
- ✅ Nueva configuración de colores Resolution Blue
- ✅ Gradientes personalizados actualizados
- ✅ Colores de estado mantenidos

### 2. `src/app/globals.css`
- ✅ Variables CSS actualizadas con nuevos valores
- ✅ Estilos base mejorados
- ✅ Scrollbar personalizado con nueva paleta
- ✅ Clases utilitarias actualizadas

### 3. `src/components/Navigation.tsx`
- ✅ Header con fondo primary-950 actualizado
- ✅ Texto en tonos primary actualizados
- ✅ Hover states con nueva paleta
- ✅ Sidebar móvil actualizado

### 4. `src/app/login/page.tsx`
- ✅ Gradiente de fondo primary actualizado
- ✅ Campos de formulario con focus primary
- ✅ Botones con colores primary actualizados

### 5. `src/app/page.tsx` (Dashboard)
- ✅ Fondo con gradiente suave actualizado
- ✅ Cards con bordes primary nuevos
- ✅ Módulos con colores actualizados
- ✅ Sección de IA con gradiente primary

### Mobile App (Flutter/Dart)
### 6. `mobile/lib/constants/colors.dart` (NUEVO)
- ✅ Paleta completa Resolution Blue
- ✅ Colores de estado definidos
- ✅ Gradientes para Flutter
- ✅ Extensiones para fácil uso

### 7. `mobile/lib/constants/theme.dart` (NUEVO)
- ✅ Tema completo de Material 3
- ✅ AppBar, botones, cards con nueva paleta
- ✅ InputDecoration con colores primary
- ✅ Tema oscuro preparado

### 8. `mobile/lib/main.dart`
- ✅ Aplicación del nuevo tema
- ✅ Configuración de tema claro/oscuro
- ✅ Integración completa

## Cómo Usar la Nueva Paleta

### En la Web (Tailwind CSS)
### Para Fondos
```jsx
className="bg-primary-50"    // Fondo muy claro
className="bg-primary-100"   // Fondo claro
className="bg-primary-500"   // Fondo principal
className="bg-primary-950"   // Fondo oscuro
```

### Para Texto
```jsx
className="text-primary-900" // Texto principal
className="text-primary-700" // Texto importante
className="text-primary-500" // Texto destacado
className="text-primary-300" // Texto secundario
```

### En el Móvil (Flutter)
### Usando AppColors
```dart
// Colores directos
Container(color: AppColors.primary500)
Text('Título', style: TextStyle(color: AppColors.primary900))

// Usando el tema
Container(color: Theme.of(context).colorScheme.primary)
Text('Título', style: Theme.of(context).textTheme.headlineMedium)

// Gradientes
Container(
  decoration: BoxDecoration(
    gradient: AppColors.primaryGradient,
  ),
)
```

### Ejemplos Consistentes entre Plataformas

### Card Simple
**Web:**
```jsx
<div className="bg-white border border-primary-200 rounded-lg p-6 hover:shadow-lg">
  <h3 className="text-primary-900 font-semibold">Título</h3>
  <p className="text-primary-600">Contenido</p>
</div>
```

**Móvil:**
```dart
Card(
  child: Padding(
    padding: EdgeInsets.all(16),
    child: Column(
      children: [
        Text('Título', style: Theme.of(context).textTheme.headlineSmall),
        Text('Contenido', style: Theme.of(context).textTheme.bodyMedium),
      ],
    ),
  ),
)
```

### Botón Principal
**Web:**
```jsx
<button className="bg-primary-500 hover:bg-primary-600 text-white px-4 py-2 rounded-lg">
  Acción
</button>
```

**Móvil:**
```dart
ElevatedButton(
  onPressed: () {},
  child: Text('Acción'),
)
```

La nueva paleta "Resolution Blue" proporciona una identidad visual coherente y moderna para el sistema de gestión del Condominio Buganvillas en todas las plataformas.