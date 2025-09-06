// services/auth.ts - Servicio de autenticación
'use client';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthUser {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  perfil: {
    id: number;
    ci: string;
    telefono: string;
    tipo_usuario: {
      tipo: string;
      descripcion: string;
    };
    condominio: {
      id: string;
      nombre: string;
    };
  };
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
  user: AuthUser;
  message: string;
}

class AuthService {
  private static instance: AuthService;
  
  static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService();
    }
    return AuthService.instance;
  }

  // Verificar si el usuario está autenticado
  isAuthenticated(): boolean {
    if (typeof window === 'undefined') return false;
    const token = localStorage.getItem('access_token');
    const user = localStorage.getItem('user');
    return !!(token && user);
  }

  // Obtener el token de acceso
  getAccessToken(): string | null {
    if (typeof window === 'undefined') return null;
    return localStorage.getItem('access_token');
  }

  // Obtener el token de refresh
  getRefreshToken(): string | null {
    if (typeof window === 'undefined') return null;
    return localStorage.getItem('refresh_token');
  }

  // Obtener el usuario actual
  getCurrentUser(): AuthUser | null {
    if (typeof window === 'undefined') return null;
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
  }

  // Guardar datos de autenticación
  private saveAuthData(data: AuthResponse): void {
    if (typeof window === 'undefined') return;
    localStorage.setItem('access_token', data.access_token);
    localStorage.setItem('refresh_token', data.refresh_token);
    localStorage.setItem('user', JSON.stringify(data.user));
    
    // También guardar en cookies para el middleware
    document.cookie = `access_token=${data.access_token}; path=/; max-age=86400; SameSite=Strict`;
  }

  // Limpiar datos de autenticación
  private clearAuthData(): void {
    if (typeof window === 'undefined') return;
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');
    
    // También limpiar cookies
    document.cookie = 'access_token=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }

  // Iniciar sesión
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    try {
      // Usar endpoint específico para aplicación web (solo administradores)
      const response = await fetch(`${API_BASE_URL}/api/auth/web/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        let errorMessage = 'Error al iniciar sesión';
        
        try {
          const errorData = await response.json();
          console.error('Error response:', errorData);
          
          // Si es un error 403 (Forbidden), redirigir a página de acceso denegado
          if (response.status === 403) {
            if (typeof window !== 'undefined') {
              window.location.href = '/access-denied';
            }
            throw new Error(errorData.error || 'Acceso denegado');
          }
          
          // Manejar diferentes tipos de errores
          if (errorData.error) {
            errorMessage = errorData.error;
          } else if (errorData.message) {
            errorMessage = errorData.message;
          } else if (errorData.non_field_errors && Array.isArray(errorData.non_field_errors)) {
            errorMessage = errorData.non_field_errors[0];
          } else if (errorData.detail) {
            errorMessage = errorData.detail;
          }
        } catch (parseError) {
          console.error('Error parsing response:', parseError);
          errorMessage = `Error del servidor (${response.status})`;
        }
        
        throw new Error(errorMessage);
      }

      const data: AuthResponse = await response.json();
      this.saveAuthData(data);
      return data;
    } catch (error) {
      console.error('Error en login:', error);
      throw error;
    }
  }

  // Cerrar sesión
  async logout(): Promise<void> {
    try {
      const refreshToken = this.getRefreshToken();
      
      if (refreshToken) {
        // Intentar invalidar el token en el servidor
        await fetch(`${API_BASE_URL}/api/auth/logout/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.getAccessToken()}`,
          },
          body: JSON.stringify({
            refresh_token: refreshToken,
          }),
        });
      }
    } catch (error) {
      console.error('Error al cerrar sesión en el servidor:', error);
      // Continúa con el logout local aunque falle el servidor
    } finally {
      // Limpiar datos locales siempre
      this.clearAuthData();
      
      // Redirigir a login
      if (typeof window !== 'undefined') {
        window.location.href = '/login';
      }
    }
  }

  // Renovar token
  async refreshAccessToken(): Promise<string | null> {
    try {
      const refreshToken = this.getRefreshToken();
      
      if (!refreshToken) {
        throw new Error('No hay refresh token disponible');
      }

      const response = await fetch(`${API_BASE_URL}/api/token/refresh/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          refresh: refreshToken,
        }),
      });

      if (!response.ok) {
        throw new Error('Error al renovar token');
      }

      const data = await response.json();
      
      if (typeof window !== 'undefined') {
        localStorage.setItem('access_token', data.access);
      }
      
      return data.access;
    } catch (error) {
      console.error('Error al renovar token:', error);
      this.logout(); // Si falla el refresh, cerrar sesión
      return null;
    }
  }

  // Hacer petición autenticada
  async authenticatedFetch(url: string, options: RequestInit = {}): Promise<Response> {
    let token = this.getAccessToken();
    
    if (!token) {
      throw new Error('No hay token de autenticación');
    }

    // Primera intento con el token actual
    let response = await fetch(url, {
      ...options,
      headers: {
        ...options.headers,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    // Si el token expiró, intentar renovarlo
    if (response.status === 401) {
      token = await this.refreshAccessToken();
      
      if (token) {
        // Reintentar con el nuevo token
        response = await fetch(url, {
          ...options,
          headers: {
            ...options.headers,
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
      }
    }

    return response;
  }
}

export default AuthService;