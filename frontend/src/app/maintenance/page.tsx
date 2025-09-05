'use client';

import { useState, useEffect } from 'react';
import { 
  Wrench, 
  Calendar, 
  Clock, 
  User, 
  MapPin, 
  AlertCircle, 
  CheckCircle, 
  XCircle,
  Plus,
  Search,
  Filter,
  FileText,
  Camera,
  MessageSquare,
  Star,
  TrendingUp,
  Settings,
  Zap,
  Droplets,
  Thermometer,
  Wifi
} from 'lucide-react';

interface MaintenanceRequest {
  id: string;
  title: string;
  description: string;
  category: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  status: 'pending' | 'in-progress' | 'completed' | 'cancelled';
  location: string;
  requestedBy: string;
  assignedTo?: string;
  createdAt: string;
  updatedAt: string;
  estimatedCompletion?: string;
  photos: number;
  rating?: number;
}

interface MaintenanceStats {
  totalRequests: number;
  pendingRequests: number;
  inProgress: number;
  completedThisMonth: number;
  averageResolutionTime: string;
  satisfactionRate: number;
}

export default function MaintenancePage() {
  const [requests, setRequests] = useState<MaintenanceRequest[]>([]);
  const [stats, setStats] = useState<MaintenanceStats>({
    totalRequests: 47,
    pendingRequests: 12,
    inProgress: 8,
    completedThisMonth: 23,
    averageResolutionTime: '2.3 días',
    satisfactionRate: 4.6
  });
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    // Simular datos de solicitudes de mantenimiento
    const mockRequests: MaintenanceRequest[] = [
      {
        id: '1',
        title: 'Fuga de agua en tubería',
        description: 'Hay una fuga en la tubería del baño principal que está causando humedad en la pared.',
        category: 'Plomería',
        priority: 'high',
        status: 'in-progress',
        location: 'Apt 205 - Baño Principal',
        requestedBy: 'María García',
        assignedTo: 'Carlos Plomero',
        createdAt: '2024-01-15T09:30:00',
        updatedAt: '2024-01-15T14:20:00',
        estimatedCompletion: '2024-01-16T16:00:00',
        photos: 3,
        rating: undefined
      },
      {
        id: '2',
        title: 'Problema eléctrico en cocina',
        description: 'Los enchufes de la cocina no están funcionando correctamente.',
        category: 'Electricidad',
        priority: 'medium',
        status: 'pending',
        location: 'Apt 308 - Cocina',
        requestedBy: 'Roberto Silva',
        createdAt: '2024-01-14T16:45:00',
        updatedAt: '2024-01-14T16:45:00',
        photos: 2
      },
      {
        id: '3',
        title: 'Mantenimiento aire acondicionado',
        description: 'El aire acondicionado necesita limpieza y revisión general.',
        category: 'HVAC',
        priority: 'low',
        status: 'completed',
        location: 'Apt 412 - Sala Principal',
        requestedBy: 'Ana Martínez',
        assignedTo: 'Técnico HVAC',
        createdAt: '2024-01-10T11:20:00',
        updatedAt: '2024-01-13T15:30:00',
        photos: 1,
        rating: 5
      },
      {
        id: '4',
        title: 'Reparación de puerta principal',
        description: 'La cerradura de la puerta principal se está atascando.',
        category: 'General',
        priority: 'medium',
        status: 'in-progress',
        location: 'Apt 101 - Entrada',
        requestedBy: 'Juan Pérez',
        assignedTo: 'Técnico General',
        createdAt: '2024-01-12T08:15:00',
        updatedAt: '2024-01-15T10:00:00',
        estimatedCompletion: '2024-01-16T12:00:00',
        photos: 0
      },
      {
        id: '5',
        title: 'Conectividad de internet intermitente',
        description: 'El internet se corta frecuentemente en las horas de la tarde.',
        category: 'Tecnología',
        priority: 'medium',
        status: 'pending',
        location: 'Apt 503 - Toda la unidad',
        requestedBy: 'Luis Rodríguez',
        createdAt: '2024-01-15T19:30:00',
        updatedAt: '2024-01-15T19:30:00',
        photos: 0
      }
    ];
    setRequests(mockRequests);
  }, []);

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'urgent':
        return 'text-red-600 bg-red-100 border-red-200';
      case 'high':
        return 'text-orange-600 bg-orange-100 border-orange-200';
      case 'medium':
        return 'text-yellow-600 bg-yellow-100 border-yellow-200';
      case 'low':
        return 'text-green-600 bg-green-100 border-green-200';
      default:
        return 'text-gray-600 bg-gray-100 border-gray-200';
    }
  };

  const getPriorityText = (priority: string) => {
    switch (priority) {
      case 'urgent':
        return 'Urgente';
      case 'high':
        return 'Alta';
      case 'medium':
        return 'Media';
      case 'low':
        return 'Baja';
      default:
        return priority;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed':
        return 'text-green-600 bg-green-100';
      case 'in-progress':
        return 'text-blue-600 bg-blue-100';
      case 'pending':
        return 'text-yellow-600 bg-yellow-100';
      case 'cancelled':
        return 'text-red-600 bg-red-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'completed':
        return 'Completado';
      case 'in-progress':
        return 'En Progreso';
      case 'pending':
        return 'Pendiente';
      case 'cancelled':
        return 'Cancelado';
      default:
        return status;
    }
  };

  const getCategoryIcon = (category: string) => {
    switch (category.toLowerCase()) {
      case 'plomería':
        return <Droplets className="h-5 w-5" />;
      case 'electricidad':
        return <Zap className="h-5 w-5" />;
      case 'hvac':
        return <Thermometer className="h-5 w-5" />;
      case 'tecnología':
        return <Wifi className="h-5 w-5" />;
      default:
        return <Settings className="h-5 w-5" />;
    }
  };

  const filteredRequests = requests.filter(request => {
    const matchesStatus = selectedFilter === 'all' || request.status === selectedFilter;
    const matchesCategory = selectedCategory === 'all' || request.category === selectedCategory;
    const matchesSearch = request.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         request.location.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         request.requestedBy.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStatus && matchesCategory && matchesSearch;
  });

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Gestión de Mantenimiento</h1>
          <p className="text-gray-600">Control de solicitudes, reparaciones y mantenimiento preventivo</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-6 mb-8">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Total Solicitudes</p>
                <p className="text-2xl font-bold text-gray-900">{stats.totalRequests}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <Wrench className="h-6 w-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Pendientes</p>
                <p className="text-2xl font-bold text-yellow-600">{stats.pendingRequests}</p>
              </div>
              <div className="bg-yellow-100 p-3 rounded-lg">
                <Clock className="h-6 w-6 text-yellow-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">En Progreso</p>
                <p className="text-2xl font-bold text-blue-600">{stats.inProgress}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <Settings className="h-6 w-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Completados</p>
                <p className="text-2xl font-bold text-green-600">{stats.completedThisMonth}</p>
              </div>
              <div className="bg-green-100 p-3 rounded-lg">
                <CheckCircle className="h-6 w-6 text-green-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Tiempo Promedio</p>
                <p className="text-2xl font-bold text-gray-900">{stats.averageResolutionTime}</p>
              </div>
              <div className="bg-purple-100 p-3 rounded-lg">
                <TrendingUp className="h-6 w-6 text-purple-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Satisfacción</p>
                <p className="text-2xl font-bold text-gray-900">{stats.satisfactionRate}/5</p>
              </div>
              <div className="bg-orange-100 p-3 rounded-lg">
                <Star className="h-6 w-6 text-orange-600" />
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap gap-4 mb-6">
          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors flex items-center">
            <Plus className="h-4 w-4 mr-2" />
            Nueva Solicitud
          </button>
          <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors flex items-center">
            <Calendar className="h-4 w-4 mr-2" />
            Programar Mantenimiento
          </button>
          <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-colors flex items-center">
            <FileText className="h-4 w-4 mr-2" />
            Generar Reporte
          </button>
        </div>

        {/* Filters and Search */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                <input
                  type="text"
                  placeholder="Buscar por título, ubicación o solicitante..."
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
            </div>
            <div className="flex gap-2">
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={selectedFilter}
                onChange={(e) => setSelectedFilter(e.target.value)}
              >
                <option value="all">Todos los estados</option>
                <option value="pending">Pendientes</option>
                <option value="in-progress">En Progreso</option>
                <option value="completed">Completados</option>
                <option value="cancelled">Cancelados</option>
              </select>
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
              >
                <option value="all">Todas las categorías</option>
                <option value="Plomería">Plomería</option>
                <option value="Electricidad">Electricidad</option>
                <option value="HVAC">HVAC</option>
                <option value="General">General</option>
                <option value="Tecnología">Tecnología</option>
              </select>
              <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center">
                <Filter className="h-4 w-4 mr-2" />
                Más Filtros
              </button>
            </div>
          </div>
        </div>

        {/* Requests List */}
        <div className="space-y-4">
          {filteredRequests.map((request) => (
            <div key={request.id} className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
              <div className="flex items-start justify-between mb-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <div className="text-gray-600">
                      {getCategoryIcon(request.category)}
                    </div>
                    <h3 className="text-lg font-semibold text-gray-900">{request.title}</h3>
                    <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full border ${getPriorityColor(request.priority)}`}>
                      {getPriorityText(request.priority)}
                    </span>
                  </div>
                  <p className="text-gray-600 mb-3">{request.description}</p>
                  <div className="flex items-center gap-4 text-sm text-gray-500">
                    <div className="flex items-center">
                      <MapPin className="h-4 w-4 mr-1" />
                      {request.location}
                    </div>
                    <div className="flex items-center">
                      <User className="h-4 w-4 mr-1" />
                      {request.requestedBy}
                    </div>
                    <div className="flex items-center">
                      <Calendar className="h-4 w-4 mr-1" />
                      {new Date(request.createdAt).toLocaleDateString()}
                    </div>
                    {request.photos > 0 && (
                      <div className="flex items-center">
                        <Camera className="h-4 w-4 mr-1" />
                        {request.photos} fotos
                      </div>
                    )}
                  </div>
                </div>
                <div className="flex flex-col items-end space-y-2">
                  <span className={`inline-flex px-3 py-1 text-sm font-semibold rounded-full ${getStatusColor(request.status)}`}>
                    {getStatusText(request.status)}
                  </span>
                  {request.rating && (
                    <div className="flex items-center">
                      <Star className="h-4 w-4 text-yellow-400 fill-current" />
                      <span className="text-sm text-gray-600 ml-1">{request.rating}/5</span>
                    </div>
                  )}
                </div>
              </div>

              {request.assignedTo && (
                <div className="bg-gray-50 rounded-lg p-3 mb-4">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center">
                      <User className="h-4 w-4 text-gray-500 mr-2" />
                      <span className="text-sm text-gray-700">Asignado a: <strong>{request.assignedTo}</strong></span>
                    </div>
                    {request.estimatedCompletion && (
                      <div className="flex items-center text-sm text-gray-600">
                        <Clock className="h-4 w-4 mr-1" />
                        Estimado: {new Date(request.estimatedCompletion).toLocaleDateString()}
                      </div>
                    )}
                  </div>
                </div>
              )}

              <div className="flex items-center justify-between pt-4 border-t border-gray-200">
                <div className="flex items-center space-x-2">
                  <span className="text-sm text-gray-500">Categoría:</span>
                  <span className="text-sm font-medium text-gray-700">{request.category}</span>
                </div>
                <div className="flex space-x-2">
                  <button className="text-blue-600 hover:text-blue-800 p-2 hover:bg-blue-50 rounded-lg transition-colors">
                    <MessageSquare className="h-4 w-4" />
                  </button>
                  <button className="text-green-600 hover:text-green-800 p-2 hover:bg-green-50 rounded-lg transition-colors">
                    <CheckCircle className="h-4 w-4" />
                  </button>
                  {request.status === 'pending' && (
                    <button className="text-red-600 hover:text-red-800 p-2 hover:bg-red-50 rounded-lg transition-colors">
                      <XCircle className="h-4 w-4" />
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Quick Stats Footer */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Categorías Más Solicitadas</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <Droplets className="h-4 w-4 text-blue-600 mr-2" />
                  <span className="text-sm text-gray-700">Plomería</span>
                </div>
                <span className="text-sm font-medium text-gray-900">18</span>
              </div>
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <Zap className="h-4 w-4 text-yellow-600 mr-2" />
                  <span className="text-sm text-gray-700">Electricidad</span>
                </div>
                <span className="text-sm font-medium text-gray-900">12</span>
              </div>
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <Settings className="h-4 w-4 text-gray-600 mr-2" />
                  <span className="text-sm text-gray-700">General</span>
                </div>
                <span className="text-sm font-medium text-gray-900">10</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Técnicos Más Activos</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Carlos Plomero</span>
                <span className="text-sm font-medium text-gray-900">8 trabajos</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Técnico HVAC</span>
                <span className="text-sm font-medium text-gray-900">6 trabajos</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Técnico General</span>
                <span className="text-sm font-medium text-gray-900">5 trabajos</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Próximos Mantenimientos</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Limpieza de filtros</span>
                <span className="text-sm text-gray-500">En 3 días</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Revisión ascensor</span>
                <span className="text-sm text-gray-500">En 1 semana</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Jardines</span>
                <span className="text-sm text-gray-500">En 2 semanas</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}