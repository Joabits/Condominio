import 'package:flutter/material.dart';

/// Paleta de colores Resolution Blue para Condominio Buganvillas
/// Consistente con la aplicación web
class AppColors {
  // Paleta Principal - Resolution Blue
  static const Color primary50 = Color(0xFFE4F4FF);
  static const Color primary100 = Color(0xFFCFEAFF);
  static const Color primary200 = Color(0xFFA8D6FF);
  static const Color primary300 = Color(0xFF74B9FF);
  static const Color primary400 = Color(0xFF3E88FF);
  static const Color primary500 = Color(0xFF135FFF); // Color principal
  static const Color primary600 = Color(0xFF0044FF);
  static const Color primary700 = Color(0xFF0044FF);
  static const Color primary800 = Color(0xFF003DE4);
  static const Color primary900 = Color(0xFF0029B0);
  static const Color primary950 = Color(0xFF001A80);

  // Colores de estado
  static const Color success50 = Color(0xFFF0FDF4);
  static const Color success500 = Color(0xFF22C55E);
  static const Color success600 = Color(0xFF16A34A);

  static const Color warning50 = Color(0xFFFFFBEB);
  static const Color warning500 = Color(0xFFF59E0B);
  static const Color warning600 = Color(0xFFD97706);

  static const Color error50 = Color(0xFFFEF2F2);
  static const Color error500 = Color(0xFFEF4444);
  static const Color error600 = Color(0xFFDC2626);

  // Grises neutros
  static const Color gray50 = Color(0xFFF9FAFB);
  static const Color gray100 = Color(0xFFF3F4F6);
  static const Color gray200 = Color(0xFFE5E7EB);
  static const Color gray300 = Color(0xFFD1D5DB);
  static const Color gray400 = Color(0xFF9CA3AF);
  static const Color gray500 = Color(0xFF6B7280);
  static const Color gray600 = Color(0xFF4B5563);
  static const Color gray700 = Color(0xFF374151);
  static const Color gray800 = Color(0xFF1F2937);
  static const Color gray900 = Color(0xFF111827);

  // Accesos rápidos
  static const Color primary = primary500;
  static const Color background = Colors.white;
  static const Color surface = Colors.white;
  static const Color onPrimary = Colors.white;
  static const Color onBackground = primary900;
  static const Color onSurface = primary900;

  // Gradientes
  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [primary500, primary600],
  );

  static const LinearGradient primaryGradientSoft = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [primary100, primary200],
  );

  static const LinearGradient backgroundGradient = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [primary50, Colors.white],
  );
}

/// Extensión para obtener colores por tonalidad
extension AppColorsExtension on AppColors {
  static Color primaryShade(int shade) {
    switch (shade) {
      case 50: return AppColors.primary50;
      case 100: return AppColors.primary100;
      case 200: return AppColors.primary200;
      case 300: return AppColors.primary300;
      case 400: return AppColors.primary400;
      case 500: return AppColors.primary500;
      case 600: return AppColors.primary600;
      case 700: return AppColors.primary700;
      case 800: return AppColors.primary800;
      case 900: return AppColors.primary900;
      case 950: return AppColors.primary950;
      default: return AppColors.primary500;
    }
  }
}