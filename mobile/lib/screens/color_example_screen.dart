import 'package:flutter/material.dart';
import '../constants/colors.dart';

/// Ejemplos de uso de la paleta Resolution Blue en Flutter
/// Este archivo demuestra cómo usar los colores correctamente
class ColorExampleScreen extends StatelessWidget {
  const ColorExampleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Paleta Resolution Blue'),
        backgroundColor: AppColors.primary950,
        foregroundColor: AppColors.primary100,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Título principal
            Text(
              'Condominio Buganvillas',
              style: Theme.of(context).textTheme.displayMedium?.copyWith(
                color: AppColors.primary900,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Sistema de Gestión Inteligente',
              style: Theme.of(context).textTheme.titleLarge?.copyWith(
                color: AppColors.primary700,
              ),
            ),
            const SizedBox(height: 32),

            // Cards de ejemplo
            const Text(
              'Cards con la nueva paleta:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w600,
                color: AppColors.primary900,
              ),
            ),
            const SizedBox(height: 16),

            // Card principal
            Card(
              elevation: 4,
              shadowColor: AppColors.primary500.withOpacity(0.2),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
                side: const BorderSide(color: AppColors.primary200),
              ),
              child: Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                  gradient: AppColors.primaryGradientSoft,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(12),
                          decoration: BoxDecoration(
                            color: AppColors.primary500,
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: const Icon(
                            Icons.home,
                            color: Colors.white,
                            size: 24,
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Dashboard Principal',
                                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                                  color: AppColors.primary900,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                              Text(
                                'Vista general del condominio',
                                style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                                  color: AppColors.primary700,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),

            // Botones de ejemplo
            const Text(
              'Botones con la nueva paleta:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w600,
                color: AppColors.primary900,
              ),
            ),
            const SizedBox(height: 16),

            // Botón principal
            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: () {},
                icon: const Icon(Icons.login),
                label: const Text('Iniciar Sesión'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.primary500,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 12),

            // Botón secundario
            SizedBox(
              width: double.infinity,
              child: OutlinedButton.icon(
                onPressed: () {},
                icon: const Icon(Icons.person_add),
                label: const Text('Registrarse'),
                style: OutlinedButton.styleFrom(
                  foregroundColor: AppColors.primary600,
                  side: const BorderSide(color: AppColors.primary300, width: 2),
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 12),

            // Botón de texto
            SizedBox(
              width: double.infinity,
              child: TextButton.icon(
                onPressed: () {},
                icon: const Icon(Icons.help_outline),
                label: const Text('¿Necesitas ayuda?'),
                style: TextButton.styleFrom(
                  foregroundColor: AppColors.primary600,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
              ),
            ),
            const SizedBox(height: 32),

            // Campos de entrada
            const Text(
              'Campos de entrada:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w600,
                color: AppColors.primary900,
              ),
            ),
            const SizedBox(height: 16),

            TextField(
              decoration: InputDecoration(
                labelText: 'Correo electrónico',
                hintText: 'tu@email.com',
                prefixIcon: const Icon(Icons.email),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
            const SizedBox(height: 16),

            TextField(
              obscureText: true,
              decoration: InputDecoration(
                labelText: 'Contraseña',
                hintText: '••••••••',
                prefixIcon: const Icon(Icons.lock),
                suffixIcon: const Icon(Icons.visibility),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
            const SizedBox(height: 32),

            // Gradiente de fondo
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                gradient: AppColors.primaryGradient,
                borderRadius: BorderRadius.circular(16),
              ),
              child: Column(
                children: [
                  const Icon(
                    Icons.security,
                    color: Colors.white,
                    size: 48,
                  ),
                  const SizedBox(height: 16),
                  const Text(
                    'Seguridad Inteligente',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Con IA y reconocimiento facial',
                    style: TextStyle(
                      color: Colors.white.withOpacity(0.9),
                      fontSize: 16,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 32),

            // Paleta de colores
            const Text(
              'Paleta de colores Resolution Blue:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w600,
                color: AppColors.primary900,
              ),
            ),
            const SizedBox(height: 16),

            GridView.count(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              crossAxisCount: 2,
              mainAxisSpacing: 8,
              crossAxisSpacing: 8,
              childAspectRatio: 3,
              children: [
                _buildColorSwatch('50', AppColors.primary50),
                _buildColorSwatch('100', AppColors.primary100),
                _buildColorSwatch('200', AppColors.primary200),
                _buildColorSwatch('300', AppColors.primary300),
                _buildColorSwatch('400', AppColors.primary400),
                _buildColorSwatch('500', AppColors.primary500),
                _buildColorSwatch('600', AppColors.primary600),
                _buildColorSwatch('700', AppColors.primary700),
                _buildColorSwatch('800', AppColors.primary800),
                _buildColorSwatch('900', AppColors.primary900),
                _buildColorSwatch('950', AppColors.primary950),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildColorSwatch(String shade, Color color) {
    final isLight = [AppColors.primary50, AppColors.primary100, AppColors.primary200].contains(color);
    return Container(
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: AppColors.primary200),
      ),
      child: Center(
        child: Text(
          shade,
          style: TextStyle(
            color: isLight ? AppColors.primary900 : Colors.white,
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
    );
  }
}