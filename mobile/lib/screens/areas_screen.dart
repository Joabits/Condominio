import 'package:flutter/material.dart';

class AreasScreen extends StatefulWidget {
  const AreasScreen({super.key});

  @override
  State<AreasScreen> createState() => _AreasScreenState();
}

class _AreasScreenState extends State<AreasScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Áreas Comunes'),
        actions: [
          IconButton(
            icon: const Icon(Icons.calendar_today),
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Calendario próximamente')),
              );
            },
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: () async {
          await Future.delayed(const Duration(seconds: 1));
        },
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Mis reservas activas
              Text(
                'Mis Reservas',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              
              _buildReservationCard(
                'Salón de Eventos',
                'Sábado 20 Enero, 18:00 - 22:00',
                'Confirmada',
                Colors.green,
                'assets/images/salon.jpg',
              ),
              const SizedBox(height: 12),
              _buildReservationCard(
                'Piscina',
                'Domingo 21 Enero, 10:00 - 12:00',
                'Pendiente pago',
                Colors.orange,
                'assets/images/piscina.jpg',
              ),
              
              const SizedBox(height: 24),
              
              // Áreas disponibles
              Text(
                'Áreas Disponibles',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              
              _buildAreaCard(
                'Salón de Eventos',
                'Capacidad: 50 personas',
                '\$25/hora',
                'Disponible',
                Colors.green,
                Icons.celebration,
                ['Audio', 'Proyector', 'Cocina', 'A/C'],
              ),
              const SizedBox(height: 12),
              _buildAreaCard(
                'Gimnasio',
                'Capacidad: 15 personas',
                '\$5/hora',
                'Disponible',
                Colors.green,
                Icons.fitness_center,
                ['Máquinas', 'Pesas', 'Espejos', 'A/C'],
              ),
              const SizedBox(height: 12),
              _buildAreaCard(
                'Piscina',
                'Capacidad: 20 personas',
                '\$8/hora',
                'Ocupada',
                Colors.red,
                Icons.pool,
                ['Climatizada', 'Duchas', 'Tumbonas'],
              ),
              const SizedBox(height: 12),
              _buildAreaCard(
                'Terraza BBQ',
                'Capacidad: 25 personas',
                '\$12/hora',
                'Disponible',
                Colors.green,
                Icons.outdoor_grill,
                ['Parrillas', 'Mesas', 'Iluminación'],
              ),
              const SizedBox(height: 12),
              _buildAreaCard(
                'Sala de Juegos',
                'Capacidad: 12 personas',
                '\$6/hora',
                'Mantenimiento',
                Colors.grey,
                Icons.sports_esports,
                ['Consolas', 'TV', 'Juegos Mesa'],
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _showQuickReservation(context),
        child: const Icon(Icons.add),
      ),
    );
  }

  Widget _buildReservationCard(
    String title,
    String datetime,
    String status,
    Color statusColor,
    String imagePath,
  ) {
    return Card(
      child: Column(
        children: [
          Container(
            height: 120,
            width: double.infinity,
            decoration: BoxDecoration(
              color: Colors.grey.shade200,
              borderRadius: const BorderRadius.only(
                topLeft: Radius.circular(12),
                topRight: Radius.circular(12),
              ),
            ),
            child: Icon(
              Icons.image,
              size: 40,
              color: Colors.grey.shade400,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        title,
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 4,
                      ),
                      decoration: BoxDecoration(
                        color: statusColor.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(
                        status,
                        style: TextStyle(
                          color: statusColor,
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Row(
                  children: [
                    Icon(Icons.schedule, size: 16, color: Colors.grey.shade600),
                    const SizedBox(width: 4),
                    Text(
                      datetime,
                      style: TextStyle(
                        color: Colors.grey.shade600,
                        fontSize: 14,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: OutlinedButton(
                        onPressed: () => _showReservationDetails(context, title),
                        child: const Text('Ver Detalles'),
                      ),
                    ),
                    const SizedBox(width: 8),
                    if (status == 'Pendiente pago')
                      Expanded(
                        child: ElevatedButton(
                          onPressed: () => _processPayment(context),
                          child: const Text('Pagar'),
                        ),
                      ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildAreaCard(
    String title,
    String subtitle,
    String price,
    String status,
    Color statusColor,
    IconData icon,
    List<String> amenities,
  ) {
    bool isAvailable = status == 'Disponible';
    
    return Card(
      child: ListTile(
        leading: Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: statusColor.withOpacity(0.1),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Icon(icon, color: statusColor, size: 24),
        ),
        title: Text(
          title,
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(subtitle),
            const SizedBox(height: 4),
            Wrap(
              spacing: 4,
              children: amenities.take(3).map((amenity) => Chip(
                label: Text(amenity),
                materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                labelStyle: const TextStyle(fontSize: 10),
                visualDensity: VisualDensity.compact,
              )).toList(),
            ),
          ],
        ),
        trailing: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            Text(
              price,
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 16,
              ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
              decoration: BoxDecoration(
                color: statusColor.withOpacity(0.1),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Text(
                status,
                style: TextStyle(
                  color: statusColor,
                  fontSize: 10,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ],
        ),
        onTap: isAvailable ? () => _showReservationForm(context, title) : null,
      ),
    );
  }

  void _showQuickReservation(BuildContext context) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      builder: (BuildContext context) {
        return DraggableScrollableSheet(
          initialChildSize: 0.6,
          maxChildSize: 0.9,
          minChildSize: 0.3,
          builder: (context, scrollController) {
            return Container(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  Container(
                    width: 40,
                    height: 4,
                    decoration: BoxDecoration(
                      color: Colors.grey.shade300,
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                  const SizedBox(height: 16),
                  const Text(
                    'Reserva Rápida',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 16),
                  Expanded(
                    child: ListView(
                      controller: scrollController,
                      children: [
                        _buildQuickReservationOption(
                          'Gimnasio',
                          'Disponible ahora',
                          Icons.fitness_center,
                          Colors.blue,
                        ),
                        _buildQuickReservationOption(
                          'Salón de Eventos',
                          'Disponible mañana',
                          Icons.celebration,
                          Colors.purple,
                        ),
                        _buildQuickReservationOption(
                          'Terraza BBQ',
                          'Disponible fin de semana',
                          Icons.outdoor_grill,
                          Colors.orange,
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }

  Widget _buildQuickReservationOption(
    String title,
    String availability,
    IconData icon,
    Color color,
  ) {
    return Card(
      child: ListTile(
        leading: Container(
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Icon(icon, color: color),
        ),
        title: Text(title),
        subtitle: Text(availability),
        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
        onTap: () {
          Navigator.of(context).pop();
          _showReservationForm(context, title);
        },
      ),
    );
  }

  void _showReservationForm(BuildContext context, String areaName) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Reservar $areaName'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextFormField(
                decoration: const InputDecoration(
                  labelText: 'Fecha',
                  prefixIcon: Icon(Icons.calendar_today),
                ),
                readOnly: true,
                onTap: () async {
                  // TODO: Implementar selector de fecha
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                decoration: const InputDecoration(
                  labelText: 'Hora de inicio',
                  prefixIcon: Icon(Icons.schedule),
                ),
                readOnly: true,
                onTap: () async {
                  // TODO: Implementar selector de hora
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                decoration: const InputDecoration(
                  labelText: 'Duración (horas)',
                  prefixIcon: Icon(Icons.timer),
                ),
                keyboardType: TextInputType.number,
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancelar'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text('Reserva de $areaName procesada'),
                    backgroundColor: Colors.green,
                  ),
                );
              },
              child: const Text('Reservar'),
            ),
          ],
        );
      },
    );
  }

  void _showReservationDetails(BuildContext context, String areaName) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Detalles de $areaName próximamente')),
    );
  }

  void _processPayment(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Procesando pago...'),
        backgroundColor: Colors.green,
      ),
    );
  }
}