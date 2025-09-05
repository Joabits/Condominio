import 'package:flutter/material.dart';
import 'login_screen.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mi Perfil'),
        actions: [
          IconButton(
            icon: const Icon(Icons.edit),
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Editar perfil próximamente')),
              );
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // Información del usuario
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [
                    Theme.of(context).colorScheme.primary,
                    Theme.of(context).colorScheme.primary.withOpacity(0.8),
                  ],
                ),
                borderRadius: BorderRadius.circular(16),
              ),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 50,
                    backgroundColor: Colors.white,
                    child: Icon(
                      Icons.person,
                      size: 60,
                      color: Theme.of(context).colorScheme.primary,
                    ),
                  ),
                  const SizedBox(height: 16),
                  const Text(
                    'Juan Carlos Pérez',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  const Text(
                    'Apartamento 205 - Torre A',
                    style: TextStyle(
                      color: Colors.white70,
                      fontSize: 16,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 4,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.green,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: const Text(
                      'PROPIETARIO',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            
            // Información de contacto
            Card(
              child: Column(
                children: [
                  _buildInfoTile(
                    Icons.email,
                    'Correo Electrónico',
                    'juan.perez@email.com',
                  ),
                  const Divider(height: 1),
                  _buildInfoTile(
                    Icons.phone,
                    'Teléfono',
                    '+591 123 456 789',
                  ),
                  const Divider(height: 1),
                  _buildInfoTile(
                    Icons.cake,
                    'Fecha de Ingreso',
                    '15 de Marzo, 2023',
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            
            // Configuraciones
            Card(
              child: Column(
                children: [
                  _buildMenuTile(
                    Icons.notifications,
                    'Notificaciones',
                    'Configurar alertas y avisos',
                    () => _showNotificationSettings(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.security,
                    'Seguridad',
                    'Contraseña y privacidad',
                    () => _showSecuritySettings(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.language,
                    'Idioma',
                    'Español',
                    () => _showLanguageSettings(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.dark_mode,
                    'Tema',
                    'Claro',
                    () => _showThemeSettings(context),
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            
            // Información adicional
            Card(
              child: Column(
                children: [
                  _buildMenuTile(
                    Icons.family_restroom,
                    'Mi Familia',
                    'Gestionar miembros familiares',
                    () => _showFamilyManagement(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.directions_car,
                    'Mis Vehículos',
                    '2 vehículos registrados',
                    () => _showVehicleManagement(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.pets,
                    'Mis Mascotas',
                    '1 mascota registrada',
                    () => _showPetManagement(context),
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            
            // Ayuda y soporte
            Card(
              child: Column(
                children: [
                  _buildMenuTile(
                    Icons.help,
                    'Ayuda y Soporte',
                    'FAQ y contacto',
                    () => _showHelp(context),
                  ),
                  const Divider(height: 1),
                  _buildMenuTile(
                    Icons.info,
                    'Acerca de',
                    'Versión 1.0.0',
                    () => _showAbout(context),
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            
            // Botón de cerrar sesión
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () => _showLogoutDialog(context),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.red,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                child: const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.logout),
                    SizedBox(width: 8),
                    Text('Cerrar Sesión'),
                  ],
                ),
              ),
            ),
            
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoTile(IconData icon, String title, String value) {
    return ListTile(
      leading: Icon(icon, color: Colors.grey.shade600),
      title: Text(
        title,
        style: TextStyle(
          color: Colors.grey.shade600,
          fontSize: 14,
        ),
      ),
      subtitle: Text(
        value,
        style: const TextStyle(
          fontWeight: FontWeight.w600,
          fontSize: 16,
        ),
      ),
    );
  }

  Widget _buildMenuTile(
    IconData icon,
    String title,
    String subtitle,
    VoidCallback onTap,
  ) {
    return ListTile(
      leading: Icon(icon, color: Colors.grey.shade600),
      title: Text(
        title,
        style: const TextStyle(fontWeight: FontWeight.w600),
      ),
      subtitle: Text(subtitle),
      trailing: const Icon(Icons.arrow_forward_ios, size: 16),
      onTap: onTap,
    );
  }

  void _showNotificationSettings(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Configuración de Notificaciones'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              SwitchListTile(
                title: const Text('Alertas de Seguridad'),
                subtitle: const Text('Recibir notificaciones de seguridad'),
                value: true,
                onChanged: (value) {},
              ),
              SwitchListTile(
                title: const Text('Avisos Administrativos'),
                subtitle: const Text('Comunicados del condominio'),
                value: true,
                onChanged: (value) {},
              ),
              SwitchListTile(
                title: const Text('Recordatorios de Pago'),
                subtitle: const Text('Vencimientos de cuotas'),
                value: false,
                onChanged: (value) {},
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cerrar'),
            ),
          ],
        );
      },
    );
  }

  void _showSecuritySettings(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Configuración de seguridad próximamente')),
    );
  }

  void _showLanguageSettings(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Configuración de idioma próximamente')),
    );
  }

  void _showThemeSettings(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Configuración de tema próximamente')),
    );
  }

  void _showFamilyManagement(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Gestión familiar próximamente')),
    );
  }

  void _showVehicleManagement(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Gestión de vehículos próximamente')),
    );
  }

  void _showPetManagement(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Gestión de mascotas próximamente')),
    );
  }

  void _showHelp(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Ayuda y soporte próximamente')),
    );
  }

  void _showAbout(BuildContext context) {
    showAboutDialog(
      context: context,
      applicationName: 'Smart Condominio',
      applicationVersion: '1.0.0',
      applicationIcon: const Icon(Icons.apartment, size: 48),
      children: [
        const Text(
          'Aplicación móvil para la gestión inteligente de condominios con tecnología de inteligencia artificial.',
        ),
      ],
    );
  }

  void _showLogoutDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Cerrar Sesión'),
          content: const Text('¿Estás seguro de que quieres cerrar sesión?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancelar'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushAndRemoveUntil(
                  MaterialPageRoute(builder: (context) => const LoginScreen()),
                  (route) => false,
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                foregroundColor: Colors.white,
              ),
              child: const Text('Cerrar Sesión'),
            ),
          ],
        );
      },
    );
  }
}