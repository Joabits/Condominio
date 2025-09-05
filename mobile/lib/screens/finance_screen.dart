import 'package:flutter/material.dart';

class FinanceScreen extends StatefulWidget {
  const FinanceScreen({super.key});

  @override
  State<FinanceScreen> createState() => _FinanceScreenState();
}

class _FinanceScreenState extends State<FinanceScreen> {
  bool _showBalance = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Finanzas'),
        actions: [
          IconButton(
            icon: Icon(_showBalance ? Icons.visibility_off : Icons.visibility),
            onPressed: () {
              setState(() {
                _showBalance = !_showBalance;
              });
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
              // Resumen financiero
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      Colors.green.shade600,
                      Colors.green.shade400,
                    ],
                  ),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Balance Actual',
                      style: TextStyle(
                        color: Colors.white70,
                        fontSize: 16,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      _showBalance ? '\$2,450.00' : '••••••',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 32,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 16),
                    Row(
                      children: [
                        _buildBalanceItem('Pagado', '\$1,200', Icons.check_circle),
                        const SizedBox(width: 24),
                        _buildBalanceItem('Pendiente', '\$350', Icons.schedule),
                      ],
                    ),
                  ],
                ),
              ),
              
              const SizedBox(height: 24),
              
              // Acciones rápidas
              Row(
                children: [
                  Expanded(
                    child: _buildActionButton(
                      'Pagar Ahora',
                      Icons.payment,
                      Colors.blue,
                      () => _showPaymentDialog(context),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: _buildActionButton(
                      'Historial',
                      Icons.history,
                      Colors.grey.shade600,
                      () => _showPaymentHistory(context),
                    ),
                  ),
                ],
              ),
              
              const SizedBox(height: 24),
              
              // Próximos pagos
              Text(
                'Próximos Pagos',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              
              _buildPaymentCard(
                'Cuota de Mantenimiento',
                'Febrero 2024',
                '\$350.00',
                'Vence en 5 días',
                Colors.orange,
                isPending: true,
              ),
              const SizedBox(height: 12),
              _buildPaymentCard(
                'Gastos Extraordinarios',
                'Reparación ascensor',
                '\$125.00',
                'Vence en 15 días',
                Colors.blue,
                isPending: true,
              ),
              
              const SizedBox(height: 24),
              
              // Pagos recientes
              Text(
                'Pagos Recientes',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              
              _buildPaymentCard(
                'Cuota de Mantenimiento',
                'Enero 2024',
                '\$350.00',
                'Pagado el 15/01/2024',
                Colors.green,
                isPending: false,
              ),
              const SizedBox(height: 12),
              _buildPaymentCard(
                'Servicio de Limpieza',
                'Enero 2024',
                '\$75.00',
                'Pagado el 10/01/2024',
                Colors.green,
                isPending: false,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildBalanceItem(String title, String amount, IconData icon) {
    return Row(
      children: [
        Icon(icon, color: Colors.white, size: 16),
        const SizedBox(width: 8),
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: const TextStyle(
                color: Colors.white70,
                fontSize: 12,
              ),
            ),
            Text(
              _showBalance ? amount : '••••',
              style: const TextStyle(
                color: Colors.white,
                fontSize: 16,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildActionButton(
    String title,
    IconData icon,
    Color color,
    VoidCallback onTap,
  ) {
    return ElevatedButton(
      onPressed: onTap,
      style: ElevatedButton.styleFrom(
        backgroundColor: color,
        foregroundColor: Colors.white,
        padding: const EdgeInsets.symmetric(vertical: 16),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 20),
          const SizedBox(width: 8),
          Text(title),
        ],
      ),
    );
  }

  Widget _buildPaymentCard(
    String title,
    String subtitle,
    String amount,
    String status,
    Color statusColor, {
    required bool isPending,
  }) {
    return Card(
      child: ListTile(
        leading: Container(
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: statusColor.withOpacity(0.1),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Icon(
            isPending ? Icons.schedule : Icons.check_circle,
            color: statusColor,
            size: 20,
          ),
        ),
        title: Text(
          title,
          style: const TextStyle(fontWeight: FontWeight.w600),
        ),
        subtitle: Text(subtitle),
        trailing: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            Text(
              amount,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 16,
                color: isPending ? Colors.orange : Colors.green,
              ),
            ),
            Text(
              status,
              style: TextStyle(
                color: statusColor,
                fontSize: 12,
              ),
            ),
          ],
        ),
        onTap: isPending ? () => _showPaymentDialog(context) : null,
      ),
    );
  }

  void _showPaymentDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Realizar Pago'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text('Selecciona el método de pago:'),
              const SizedBox(height: 16),
              ListTile(
                leading: const Icon(Icons.credit_card),
                title: const Text('Tarjeta de Crédito'),
                onTap: () {
                  Navigator.of(context).pop();
                  _processPayment('Tarjeta de Crédito');
                },
              ),
              ListTile(
                leading: const Icon(Icons.account_balance),
                title: const Text('Transferencia Bancaria'),
                onTap: () {
                  Navigator.of(context).pop();
                  _processPayment('Transferencia Bancaria');
                },
              ),
              ListTile(
                leading: const Icon(Icons.qr_code),
                title: const Text('Código QR'),
                onTap: () {
                  Navigator.of(context).pop();
                  _processPayment('Código QR');
                },
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancelar'),
            ),
          ],
        );
      },
    );
  }

  void _processPayment(String method) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Procesando pago con $method...'),
        backgroundColor: Colors.green,
      ),
    );
  }

  void _showPaymentHistory(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Historial de pagos próximamente'),
      ),
    );
  }
}