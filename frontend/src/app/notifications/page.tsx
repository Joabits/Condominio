'use client';

import { useState, useEffect } from 'react';
import Navigation from '../../components/Navigation';
import { 
  Bell,
  Mail,
  Shield,
  CreditCard,
  Wrench,
  Users,
  AlertTriangle,
  CheckCircle,
  Clock,
  X,
  Archive,
  Mail as MarkAsUnread,
  Trash2,
  Filter,
  Search,
  Calendar,
  Eye
} from 'lucide-react';

interface Notification {
  id: number;
  type: 'security' | 'payment' | 'maintenance' | 'general' | 'emergency';
  title: string;
  message: string;
  timestamp: string;
  read: boolean;
  priority: 'high' | 'medium' | 'low';
  sender?: string;
}

export default function NotificationsPage() {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [filter, setFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedNotifications, setSelectedNotifications] = useState<number[]>([]);

  useEffect(() => {
    loadNotifications();
  }, []);

  const loadNotifications = () => {
    // Datos simulados de notificaciones
    const mockNotifications: Notification[] = [
      {
        id: 1,
        type: 'security',
        title: 'Alerta de Seguridad',
        message: 'Se detectó un vehículo no autorizado en el área de estacionamiento. Cámara 3 - Zona A.',
        timestamp: '2025-09-05T10:30:00Z',
        read: false,
        priority: 'high',
        sender: 'Sistema de Seguridad IA'
      },
      {
        id: 2,
        type: 'payment',
        title: 'Recordatorio de Pago',
        message: 'La cuota de mantenimiento del mes de septiembre vence en 3 días. Apartamento 205.',
        timestamp: '2025-09-05T09:15:00Z',
        read: false,
        priority: 'medium',
        sender: 'Sistema de Facturación'
      },
      {
        id: 3,
        type: 'maintenance',
        title: 'Mantenimiento Programado',
        message: 'El ascensor A estará fuera de servicio mañana de 8:00 AM a 12:00 PM para mantenimiento preventivo.',
        timestamp: '2025-09-04T16:45:00Z',
        read: true,
        priority: 'medium',
        sender: 'Departamento de Mantenimiento'
      },
      {
        id: 4,
        type: 'general',
        title: 'Nuevo Residente',
        message: 'Se ha registrado un nuevo residente en el apartamento 310. Juan Carlos Mendoza.',
        timestamp: '2025-09-04T14:20:00Z',
        read: true,
        priority: 'low',
        sender: 'Administración'
      },
      {
        id: 5,
        type: 'emergency',
        title: 'Corte de Agua Programado',
        message: 'Se realizará un corte de agua programado mañana de 6:00 AM a 10:00 AM en todo el edificio.',
        timestamp: '2025-09-03T18:30:00Z',
        read: false,
        priority: 'high',
        sender: 'Servicios Públicos'
      },
      {
        id: 6,
        type: 'security',
        title: 'Reconocimiento Facial',
        message: 'El sistema de reconocimiento facial identificó a un visitante frecuente. Acceso autorizado automáticamente.',
        timestamp: '2025-09-03T15:10:00Z',
        read: true,
        priority: 'low',
        sender: 'Sistema de Seguridad IA'
      },
      {
        id: 7,
        type: 'payment',
        title: 'Pago Recibido',
        message: 'Se ha registrado el pago de la cuota de mantenimiento. Apartamento 108 - $450.00.',
        timestamp: '2025-09-03T11:25:00Z',
        read: true,
        priority: 'low',
        sender: 'Sistema de Facturación'
      },
      {
        id: 8,
        type: 'maintenance',
        title: 'Solicitud de Mantenimiento',
        message: 'Nueva solicitud de mantenimiento: Problema con el aire acondicionado en apartamento 207.',
        timestamp: '2025-09-02T13:40:00Z',
        read: false,
        priority: 'medium',
        sender: 'Ana Martínez Vega'
      }
    ];
    setNotifications(mockNotifications);
  };

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'security':
        return Shield;
      case 'payment':
        return CreditCard;
      case 'maintenance':
        return Wrench;
      case 'emergency':
        return AlertTriangle;
      default:
        return Bell;
    }
  };

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'security':
        return 'text-blue-600 bg-blue-100';
      case 'payment':
        return 'text-green-600 bg-green-100';
      case 'maintenance':
        return 'text-orange-600 bg-orange-100';
      case 'emergency':
        return 'text-red-600 bg-red-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high':
        return 'border-l-red-500';
      case 'medium':
        return 'border-l-yellow-500';
      case 'low':
        return 'border-l-green-500';
      default:
        return 'border-l-gray-300';
    }
  };

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffInHours = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60));
    
    if (diffInHours < 1) {
      return 'Hace menos de 1 hora';
    } else if (diffInHours < 24) {
      return `Hace ${diffInHours} horas`;
    } else {
      return date.toLocaleDateString('es-ES', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
  };

  const markAsRead = (id: number) => {
    setNotifications(notifications.map(n => 
      n.id === id ? { ...n, read: true } : n
    ));
  };

  const markAsUnread = (id: number) => {
    setNotifications(notifications.map(n => 
      n.id === id ? { ...n, read: false } : n
    ));
  };

  const deleteNotification = (id: number) => {
    setNotifications(notifications.filter(n => n.id !== id));
  };

  const toggleSelection = (id: number) => {
    setSelectedNotifications(prev => 
      prev.includes(id) 
        ? prev.filter(nId => nId !== id)
        : [...prev, id]
    );
  };

  const markAllAsRead = () => {
    setNotifications(notifications.map(n => ({ ...n, read: true })));
  };

  const deleteSelected = () => {
    setNotifications(notifications.filter(n => !selectedNotifications.includes(n.id)));
    setSelectedNotifications([]);
  };

  const filteredNotifications = notifications.filter(notification => {
    const matchesFilter = filter === 'all' || 
                         (filter === 'unread' && !notification.read) ||
                         (filter === 'read' && notification.read) ||
                         notification.type === filter;
    
    const matchesSearch = notification.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         notification.message.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         (notification.sender && notification.sender.toLowerCase().includes(searchTerm.toLowerCase()));
    
    return matchesFilter && matchesSearch;
  });

  const unreadCount = notifications.filter(n => !n.read).length;

  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation />
      
      <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Notificaciones</h1>
              <p className="mt-2 text-gray-600">
                Gestiona todas las notificaciones y alertas del sistema
                {unreadCount > 0 && (
                  <span className="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
                    {unreadCount} sin leer
                  </span>
                )}
              </p>
            </div>
            <div className="flex space-x-2">
              <button
                onClick={markAllAsRead}
                className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
              >
                <CheckCircle className="h-4 w-4 mr-2" />
                Marcar todo como leído
              </button>
              {selectedNotifications.length > 0 && (
                <button
                  onClick={deleteSelected}
                  className="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
                >
                  <Trash2 className="h-4 w-4 mr-2" />
                  Eliminar seleccionadas ({selectedNotifications.length})
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Filters and Search */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                <input
                  type="text"
                  placeholder="Buscar notificaciones..."
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
            </div>
            <div className="flex gap-2">
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
              >
                <option value="all">Todas</option>
                <option value="unread">Sin leer</option>
                <option value="read">Leídas</option>
                <option value="security">Seguridad</option>
                <option value="payment">Pagos</option>
                <option value="maintenance">Mantenimiento</option>
                <option value="emergency">Emergencia</option>
                <option value="general">General</option>
              </select>
            </div>
          </div>
        </div>

        {/* Notifications List */}
        <div className="space-y-4">
          {filteredNotifications.length === 0 ? (
            <div className="text-center py-12 bg-white rounded-lg shadow-sm border border-gray-200">
              <Bell className="h-12 w-12 text-gray-400 mx-auto mb-4" />
              <p className="text-gray-500">No hay notificaciones que coincidan con los filtros</p>
            </div>
          ) : (
            filteredNotifications.map((notification) => {
              const TypeIcon = getTypeIcon(notification.type);
              return (
                <div
                  key={notification.id}
                  className={`bg-white rounded-lg shadow-sm border-l-4 ${getPriorityColor(notification.priority)} border-r border-t border-b border-gray-200 p-6 ${
                    !notification.read ? 'bg-blue-50' : ''
                  }`}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex items-start space-x-4 flex-1">
                      <div className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={selectedNotifications.includes(notification.id)}
                          onChange={() => toggleSelection(notification.id)}
                          className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                        />
                        <div className={`p-2 rounded-lg ${getTypeColor(notification.type)}`}>
                          <TypeIcon className="h-5 w-5" />
                        </div>
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center space-x-2 mb-1">
                          <h3 className={`text-sm font-medium ${!notification.read ? 'text-gray-900' : 'text-gray-600'}`}>
                            {notification.title}
                          </h3>
                          {!notification.read && (
                            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                          )}
                          <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${
                            notification.priority === 'high' ? 'bg-red-100 text-red-800' :
                            notification.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                            'bg-green-100 text-green-800'
                          }`}>
                            {notification.priority === 'high' ? 'Alta' : 
                             notification.priority === 'medium' ? 'Media' : 'Baja'}
                          </span>
                        </div>
                        <p className="text-sm text-gray-600 mb-2">
                          {notification.message}
                        </p>
                        <div className="flex items-center space-x-4 text-xs text-gray-500">
                          <div className="flex items-center">
                            <Clock className="h-3 w-3 mr-1" />
                            {formatTimestamp(notification.timestamp)}
                          </div>
                          {notification.sender && (
                            <div className="flex items-center">
                              <Users className="h-3 w-3 mr-1" />
                              {notification.sender}
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2 ml-4">
                      {!notification.read ? (
                        <button
                          onClick={() => markAsRead(notification.id)}
                          className="text-gray-400 hover:text-blue-600 p-1"
                          title="Marcar como leído"
                        >
                          <Eye className="h-4 w-4" />
                        </button>
                      ) : (
                        <button
                          onClick={() => markAsUnread(notification.id)}
                          className="text-gray-400 hover:text-yellow-600 p-1"
                          title="Marcar como no leído"
                        >
                          <MarkAsUnread className="h-4 w-4" />
                        </button>
                      )}
                      <button
                        onClick={() => deleteNotification(notification.id)}
                        className="text-gray-400 hover:text-red-600 p-1"
                        title="Eliminar"
                      >
                        <Trash2 className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Summary Stats */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
            <div className="flex items-center">
              <Bell className="h-8 w-8 text-blue-600" />
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-600">Total</p>
                <p className="text-lg font-semibold text-gray-900">{notifications.length}</p>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
            <div className="flex items-center">
              <MarkAsUnread className="h-8 w-8 text-red-600" />
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-600">Sin Leer</p>
                <p className="text-lg font-semibold text-gray-900">{unreadCount}</p>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
            <div className="flex items-center">
              <Shield className="h-8 w-8 text-yellow-600" />
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-600">Seguridad</p>
                <p className="text-lg font-semibold text-gray-900">
                  {notifications.filter(n => n.type === 'security').length}
                </p>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
            <div className="flex items-center">
              <AlertTriangle className="h-8 w-8 text-orange-600" />
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-600">Urgentes</p>
                <p className="text-lg font-semibold text-gray-900">
                  {notifications.filter(n => n.priority === 'high').length}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}