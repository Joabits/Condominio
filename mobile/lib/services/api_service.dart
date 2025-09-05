import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  // URL base del API - Cambiar por la IP local de tu servidor Django
  static const String baseUrl = 'http://10.0.2.2:8000'; // Para emulador Android
  // static const String baseUrl = 'http://192.168.1.3:8000'; // Para dispositivo físico  
  // static const String baseUrl = 'http://localhost:8000'; // Para web
  // static const String baseUrl = 'http://127.0.0.1:8000'; // Para iOS simulator
  
  static String? _accessToken;
  static String? _refreshToken;

  // Headers comunes
  static Map<String, String> get _headers => {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    if (_accessToken != null) 'Authorization': 'Bearer $_accessToken',
  };

  // Inicializar tokens desde SharedPreferences
  static Future<void> initializeTokens() async {
    final prefs = await SharedPreferences.getInstance();
    _accessToken = prefs.getString('access_token');
    _refreshToken = prefs.getString('refresh_token');
  }

  // Guardar tokens
  static Future<void> saveTokens(String accessToken, String refreshToken) async {
    final prefs = await SharedPreferences.getInstance();
    _accessToken = accessToken;
    _refreshToken = refreshToken;
    await prefs.setString('access_token', accessToken);
    await prefs.setString('refresh_token', refreshToken);
  }

  // Limpiar tokens
  static Future<void> clearTokens() async {
    final prefs = await SharedPreferences.getInstance();
    _accessToken = null;
    _refreshToken = null;
    await prefs.remove('access_token');
    await prefs.remove('refresh_token');
  }

  // Refresh token si es necesario
  static Future<bool> refreshAccessToken() async {
    if (_refreshToken == null) return false;

    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/token/refresh/'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'refresh': _refreshToken}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        _accessToken = data['access'];
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('access_token', _accessToken!);
        return true;
      }
    } catch (e) {
      print('Error refreshing token: $e');
    }
    return false;
  }

  // Realizar petición HTTP con manejo de errores
  static Future<http.Response?> _makeRequest(
    String method,
    String endpoint, {
    Map<String, dynamic>? body,
    bool retry = true,
  }) async {
    await initializeTokens();

    Uri url = Uri.parse('$baseUrl$endpoint');
    http.Response response;

    try {
      switch (method.toUpperCase()) {
        case 'GET':
          response = await http.get(url, headers: _headers);
          break;
        case 'POST':
          response = await http.post(
            url,
            headers: _headers,
            body: body != null ? jsonEncode(body) : null,
          );
          break;
        case 'PUT':
          response = await http.put(
            url,
            headers: _headers,
            body: body != null ? jsonEncode(body) : null,
          );
          break;
        case 'DELETE':
          response = await http.delete(url, headers: _headers);
          break;
        default:
          throw Exception('Método HTTP no soportado: $method');
      }

      // Si el token expiró, intentar refreshear
      if (response.statusCode == 401 && retry) {
        if (await refreshAccessToken()) {
          return _makeRequest(method, endpoint, body: body, retry: false);
        }
      }

      return response;
    } catch (e) {
      print('Error en petición HTTP: $e');
      return null;
    }
  }

  // =====================================
  // MÉTODOS DE AUTENTICACIÓN
  // =====================================

  static Future<Map<String, dynamic>?> login(String email, String password) async {
    final response = await _makeRequest(
      'POST',
      '/api/auth/login/',
      body: {
        'email': email,
        'password': password,
      },
      retry: false,
    );

    if (response?.statusCode == 200) {
      final data = jsonDecode(response!.body);
      await saveTokens(data['access_token'], data['refresh_token']);
      return data;
    }
    
    return null;
  }

  static Future<bool> logout() async {
    final response = await _makeRequest(
      'POST',
      '/api/auth/logout/',
      body: {'refresh_token': _refreshToken},
    );

    await clearTokens();
    return response?.statusCode == 200;
  }

  static Future<Map<String, dynamic>?> registro(Map<String, dynamic> userData) async {
    final response = await _makeRequest(
      'POST',
      '/api/auth/registro/',
      body: userData,
      retry: false,
    );

    if (response?.statusCode == 201) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // DASHBOARD
  // =====================================

  static Future<Map<String, dynamic>?> getDashboardData() async {
    final response = await _makeRequest('GET', '/api/dashboard/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  static Future<List<dynamic>?> getQuickActions() async {
    final response = await _makeRequest('GET', '/api/quick-actions/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // FINANZAS
  // =====================================

  static Future<Map<String, dynamic>?> getFinanzasData() async {
    final response = await _makeRequest('GET', '/api/finanzas/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  static Future<Map<String, dynamic>?> procesarPago(Map<String, dynamic> pagoData) async {
    final response = await _makeRequest(
      'POST',
      '/api/finanzas/pagar/',
      body: pagoData,
    );
    
    if (response?.statusCode == 201) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // ÁREAS COMUNES
  // =====================================

  static Future<Map<String, dynamic>?> getAreasData() async {
    final response = await _makeRequest('GET', '/api/areas/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  static Future<Map<String, dynamic>?> crearReserva(Map<String, dynamic> reservaData) async {
    final response = await _makeRequest(
      'POST',
      '/api/areas/reservar/',
      body: reservaData,
    );
    
    if (response?.statusCode == 201) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // NOTIFICACIONES
  // =====================================

  static Future<Map<String, dynamic>?> getNotificaciones() async {
    final response = await _makeRequest('GET', '/api/notificaciones/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // PERFIL
  // =====================================

  static Future<Map<String, dynamic>?> getPerfilData() async {
    final response = await _makeRequest('GET', '/api/perfil/');
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  static Future<Map<String, dynamic>?> actualizarPerfil(Map<String, dynamic> perfilData) async {
    final response = await _makeRequest(
      'PUT',
      '/api/perfil/',
      body: perfilData,
    );
    
    if (response?.statusCode == 200) {
      return jsonDecode(response!.body);
    }
    
    return null;
  }

  // =====================================
  // UTILIDADES
  // =====================================

  static bool isLoggedIn() {
    return _accessToken != null;
  }

  static Future<bool> checkConnection() async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/api/dashboard/'),
        headers: _headers,
      ).timeout(const Duration(seconds: 5));
      
      return response.statusCode == 200 || response.statusCode == 401;
    } catch (e) {
      return false;
    }
  }
}