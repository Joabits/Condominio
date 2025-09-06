'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import { 
  Building2, 
  Users, 
  Shield, 
  CreditCard, 
  Calendar,
  Wrench,
  User,
  Settings,
  LogOut,
  Menu,
  X,
  Home,
  Bell
} from 'lucide-react';

export default function Navigation() {
  const [isOpen, setIsOpen] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);
  const pathname = usePathname();
  const router = useRouter();
  const { user, logout, isLoading } = useAuth();

  const handleLogout = async () => {
    try {
      setShowUserMenu(false);
      await logout();
      router.push('/login');
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
      // Aunque falle, redirigir al login
      router.push('/login');
    }
  };

  const navigationItems = [
    {
      name: 'Dashboard',
      href: '/',
      icon: Home,
      description: 'Vista general'
    },
    {
      name: 'Residentes',
      href: '/residents',
      icon: Users,
      description: 'Gestión de residentes'
    },
    {
      name: 'Seguridad',
      href: '/security',
      icon: Shield,
      description: 'Control de acceso y cámaras'
    },
    {
      name: 'Finanzas',
      href: '/finance',
      icon: CreditCard,
      description: 'Pagos y facturación'
    },
    {
      name: 'Áreas Comunes',
      href: '/areas',
      icon: Calendar,
      description: 'Reservas y disponibilidad'
    },
    {
      name: 'Mantenimiento',
      href: '/maintenance',
      icon: Wrench,
      description: 'Solicitudes y programación'
    }
  ];

  const defaultUser = {
    name: 'Usuario',
    email: 'usuario@condominio.com',
    role: 'Usuario',
    avatar: undefined
  };

  const currentUser = user ? {
    name: [user.first_name, user.last_name].filter(Boolean).join(' ') 
      || user?.email 
      || 'Usuario',
    email: user.email || 'usuario@condominio.com',
    role: user.perfil?.tipo_usuario?.descripcion || 'Usuario',
    avatar: undefined
  } : defaultUser;

  const isActive = (href: string) => {
    return pathname === href;
  };

  return (
    <>
      {/* Mobile menu overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 z-20 bg-black bg-opacity-50 lg:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Header */}
      <header className="bg-primary-950 shadow-sm border-b border-primary-900 relative z-30">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex items-center">
              <button
                onClick={() => setIsOpen(!isOpen)}
                className="lg:hidden p-2 rounded-md text-primary-300 hover:text-primary-100 hover:bg-primary-900"
              >
                {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
              </button>
              <Building2 className="h-8 w-8 text-primary-400 ml-2 lg:ml-0" />
              <h1 className="ml-3 text-xl font-bold text-primary-100">
                Condominio Buganvillas
              </h1>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden lg:flex space-x-8">
              {navigationItems.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className={`flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                    isActive(item.href)
                      ? 'text-primary-300 bg-primary-800'
                      : 'text-primary-200 hover:text-primary-100 hover:bg-primary-900'
                  }`}
                >
                  <item.icon className="h-4 w-4 mr-2" />
                  {item.name}
                </Link>
              ))}
            </nav>

            {/* User Menu */}
            <div className="relative">
              <button
                onClick={() => setShowUserMenu(!showUserMenu)}
                className="flex items-center space-x-3 p-2 rounded-md hover:bg-primary-900"
              >
                <div className="w-8 h-8 bg-primary-500 rounded-full flex items-center justify-center">
                  {currentUser.avatar ? (
                    <img src={currentUser.avatar} alt="Avatar" className="w-8 h-8 rounded-full" />
                  ) : (
                    <User className="h-4 w-4 text-white" />
                  )}
                </div>
                <div className="hidden md:block text-left">
                  <p className="text-sm font-medium text-primary-100">{currentUser.name}</p>
                  <p className="text-xs text-primary-300">{currentUser.role}</p>
                </div>
              </button>

              {/* User Dropdown */}
              {showUserMenu && (
                <div className="absolute right-0 mt-2 w-56 bg-white rounded-md shadow-lg ring-1 ring-black ring-opacity-5 z-50">
                  <div className="py-1">
                    <div className="px-4 py-3 border-b border-gray-100">
                      <p className="text-sm font-medium text-gray-900">{currentUser.name}</p>
                      <p className="text-sm text-gray-500">{currentUser.email}</p>
                    </div>
                    <Link
                      href="/profile"
                      className="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-primary-50"
                      onClick={() => setShowUserMenu(false)}
                    >
                      <User className="h-4 w-4 mr-3" />
                      Mi Perfil
                    </Link>
                    <Link
                      href="/settings"
                      className="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      onClick={() => setShowUserMenu(false)}
                    >
                      <Settings className="h-4 w-4 mr-3" />
                      Configuración
                    </Link>
                    <Link
                      href="/notifications"
                      className="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      onClick={() => setShowUserMenu(false)}
                    >
                      <Bell className="h-4 w-4 mr-3" />
                      Notificaciones
                    </Link>
                    <div className="border-t border-gray-100">
                      <button
                        className="flex items-center w-full px-4 py-2 text-sm text-red-700 hover:bg-red-50 disabled:opacity-50"
                        onClick={handleLogout}
                        disabled={isLoading}
                      >
                        <LogOut className="h-4 w-4 mr-3" />
                        {isLoading ? 'Cerrando sesión...' : 'Cerrar Sesión'}
                      </button>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Mobile Navigation Sidebar */}
      <div className={`fixed inset-y-0 left-0 z-50 w-64 bg-primary-950 shadow-lg transform transition-transform duration-300 ease-in-out lg:hidden ${
        isOpen ? 'translate-x-0' : '-translate-x-full'
      }`}>
        <div className="flex items-center justify-between h-16 px-4 border-b border-primary-900">
          <div className="flex items-center">
            <Building2 className="h-6 w-6 text-primary-400" />
            <span className="ml-2 text-lg font-semibold text-primary-100">Buganvillas</span>
          </div>
          <button
            onClick={() => setIsOpen(false)}
            className="p-2 rounded-md text-primary-300 hover:text-primary-100 hover:bg-primary-900"
          >
            <X className="h-5 w-5" />
          </button>
        </div>
        
        <nav className="mt-6 px-4">
          <div className="space-y-2">
            {navigationItems.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                onClick={() => setIsOpen(false)}
                className={`flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                  isActive(item.href)
                    ? 'text-primary-300 bg-primary-800'
                    : 'text-primary-200 hover:text-primary-100 hover:bg-primary-900'
                }`}
              >
                <item.icon className="h-5 w-5 mr-3" />
                <div>
                  <div>{item.name}</div>
                  <div className="text-xs text-primary-400">{item.description}</div>
                </div>
              </Link>
            ))}
          </div>
        </nav>

        {/* Mobile User Info */}
        <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-primary-900">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-primary-500 rounded-full flex items-center justify-center">
              <User className="h-5 w-5 text-white" />
            </div>
            <div>
              <p className="text-sm font-medium text-primary-100">{currentUser.name}</p>
              <p className="text-xs text-primary-300">{currentUser.role}</p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}