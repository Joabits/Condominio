'use client';

import { useState, useEffect } from 'react';
import { 
  Users, 
  UserPlus, 
  Phone, 
  Mail, 
  MapPin, 
  Calendar, 
  Search, 
  Filter, 
  Edit, 
  Trash2, 
  Eye,
  Download,
  Upload,
  Home,
  Car,
  Shield,
  AlertTriangle,
  CheckCircle
} from 'lucide-react';

interface Resident {
  id: string;
  name: string;
  email: string;
  phone: string;
  apartment: string;
  role: 'owner' | 'tenant' | 'family';
  status: 'active' | 'inactive' | 'pending';
  moveInDate: string;
  emergencyContact: {
    name: string;
    phone: string;
    relationship: string;
  };
  vehicles: number;
  pets: boolean;
  avatar?: string;
}

interface ResidentStats {
  totalResidents: number;
  activeResidents: number;
  newThisMonth: number;
  occupancyRate: number;
}

export default function ResidentsPage() {
  const [residents, setResidents] = useState<Resident[]>([]);
  const [stats, setStats] = useState<ResidentStats>({
    totalResidents: 85,
    activeResidents: 82,
    newThisMonth: 3,
    occupancyRate: 94.2
  });
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRole, setSelectedRole] = useState('all');

  useEffect(() => {
    // Simular datos de residentes
    const mockResidents: Resident[] = [
      {
        id: '1',
        name: 'Juan Carlos Pérez',
        email: 'juan.perez@email.com',
        phone: '+1 555-0123',
        apartment: 'Apt 101',
        role: 'owner',
        status: 'active',
        moveInDate: '2023-03-15',
        emergencyContact: {
          name: 'María Pérez',
          phone: '+1 555-0124',
          relationship: 'Esposa'
        },
        vehicles: 2,
        pets: true
      },
      {
        id: '2',
        name: 'María Elena García',
        email: 'maria.garcia@email.com',
        phone: '+1 555-0125',
        apartment: 'Apt 205',
        role: 'tenant',
        status: 'active',
        moveInDate: '2023-06-01',
        emergencyContact: {
          name: 'Carlos García',
          phone: '+1 555-0126',
          relationship: 'Hermano'
        },
        vehicles: 1,
        pets: false
      },
      {
        id: '3',
        name: 'Roberto Silva',
        email: 'roberto.silva@email.com',
        phone: '+1 555-0127',
        apartment: 'Apt 308',
        role: 'owner',
        status: 'pending',
        moveInDate: '2024-01-15',
        emergencyContact: {
          name: 'Ana Silva',
          phone: '+1 555-0128',
          relationship: 'Madre'
        },
        vehicles: 1,
        pets: true
      },
      {
        id: '4',
        name: 'Ana Martínez',
        email: 'ana.martinez@email.com',
        phone: '+1 555-0129',
        apartment: 'Apt 412',
        role: 'family',
        status: 'active',
        moveInDate: '2022-11-20',
        emergencyContact: {
          name: 'Luis Martínez',
          phone: '+1 555-0130',
          relationship: 'Padre'
        },
        vehicles: 0,
        pets: false
      },
      {
        id: '5',
        name: 'Luis Fernando Rodríguez',
        email: 'luis.rodriguez@email.com',
        phone: '+1 555-0131',
        apartment: 'Apt 503',
        role: 'owner',
        status: 'active',
        moveInDate: '2023-09-10',
        emergencyContact: {
          name: 'Carmen Rodríguez',
          phone: '+1 555-0132',
          relationship: 'Esposa'
        },
        vehicles: 2,
        pets: true
      }
    ];
    setResidents(mockResidents);
  }, []);

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active':
        return 'text-green-600 bg-green-100';
      case 'inactive':
        return 'text-gray-600 bg-gray-100';
      case 'pending':
        return 'text-yellow-600 bg-yellow-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'active':
        return 'Activo';
      case 'inactive':
        return 'Inactivo';
      case 'pending':
        return 'Pendiente';
      default:
        return status;
    }
  };

  const getRoleText = (role: string) => {
    switch (role) {
      case 'owner':
        return 'Propietario';
      case 'tenant':
        return 'Inquilino';
      case 'family':
        return 'Familiar';
      default:
        return role;
    }
  };

  const getRoleColor = (role: string) => {
    switch (role) {
      case 'owner':
        return 'text-blue-600 bg-blue-100';
      case 'tenant':
        return 'text-purple-600 bg-purple-100';
      case 'family':
        return 'text-orange-600 bg-orange-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const filteredResidents = residents.filter(resident => {
    const matchesStatus = selectedFilter === 'all' || resident.status === selectedFilter;
    const matchesRole = selectedRole === 'all' || resident.role === selectedRole;
    const matchesSearch = resident.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         resident.apartment.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         resident.email.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStatus && matchesRole && matchesSearch;
  });

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Gestión de Residentes</h1>
          <p className="text-gray-600">Administración de residentes, propietarios e inquilinos</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Total Residentes</p>
                <p className="text-2xl font-bold text-gray-900">{stats.totalResidents}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <Users className="h-6 w-6 text-blue-600" />
              </div>
            </div>
            <div className="mt-4 flex items-center">
              <CheckCircle className="h-4 w-4 text-green-500 mr-1" />
              <span className="text-sm text-green-600">{stats.activeResidents} activos</span>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Nuevos Este Mes</p>
                <p className="text-2xl font-bold text-gray-900">{stats.newThisMonth}</p>
              </div>
              <div className="bg-green-100 p-3 rounded-lg">
                <UserPlus className="h-6 w-6 text-green-600" />
              </div>
            </div>
            <div className="mt-4 flex items-center">
              <Calendar className="h-4 w-4 text-gray-500 mr-1" />
              <span className="text-sm text-gray-600">Último: Ayer</span>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Tasa de Ocupación</p>
                <p className="text-2xl font-bold text-gray-900">{stats.occupancyRate}%</p>
              </div>
              <div className="bg-purple-100 p-3 rounded-lg">
                <Home className="h-6 w-6 text-purple-600" />
              </div>
            </div>
            <div className="mt-4 flex items-center">
              <MapPin className="h-4 w-4 text-gray-500 mr-1" />
              <span className="text-sm text-gray-600">82 de 87 unidades</span>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Verificaciones Pendientes</p>
                <p className="text-2xl font-bold text-gray-900">3</p>
              </div>
              <div className="bg-yellow-100 p-3 rounded-lg">
                <AlertTriangle className="h-6 w-6 text-yellow-600" />
              </div>
            </div>
            <div className="mt-4 flex items-center">
              <Shield className="h-4 w-4 text-yellow-500 mr-1" />
              <span className="text-sm text-yellow-600">Requieren atención</span>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap gap-4 mb-6">
          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors flex items-center">
            <UserPlus className="h-4 w-4 mr-2" />
            Agregar Residente
          </button>
          <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors flex items-center">
            <Upload className="h-4 w-4 mr-2" />
            Importar Lista
          </button>
          <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-colors flex items-center">
            <Download className="h-4 w-4 mr-2" />
            Exportar Datos
          </button>
          <button className="bg-orange-600 text-white px-4 py-2 rounded-lg hover:bg-orange-700 transition-colors flex items-center">
            <Shield className="h-4 w-4 mr-2" />
            Verificar Identidades
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
                  placeholder="Buscar por nombre, apartamento o email..."
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
                <option value="active">Activos</option>
                <option value="inactive">Inactivos</option>
                <option value="pending">Pendientes</option>
              </select>
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={selectedRole}
                onChange={(e) => setSelectedRole(e.target.value)}
              >
                <option value="all">Todos los roles</option>
                <option value="owner">Propietarios</option>
                <option value="tenant">Inquilinos</option>
                <option value="family">Familiares</option>
              </select>
              <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center">
                <Filter className="h-4 w-4 mr-2" />
                Más Filtros
              </button>
            </div>
          </div>
        </div>

        {/* Residents Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredResidents.map((resident) => (
            <div key={resident.id} className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center">
                  <div className="w-12 h-12 bg-gray-200 rounded-full flex items-center justify-center">
                    <Users className="h-6 w-6 text-gray-400" />
                  </div>
                  <div className="ml-3">
                    <h3 className="text-lg font-semibold text-gray-900">{resident.name}</h3>
                    <p className="text-sm text-gray-500">{resident.apartment}</p>
                  </div>
                </div>
                <div className="flex space-x-1">
                  <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getStatusColor(resident.status)}`}>
                    {getStatusText(resident.status)}
                  </span>
                </div>
              </div>

              <div className="space-y-2 mb-4">
                <div className="flex items-center text-sm text-gray-600">
                  <Mail className="h-4 w-4 mr-2" />
                  {resident.email}
                </div>
                <div className="flex items-center text-sm text-gray-600">
                  <Phone className="h-4 w-4 mr-2" />
                  {resident.phone}
                </div>
                <div className="flex items-center text-sm text-gray-600">
                  <Calendar className="h-4 w-4 mr-2" />
                  Ingreso: {new Date(resident.moveInDate).toLocaleDateString()}
                </div>
              </div>

              <div className="flex items-center justify-between mb-4">
                <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getRoleColor(resident.role)}`}>
                  {getRoleText(resident.role)}
                </span>
                <div className="flex items-center space-x-3 text-sm text-gray-500">
                  <div className="flex items-center">
                    <Car className="h-4 w-4 mr-1" />
                    {resident.vehicles}
                  </div>
                  {resident.pets && (
                    <div className="flex items-center">
                      <span className="text-xs">🐕</span>
                    </div>
                  )}
                </div>
              </div>

              <div className="border-t border-gray-200 pt-4">
                <p className="text-xs text-gray-500 mb-2">Contacto de Emergencia:</p>
                <p className="text-sm font-medium text-gray-700">{resident.emergencyContact.name}</p>
                <p className="text-sm text-gray-500">{resident.emergencyContact.phone}</p>
              </div>

              <div className="flex justify-end space-x-2 mt-4 pt-4 border-t border-gray-200">
                <button className="text-blue-600 hover:text-blue-800 p-1">
                  <Eye className="h-4 w-4" />
                </button>
                <button className="text-green-600 hover:text-green-800 p-1">
                  <Edit className="h-4 w-4" />
                </button>
                <button className="text-red-600 hover:text-red-800 p-1">
                  <Trash2 className="h-4 w-4" />
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Quick Actions Panel */}
        <div className="mt-8 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Acciones Rápidas</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <Shield className="h-6 w-6 text-blue-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Verificar Identidades</p>
                  <p className="text-sm text-gray-500">3 pendientes</p>
                </div>
              </div>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <Car className="h-6 w-6 text-green-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Gestionar Vehículos</p>
                  <p className="text-sm text-gray-500">48 registrados</p>
                </div>
              </div>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <AlertTriangle className="h-6 w-6 text-yellow-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Revisar Alertas</p>
                  <p className="text-sm text-gray-500">2 nuevas</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}