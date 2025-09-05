import 'package:flutter/material.dart';

class NotificationsScreen extends StatefulWidget {
  const NotificationsScreen({super.key});

  @override
  State<NotificationsScreen> createState() => _NotificationsScreenState();
}

class _NotificationsScreenState extends State<NotificationsScreen> {
  int _selectedTab = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Comunicados'),
        actions: [
          IconButton(
            icon: const Icon(Icons.mark_email_read),
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Marcar todo como leído')),
              );
            },
          ),
        ],
      ),
      body: Column(
        children: [
          // Tabs
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: Row(
              children: [
                Expanded(
                  child: _buildTabButton('Avisos', 0, Icons.announcement),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: _buildTabButton('Alertas', 1, Icons.warning),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: _buildTabButton('Emergencias', 2, Icons.emergency),
                ),
              ],
            ),
          ),
          
          const SizedBox(height: 16),
          
          // Content
          Expanded(
            child: _selectedTab == 0
                ? _buildAnnouncementsList()
                : _selectedTab == 1
                    ? _buildAlertsList()
                    : _buildEmergenciesList(),
          ),
        ],
      ),
    );
  }

  Widget _buildTabButton(String title, int index, IconData icon) {
    bool isSelected = _selectedTab == index;
    return GestureDetector(
      onTap: () {
        setState(() {
          _selectedTab = index;
        });
      },
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: BoxDecoration(
          color: isSelected
              ? Theme.of(context).colorScheme.primary
              : Colors.grey.shade200,
          borderRadius: BorderRadius.circular(12),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              icon,
              size: 16,
              color: isSelected ? Colors.white : Colors.grey.shade600,
            ),
            const SizedBox(width: 4),
            Text(
              title,
              style: TextStyle(
                color: isSelected ? Colors.white : Colors.grey.shade600,
                fontWeight: FontWeight.w600,
                fontSize: 12,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildAnnouncementsList() {
    return RefreshIndicator(
      onRefresh: () async {
        await Future.delayed(const Duration(seconds: 1));
      },
      child: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        children: [
          _buildAnnouncementCard(
            'Mantenimiento de Ascensores',
            'Se realizará mantenimiento preventivo de los ascensores el sábado 20 de enero de 8:00 AM a 2:00 PM. Durante este tiempo, los ascensores no estarán disponibles.',
            'Administración',
            'Hace 2 horas',
            Icons.elevator,
            Colors.orange,
            isNew: true,
          ),
          const SizedBox(height: 12),
          _buildAnnouncementCard(
            'Reunión de Propietarios',
            'Se convoca a reunión ordinaria de propietarios para el día 25 de enero a las 7:00 PM en el salón de eventos.',
            'Junta Directiva',
            'Ayer',
            Icons.people,
            Colors.blue,
            isNew: false,
          ),
          const SizedBox(height: 12),
          _buildAnnouncementCard(
            'Nuevas Medidas de Seguridad',
            'A partir del 1 de febrero se implementarán nuevas medidas de seguridad con reconocimiento facial en el acceso principal.',
            'Seguridad',
            'Hace 3 días',
            Icons.security,
            Colors.green,
            isNew: false,
          ),
          const SizedBox(height: 12),
          _buildAnnouncementCard(
            'Horarios de Piscina',
            'Los nuevos horarios de la piscina serán de 6:00 AM a 10:00 PM de lunes a domingo.',
            'Administración',
            'Hace 1 semana',
            Icons.pool,
            Colors.cyan,
            isNew: false,
          ),
        ],
      ),
    );
  }

  Widget _buildAlertsList() {
    return RefreshIndicator(
      onRefresh: () async {
        await Future.delayed(const Duration(seconds: 1));
      },
      child: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        children: [
          _buildAlertCard(
            'Visitante No Registrado',
            'El sistema de IA detectó una persona no registrada en el área de la piscina.',
            'Hace 30 min',
            Colors.red,
            Icons.person_off,
            isHigh: true,
          ),
          const SizedBox(height: 12),
          _buildAlertCard(
            'Vehículo Mal Estacionado',
            'Vehículo placa ABC-123 estacionado en zona de emergencia.',
            'Hace 2 horas',
            Colors.orange,
            Icons.local_parking,
            isHigh: false,
          ),
          const SizedBox(height: 12),
          _buildAlertCard(
            'Puerta de Acceso Abierta',
            'La puerta del área de servicios ha permanecido abierta por más de 15 minutos.',
            'Hace 4 horas',
            Colors.yellow.shade700,
            Icons.door_front_door,
            isHigh: false,
          ),
          const SizedBox(height: 12),
          _buildAlertCard(
            'Actividad Inusual',
            'Movimiento detectado en el área de juegos después del horario permitido.',
            'Ayer',
            Colors.purple,
            Icons.visibility,
            isHigh: false,
          ),
        ],
      ),
    );
  }

  Widget _buildEmergenciesList() {
    return RefreshIndicator(
      onRefresh: () async {
        await Future.delayed(const Duration(seconds: 1));
      },
      child: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        children: [
          _buildEmergencyCard(
            'Sistema de Emergencia Activado',
            'Se activó el botón de emergencia en el apartamento 304. Personal de seguridad fue notificado.',
            'Hace 1 día',
            Colors.red,
            Icons.emergency,
            status: 'Resuelto',
          ),
          const SizedBox(height: 12),
          _buildEmergencyCard(
            'Corte de Energía Sector B',
            'Falla eléctrica en el sector B del edificio. Se contactó a la empresa eléctrica.',
            'Hace 3 días',
            Colors.orange,
            Icons.power_off,
            status: 'Resuelto',
          ),
          const SizedBox(height: 12),
          _buildEmergencyCard(
            'Fuga de Agua Principal',
            'Fuga detectada en la tubería principal. Servicio de agua temporalmente suspendido.',
            'Hace 1 semana',
            Colors.blue,
            Icons.water_drop,
            status: 'Resuelto',
          ),
        ],
      ),
    );
  }

  Widget _buildAnnouncementCard(
    String title,
    String content,
    String author,
    String time,
    IconData icon,
    Color color, {
    required bool isNew,
  }) {
    return Card(
      elevation: isNew ? 4 : 2,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          border: isNew
              ? Border.all(color: Theme.of(context).colorScheme.primary, width: 2)
              : null,
        ),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: color.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Icon(icon, color: color, size: 20),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Expanded(
                              child: Text(
                                title,
                                style: const TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 16,
                                ),
                              ),
                            ),
                            if (isNew)
                              Container(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 8,
                                  vertical: 2,
                                ),
                                decoration: BoxDecoration(
                                  color: Colors.red,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: const Text(
                                  'NUEVO',
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 10,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                          ],
                        ),
                        Text(
                          '$author • $time',
                          style: TextStyle(
                            color: Colors.grey.shade600,
                            fontSize: 12,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              Text(
                content,
                style: const TextStyle(fontSize: 14, height: 1.4),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildAlertCard(
    String title,
    String content,
    String time,
    Color color,
    IconData icon, {
    required bool isHigh,
  }) {
    return Card(
      elevation: isHigh ? 4 : 2,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          border: isHigh
              ? Border.all(color: Colors.red, width: 2)
              : null,
        ),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: color.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Icon(icon, color: color, size: 20),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Expanded(
                          child: Text(
                            title,
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 14,
                            ),
                          ),
                        ),
                        if (isHigh)
                          const Icon(
                            Icons.priority_high,
                            color: Colors.red,
                            size: 20,
                          ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Text(
                      content,
                      style: const TextStyle(fontSize: 12),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      time,
                      style: TextStyle(
                        color: Colors.grey.shade600,
                        fontSize: 10,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmergencyCard(
    String title,
    String content,
    String time,
    Color color,
    IconData icon, {
    required String status,
  }) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: color.withOpacity(0.1),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Icon(icon, color: color, size: 20),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: Text(
                          title,
                          style: const TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 14,
                          ),
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 2,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.green.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          status,
                          style: const TextStyle(
                            color: Colors.green,
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Text(
                    content,
                    style: const TextStyle(fontSize: 12),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    time,
                    style: TextStyle(
                      color: Colors.grey.shade600,
                      fontSize: 10,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}