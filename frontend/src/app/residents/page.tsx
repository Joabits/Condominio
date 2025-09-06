'use client';

import { useState, useEffect } from 'react';
import Navigation from '../../components/Navigation';
import apiService, { PerfilUsuario } from '../../services/api';
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
  CheckCircle,
  Loader
} from 'lucide-react';

interface ResidentStats {
  totalResidents: number;
  activeResidents: number;
  newThisMonth: number;
  occupancyRate: number;
}

export default function ResidentsPage() {
  const [residents, setResidents] = useState<PerfilUsuario[]>([]);
  const [stats, setStats] = useState<ResidentStats>({
    totalResidents: 0,
    activeResidents: 0,
    newThisMonth: 0,
    occupancyRate: 0
  });
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRole, setSelectedRole] = useState('all');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadResidents();
    loadStats();
  }, []);

  const loadResidents = async () => {
    try {
      setLoading(true);
      const data = await apiService.getUsuarios();
      // Asegurar que data es un array
      setResidents(Array.isArray(data) ? data : []);
      setError(null);
    } catch (err) {
      setError('Error al cargar residentes');
      setResidents([]); // Asegurar que residents sea un array vacío en caso de error
      console.error('Error loading residents:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadStats = async () => {
    try {
      const data = await apiService.getEstadisticas();
      if (data && data.residentes) {
        setStats({
          totalResidents: data.residentes.total || (residents || []).length,
          activeResidents: data.residentes.activos || (residents || []).filter(r => r.activo).length,
          newThisMonth: data.residentes.nuevos_mes || 0,
          occupancyRate: data.residentes.tasa_ocupacion || 0
        });
      } else {
        // Estadísticas calculadas localmente
        setStats({
          totalResidents: (residents || []).length,
          activeResidents: (residents || []).filter(r => r.activo).length,
          newThisMonth: 0,
          occupancyRate: 0
        });
      }
    } catch (err) {
      console.error('Error loading stats:', err);
      // Estadísticas calculadas localmente
      setStats({
        totalResidents: (residents || []).length,
        activeResidents: (residents || []).filter(r => r.activo).length,
        newThisMonth: 0,
        occupancyRate: 0
      });
    }
  };

  const getStatusColor = (activo: boolean) => {
    return activo ? 'text-green-600 bg-green-100' : 'text-red-600 bg-red-100';
  };

  const getStatusText = (activo: boolean) => {
    return activo ? 'Activo' : 'Inactivo';
  };

  const getRoleText = (tipo: string) => {
    switch (tipo.toUpperCase()) {
      case 'PROPIETARIO':
        return 'Propietario';
      case 'INQUILINO':
        return 'Inquilino';
      case 'ADMINISTRADOR':
        return 'Administrador';
      case 'SEGURIDAD':
        return 'Seguridad';
      case 'MANTENIMIENTO':
        return 'Mantenimiento';
      default:
        return tipo;
    }
  };

  const getRoleColor = (tipo: string) => {
    switch (tipo.toUpperCase()) {
      case 'PROPIETARIO':
        return 'text-blue-600 bg-blue-100';
      case 'INQUILINO':
        return 'text-purple-600 bg-purple-100';
      case 'ADMINISTRADOR':
        return 'text-red-600 bg-red-100';
      case 'SEGURIDAD':
        return 'text-yellow-600 bg-yellow-100';
      case 'MANTENIMIENTO':
        return 'text-orange-600 bg-orange-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('es-ES');
  };

  const filteredResidents = (residents || []).filter(resident => {
    const isActive = resident.activo;
    const matchesStatus = selectedFilter === 'all' || 
                         (selectedFilter === 'active' && isActive) ||
                         (selectedFilter === 'inactive' && !isActive);
    
    const userType = resident.tipo_usuario?.tipo || '';
    const matchesRole = selectedRole === 'all' || userType.toUpperCase() === selectedRole.toUpperCase();
    
    const searchFields = [
      resident.user.first_name,
      resident.user.last_name,
      resident.user.email,
      resident.ci,
      resident.telefono
    ].join(' ').toLowerCase();
    
    const matchesSearch = searchFields.includes(searchTerm.toLowerCase());
    
    return matchesStatus && matchesRole && matchesSearch;
  });

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <Loader className="h-8 w-8 animate-spin mx-auto mb-4 text-blue-600" />
          <p className="text-gray-600">Cargando residentes...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <AlertTriangle className="h-8 w-8 mx-auto mb-4 text-red-600" />
          <p className="text-gray-600">{error}</p>
          <button 
            onClick={loadResidents}
            className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation />
      
      <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
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
              <span className="text-sm text-gray-600">Registro reciente</span>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Tasa de Ocupación</p>
                <p className="text-2xl font-bold text-gray-900">{stats.occupancyRate.toFixed(1)}%</p>
              </div>
              <div className="bg-purple-100 p-3 rounded-lg">
                <Home className="h-6 w-6 text-purple-600" />
              </div>
            </div>
            <div className="mt-4 flex items-center">
              <MapPin className="h-4 w-4 text-gray-500 mr-1" />
              <span className="text-sm text-gray-600">Condominio Buganvillas</span>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Inactivos</p>
                <p className="text-2xl font-bold text-gray-900">{stats.totalResidents - stats.activeResidents}</p>
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
          <button 
            onClick={loadResidents}
            className="bg-orange-600 text-white px-4 py-2 rounded-lg hover:bg-orange-700 transition-colors flex items-center"
          >
            <Shield className="h-4 w-4 mr-2" />
            Actualizar
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
                  placeholder="Buscar por nombre, CI, email o teléfono..."
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
              </select>
              <select
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={selectedRole}
                onChange={(e) => setSelectedRole(e.target.value)}
              >
                <option value="all">Todos los roles</option>
                <option value="PROPIETARIO">Propietarios</option>
                <option value="INQUILINO">Inquilinos</option>
                <option value="ADMINISTRADOR">Administradores</option>
                <option value="SEGURIDAD">Seguridad</option>
                <option value="MANTENIMIENTO">Mantenimiento</option>
              </select>
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
                    <h3 className="text-lg font-semibold text-gray-900">
                      {resident.user.first_name} {resident.user.last_name}
                    </h3>
                    <p className="text-sm text-gray-500">CI: {resident.ci}</p>
                  </div>
                </div>
                <div className="flex space-x-1">
                  <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getStatusColor(resident.activo)}`}>
                    {getStatusText(resident.activo)}
                  </span>
                </div>
              </div>

              <div className="space-y-2 mb-4">
                <div className="flex items-center text-sm text-gray-600">
                  <Mail className="h-4 w-4 mr-2" />
                  {resident.user.email}
                </div>
                <div className="flex items-center text-sm text-gray-600">
                  <Phone className="h-4 w-4 mr-2" />
                  {resident.telefono || 'No registrado'}
                </div>
                <div className="flex items-center text-sm text-gray-600">
                  <Calendar className="h-4 w-4 mr-2" />
                  Usuario: {resident.user.username}
                </div>
              </div>

              <div className="flex items-center justify-between mb-4">
                <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getRoleColor(resident.tipo_usuario?.tipo || '')}`}>
                  {getRoleText(resident.tipo_usuario?.tipo || '')}
                </span>
                <div className="text-sm text-gray-500">
                  {resident.condominio?.nombre || 'Sin condominio'}
                </div>
              </div>

              <div className="border-t border-gray-200 pt-4">
                <p className="text-xs text-gray-500 mb-2">Información adicional:</p>
                <p className="text-sm text-gray-700">CI: {resident.ci}</p>
                {resident.telefono && (
                  <p className="text-sm text-gray-500">Teléfono: {resident.telefono}</p>
                )}
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

        {filteredResidents.length === 0 && !loading && (
          <div className="text-center py-12">
            <Users className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            <p className="text-gray-500">No se encontraron residentes con los filtros seleccionados</p>
          </div>
        )}

        {/* Quick Actions Panel */}
        <div className="mt-8 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Acciones Rápidas</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <Shield className="h-6 w-6 text-blue-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Gestionar Accesos</p>
                  <p className="text-sm text-gray-500">{stats.activeResidents} usuarios activos</p>
                </div>
              </div>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <Home className="h-6 w-6 text-green-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Gestionar Unidades</p>
                  <p className="text-sm text-gray-500">Asignar residencias</p>
                </div>
              </div>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
              <div className="flex items-center">
                <AlertTriangle className="h-6 w-6 text-yellow-600 mr-3" />
                <div>
                  <p className="font-medium text-gray-900">Revisar Perfiles</p>
                  <p className="text-sm text-gray-500">Validar información</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}