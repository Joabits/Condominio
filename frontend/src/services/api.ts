// services/api.ts - Servicio para conectar Next.js con Django Backend

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

// Tipos TypeScript
export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

export interface PerfilUsuario {
  id: number;
  user: User;
  condominio: Condominio;
  tipo_usuario: TipoUsuario;
  ci: string;
  telefono: string;
  activo: boolean;
}

export interface Condominio {
  id: string;
  nombre: string;
  direccion: string;
  telefono: string;
  email: string;
  ciudad: string;
  pais: string;
}

export interface TipoUsuario {
  id: number;
  tipo: string;
  descripcion: string;
}

export interface Unidad {
  id: string;
  numero: string;
  piso: number;
  bloque: string;
  metros_cuadrados: number;
  dormitorios: number;
  baños: number;
  activa: boolean;
  tipo_unidad: TipoUnidad;
}

export interface TipoUnidad {
  id: number;
  nombre: string;
  factor_costo: number;
}

export interface AreaComun {
  id: number;
  nombre: string;
  descripcion: string;
  capacidad_maxima: number;
  precio_por_hora: number;
  hora_apertura: string;
  hora_cierre: string;
  dias_disponibles: string[];
  activa: boolean;
}

export interface CamaraSeguridad {
  id: number;
  nombre: string;
  ubicacion: string;
  ip_address: string;
  reconocimiento_facial: boolean;
  deteccion_vehiculos: boolean;
  deteccion_anomalias: boolean;
  activa: boolean;
}

export interface AlertaSeguridad {
  id: number;
  tipo_alerta: string;
  nivel: string;
  descripcion: string;
  fecha_hora: string;
  confianza_deteccion: number;
  revisada: boolean;
  camara: CamaraSeguridad;
}

export interface RegistroAcceso {
  id: number;
  tipo_acceso: string;
  metodo_identificacion: string;
  fecha_hora: string;
  confianza_ia: number;
  autorizado: boolean;
  usuario?: PerfilUsuario;
}

export interface CuotaMantenimiento {
  id: number;
  monto_total: number;
  monto_pagado: number;
  monto_pendiente: number;
  estado: string;
  fecha_vencimiento: string;
  unidad: Unidad;
}

// Clase principal del servicio API
class ApiService {
  private baseURL: string;
  private token: string | null = null;

  constructor() {
    this.baseURL = API_BASE_URL;
    // Intentar obtener token del localStorage
    if (typeof window !== 'undefined') {
      this.token = localStorage.getItem('access_token');
    }
  }

  // Configurar headers
  private getHeaders(): HeadersInit {
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    };

    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }

    return headers;
  }

  // Método para manejar respuestas
  private async handleResponse<T>(response: Response): Promise<T> {
    if (!response.ok) {
      if (response.status === 401) {
        // Token expirado, limpiar y redirigir
        this.token = null;
        if (typeof window !== 'undefined') {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login';
        }
      }
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      return response.json();
    }
    
    return response.text() as any;
  }

  // Autenticación
  async login(email: string, password: string): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/auth/login/`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify({ email, password }),
    });

    const data = await this.handleResponse<any>(response);
    
    if (data.access_token) {
      this.token = data.access_token;
      if (typeof window !== 'undefined') {
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('refresh_token', data.refresh_token);
      }
    }

    return data;
  }

  // Dashboard
  async getDashboardData(): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/dashboard/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  // Usuarios y Residentes
  async getUsuarios(): Promise<PerfilUsuario[]> {
    try {
      const response = await fetch(`${this.baseURL}/api/usuarios/`, {
        headers: this.getHeaders(),
      });
      const data = await this.handleResponse(response);
      // Asegurar que siempre retorne un array
      return Array.isArray(data) ? data : [];
    } catch (error) {
      console.error('Error fetching usuarios:', error);
      return [];
    }
  }

  async createUsuario(userData: Partial<PerfilUsuario>): Promise<PerfilUsuario> {
    const response = await fetch(`${this.baseURL}/api/usuarios/`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(userData),
    });
    return this.handleResponse(response);
  }

  async updateUsuario(id: number, userData: Partial<PerfilUsuario>): Promise<PerfilUsuario> {
    const response = await fetch(`${this.baseURL}/api/usuarios/${id}/`, {
      method: 'PUT',
      headers: this.getHeaders(),
      body: JSON.stringify(userData),
    });
    return this.handleResponse(response);
  }

  async deleteUsuario(id: number): Promise<void> {
    const response = await fetch(`${this.baseURL}/api/usuarios/${id}/`, {
      method: 'DELETE',
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  // Unidades
  async getUnidades(): Promise<Unidad[]> {
    const response = await fetch(`${this.baseURL}/api/unidades/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async createUnidad(unidadData: Partial<Unidad>): Promise<Unidad> {
    const response = await fetch(`${this.baseURL}/api/unidades/`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(unidadData),
    });
    return this.handleResponse(response);
  }

  // Áreas Comunes
  async getAreasComunes(): Promise<AreaComun[]> {
    const response = await fetch(`${this.baseURL}/api/areas-comunes/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async createAreaComun(areaData: Partial<AreaComun>): Promise<AreaComun> {
    const response = await fetch(`${this.baseURL}/api/areas-comunes/`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(areaData),
    });
    return this.handleResponse(response);
  }

  async updateAreaComun(id: number, areaData: Partial<AreaComun>): Promise<AreaComun> {
    const response = await fetch(`${this.baseURL}/api/areas-comunes/${id}/`, {
      method: 'PUT',
      headers: this.getHeaders(),
      body: JSON.stringify(areaData),
    });
    return this.handleResponse(response);
  }

  // Seguridad
  async getCamaras(): Promise<CamaraSeguridad[]> {
    const response = await fetch(`${this.baseURL}/api/camaras/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async getAlertas(): Promise<AlertaSeguridad[]> {
    const response = await fetch(`${this.baseURL}/api/alertas/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async getRegistrosAcceso(): Promise<RegistroAcceso[]> {
    const response = await fetch(`${this.baseURL}/api/accesos/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async marcarAlertaRevisada(id: number): Promise<AlertaSeguridad> {
    const response = await fetch(`${this.baseURL}/api/alertas/${id}/revisar/`, {
      method: 'POST',
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  // Finanzas
  async getCuotas(): Promise<CuotaMantenimiento[]> {
    const response = await fetch(`${this.baseURL}/api/cuotas/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async getReporteFinanciero(): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/reportes/financiero/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  // Mantenimiento
  async getTareasMantenimiento(): Promise<any[]> {
    const response = await fetch(`${this.baseURL}/api/mantenimiento/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async createTareaMantenimiento(tareaData: any): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/mantenimiento/`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(tareaData),
    });
    return this.handleResponse(response);
  }

  // Estadísticas y Reportes
  async getEstadisticas(): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/estadisticas/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async getReporteSeguridad(): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/reportes/seguridad/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }

  async getReporteOcupacion(): Promise<any> {
    const response = await fetch(`${this.baseURL}/api/reportes/ocupacion/`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse(response);
  }
}

// Exportar instancia única
const apiService = new ApiService();
export default apiService;