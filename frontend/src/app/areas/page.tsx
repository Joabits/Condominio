'use client';

import { useState, useEffect } from 'react';
import { 
  MapPin, 
  Calendar, 
  Clock, 
  Users, 
  Plus, 
  Search, 
  Filter,
  CheckCircle,
  XCircle,
  Edit,
  Eye,
  Star,
  Wifi,
  Car,
  Utensils,
  Dumbbell,
  Waves,
  TreePine,
  Building,
  Music,
  Gamepad2,
  Coffee
} from 'lucide-react';

interface AreaCommon {
  id: string;
  name: string;
  description: string;
  capacity: number;
  type: string;
  amenities: string[];
  hourlyRate: number;
  status: 'available' | 'occupied' | 'maintenance' | 'reserved';
  location: string;
  images: number;
  rating: number;
  totalBookings: number;
}

interface Booking {
  id: string;
  areaId: string;
  areaName: string;
  residentName: string;
  apartment: string;
  date: string;
  startTime: string;
  endTime: string;
  status: 'confirmed' | 'pending' | 'cancelled' | 'completed';
  guests: number;
  totalCost: number;
  notes?: string;
}

interface AreasStats {
  totalAreas: number;
  availableNow: number;
  bookedToday: number;
  revenue: number;
  occupancyRate: number;
  popularArea: string;
}

export default function AreasPage() {
  const [areas, setAreas] = useState<AreaCommon[]>([]);
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [stats, setStats] = useState<AreasStats>({
    totalAreas: 12,
    availableNow: 8,
    bookedToday: 6,
    revenue: 850.00,
    occupancyRate: 73.5,
    popularArea: 'Salón de Eventos'
  });
  const [activeTab, setActiveTab] = useState<'areas' | 'bookings'>('areas');
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    // Simular datos de áreas comunes
    const mockAreas: AreaCommon[] = [
      {
        id: '1',
        name: 'Salón de Eventos',
        description: 'Amplio salón para celebraciones y reuniones familiares',
        capacity: 50,
        type: 'Eventos',
        amenities: ['Audio', 'Proyector', 'Cocina', 'Aire Acondicionado'],
        hourlyRate: 25.00,
        status: 'available',
        location: 'Planta Baja',
        images: 8,
        rating: 4.8,
        totalBookings: 45
      },
      {
        id: '2',
        name: 'Gimnasio',
        description: 'Gimnasio completamente equipado con máquinas de cardio y pesas',
        capacity: 15,
        type: 'Deportes',
        amenities: ['Máquinas de Cardio', 'Pesas', 'Espejos', 'Aire Acondicionado'],
        hourlyRate: 5.00,
        status: 'occupied',
        location: 'Segundo Piso',
        images: 12,
        rating: 4.6,
        totalBookings: 120
      },
      {
        id: '3',
        name: 'Piscina',
        description: 'Piscina climatizada con área de descanso',
        capacity: 20,
        type: 'Recreación',
        amenities: ['Climatizada', 'Duchas', 'Cambiadores', 'Tumbonas'],
        hourlyRate: 8.00,
        status: 'available',
        location: 'Terraza',
        images: 15,
        rating: 4.9,
        totalBookings: 89
      },
      {
        id: '4',
        name: 'Sala de Juegos',
        description: 'Espacio recreativo con juegos de mesa y videojuegos',
        capacity: 12,
        type: 'Entretenimiento',
        amenities: ['Consolas', 'Juegos de Mesa', 'TV Grande', 'Sofás'],
        hourlyRate: 6.00,
        status: 'available',
        location: 'Primer Piso',
        images: 6,
        rating: 4.3,
        totalBookings: 67
      },
      {
        id: '5',
        name: 'Terraza BBQ',
        description: 'Terraza con parrillas y área de comedor al aire libre',
        capacity: 25,
        type: 'Exterior',
        amenities: ['Parrillas', 'Mesas', 'Lavaplatos', 'Iluminación'],
        hourlyRate: 12.00,
        status: 'reserved',
        location: 'Azotea',
        images: 10,
        rating: 4.7,
        totalBookings: 78
      },
      {
        id: '6',
        name: 'Sala de Reuniones',
        description: 'Sala equipada para reuniones de trabajo o estudio',
        capacity: 8,
        type: 'Trabajo',
        amenities: ['WiFi', 'Proyector', 'Pizarra', 'Aire Acondicionado'],
        hourlyRate: 10.00,
        status: 'available',
        location: 'Primer Piso',
        images: 4,
        rating: 4.4,
        totalBookings: 34
      }
    ];

    const mockBookings: Booking[] = [
      {
        id: '1',
        areaId: '1',
        areaName: 'Salón de Eventos',
        residentName: 'María García',
        apartment: 'Apt 205',
        date: '2024-01-20',
        startTime: '18:00',
        endTime: '22:00',
        status: 'confirmed',
        guests: 30,
        totalCost: 100.00,
        notes: 'Cumpleaños familiar'
      },
      {
        id: '2',
        areaId: '3',
        areaName: 'Piscina',
        residentName: 'Juan Pérez',
        apartment: 'Apt 101',
        date: '2024-01-16',
        startTime: '10:00',
        endTime: '12:00',
        status: 'completed',
        guests: 4,
        totalCost: 16.00
      },
      {
        id: '3',
        areaId: '2',
        areaName: 'Gimnasio',
        residentName: 'Roberto Silva',
        apartment: 'Apt 308',
        date: '2024-01-16',
        startTime: '07:00',
        endTime: '08:00',
        status: 'confirmed',
        guests: 1,
        totalCost: 5.00
      },
      {
        id: '4',
        areaId: '5',
        areaName: 'Terraza BBQ',
        residentName: 'Ana Martínez',
        apartment: 'Apt 412',
        date: '2024-01-18',
        startTime: '19:00',
        endTime: '23:00',
        status: 'pending',
        guests: 15,
        totalCost: 48.00,
        notes: 'Cena de amigos'
      }
    ];

    setAreas(mockAreas);
    setBookings(mockBookings);
  }, []);

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'available':
        return 'text-green-600 bg-green-100';
      case 'occupied':
        return 'text-blue-600 bg-blue-100';
      case 'maintenance':
        return 'text-red-600 bg-red-100';
      case 'reserved':
        return 'text-purple-600 bg-purple-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'available':
        return 'Disponible';
      case 'occupied':
        return 'Ocupada';
      case 'maintenance':
        return 'Mantenimiento';
      case 'reserved':
        return 'Reservada';
      default:
        return status;
    }
  };

  const getBookingStatusColor = (status: string) => {
    switch (status) {
      case 'confirmed':
        return 'text-green-600 bg-green-100';
      case 'pending':
        return 'text-yellow-600 bg-yellow-100';
      case 'cancelled':
        return 'text-red-600 bg-red-100';
      case 'completed':
        return 'text-blue-600 bg-blue-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getBookingStatusText = (status: string) => {
    switch (status) {
      case 'confirmed':
        return 'Confirmada';
      case 'pending':
        return 'Pendiente';
      case 'cancelled':
        return 'Cancelada';
      case 'completed':
        return 'Completada';
      default:
        return status;
    }
  };

  const getTypeIcon = (type: string) => {
    switch (type.toLowerCase()) {
      case 'eventos':
        return <Music className="h-5 w-5" />;
      case 'deportes':
        return <Dumbbell className="h-5 w-5" />;
      case 'recreación':
        return <Waves className="h-5 w-5" />;
      case 'entretenimiento':
        return <Gamepad2 className="h-5 w-5" />;
      case 'exterior':
        return <TreePine className="h-5 w-5" />;
      case 'trabajo':
        return <Coffee className="h-5 w-5" />;
      default:
        return <Building className="h-5 w-5" />;
    }
  };

  const filteredAreas = areas.filter(area => {
    const matchesStatus = selectedFilter === 'all' || area.status === selectedFilter;
    const matchesSearch = area.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         area.type.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  const filteredBookings = bookings.filter(booking => {
    const matchesStatus = selectedFilter === 'all' || booking.status === selectedFilter;
    const matchesSearch = booking.areaName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         booking.residentName.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Gestión de Áreas Comunes</h1>
          <p className="text-gray-600">Administración de espacios compartidos y reservas</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-6 mb-8">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Total Áreas</p>
                <p className="text-2xl font-bold text-gray-900">{stats.totalAreas}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <Building className="h-6 w-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Disponibles</p>
                <p className="text-2xl font-bold text-green-600">{stats.availableNow}</p>
              </div>
              <div className="bg-green-100 p-3 rounded-lg">
                <CheckCircle className="h-6 w-6 text-green-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Reservas Hoy</p>
                <p className="text-2xl font-bold text-blue-600">{stats.bookedToday}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <Calendar className="h-6 w-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Ingresos</p>
                <p className="text-2xl font-bold text-gray-900">${stats.revenue}</p>
              </div>
              <div className="bg-purple-100 p-3 rounded-lg">
                <Star className="h-6 w-6 text-purple-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Ocupación</p>
                <p className="text-2xl font-bold text-gray-900">{stats.occupancyRate}%</p>
              </div>
              <div className="bg-orange-100 p-3 rounded-lg">
                <Users className="h-6 w-6 text-orange-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Más Popular</p>
                <p className="text-lg font-bold text-gray-900">{stats.popularArea}</p>
              </div>
              <div className="bg-yellow-100 p-3 rounded-lg">
                <Music className="h-6 w-6 text-yellow-600" />
              </div>
            </div>
          </div>
        </div>

        {/* Tabs */}
        <div className="mb-6">
          <div className="border-b border-gray-200">
            <nav className="-mb-px flex space-x-8">
              <button
                className={`py-2 px-1 border-b-2 font-medium text-sm ${
                  activeTab === 'areas'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
                onClick={() => setActiveTab('areas')}
              >
                Áreas Comunes
              </button>
              <button
                className={`py-2 px-1 border-b-2 font-medium text-sm ${
                  activeTab === 'bookings'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
                onClick={() => setActiveTab('bookings')}
              >
                Reservas
              </button>
            </nav>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap gap-4 mb-6">
          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors flex items-center">
            <Plus className="h-4 w-4 mr-2" />
            {activeTab === 'areas' ? 'Nueva Área' : 'Nueva Reserva'}
          </button>
          <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors flex items-center">
            <Calendar className="h-4 w-4 mr-2" />
            Ver Calendario
          </button>
          <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-colors flex items-center">
            <Users className="h-4 w-4 mr-2" />
            Gestionar Disponibilidad
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
                  placeholder={activeTab === 'areas' ? "Buscar áreas..." : "Buscar reservas..."}
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
                {activeTab === 'areas' ? (
                  <>
                    <option value="all">Todos los estados</option>
                    <option value="available">Disponibles</option>
                    <option value="occupied">Ocupadas</option>
                    <option value="reserved">Reservadas</option>
                    <option value="maintenance">Mantenimiento</option>
                  </>
                ) : (
                  <>
                    <option value="all">Todas las reservas</option>
                    <option value="confirmed">Confirmadas</option>
                    <option value="pending">Pendientes</option>
                    <option value="completed">Completadas</option>
                    <option value="cancelled">Canceladas</option>
                  </>
                )}
              </select>
              <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center">
                <Filter className="h-4 w-4 mr-2" />
                Filtros
              </button>
            </div>
          </div>
        </div>

        {/* Areas Tab Content */}
        {activeTab === 'areas' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredAreas.map((area) => (
              <div key={area.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
                <div className="h-48 bg-gray-200 flex items-center justify-center">
                  <div className="text-center text-gray-500">
                    {getTypeIcon(area.type)}
                    <p className="mt-2 text-sm">{area.images} fotos</p>
                  </div>
                </div>
                
                <div className="p-6">
                  <div className="flex items-start justify-between mb-3">
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900">{area.name}</h3>
                      <p className="text-sm text-gray-500">{area.type}</p>
                    </div>
                    <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getStatusColor(area.status)}`}>
                      {getStatusText(area.status)}
                    </span>
                  </div>
                  
                  <p className="text-gray-600 text-sm mb-4">{area.description}</p>
                  
                  <div className="space-y-2 mb-4">
                    <div className="flex items-center text-sm text-gray-600">
                      <Users className="h-4 w-4 mr-2" />
                      Capacidad: {area.capacity} personas
                    </div>
                    <div className="flex items-center text-sm text-gray-600">
                      <MapPin className="h-4 w-4 mr-2" />
                      {area.location}
                    </div>
                    <div className="flex items-center text-sm text-gray-600">
                      <Star className="h-4 w-4 mr-2" />
                      {area.rating}/5 ({area.totalBookings} reservas)
                    </div>
                  </div>
                  
                  <div className="mb-4">
                    <p className="text-sm font-medium text-gray-700 mb-2">Amenidades:</p>
                    <div className="flex flex-wrap gap-1">
                      {area.amenities.slice(0, 3).map((amenity, index) => (
                        <span key={index} className="inline-block px-2 py-1 text-xs bg-blue-100 text-blue-600 rounded">
                          {amenity}
                        </span>
                      ))}
                      {area.amenities.length > 3 && (
                        <span className="inline-block px-2 py-1 text-xs bg-gray-100 text-gray-600 rounded">
                          +{area.amenities.length - 3} más
                        </span>
                      )}
                    </div>
                  </div>
                  
                  <div className="flex items-center justify-between pt-4 border-t border-gray-200">
                    <div>
                      <span className="text-lg font-bold text-gray-900">${area.hourlyRate}</span>
                      <span className="text-sm text-gray-500">/hora</span>
                    </div>
                    <div className="flex space-x-2">
                      <button className="text-blue-600 hover:text-blue-800 p-1">
                        <Eye className="h-4 w-4" />
                      </button>
                      <button className="text-green-600 hover:text-green-800 p-1">
                        <Calendar className="h-4 w-4" />
                      </button>
                      <button className="text-gray-600 hover:text-gray-800 p-1">
                        <Edit className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Bookings Tab Content */}
        {activeTab === 'bookings' && (
          <div className="space-y-4">
            {filteredBookings.map((booking) => (
              <div key={booking.id} className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
                <div className="flex items-start justify-between mb-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <h3 className="text-lg font-semibold text-gray-900">{booking.areaName}</h3>
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getBookingStatusColor(booking.status)}`}>
                        {getBookingStatusText(booking.status)}
                      </span>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-gray-600">
                      <div className="flex items-center">
                        <Users className="h-4 w-4 mr-2" />
                        {booking.residentName} ({booking.apartment})
                      </div>
                      <div className="flex items-center">
                        <Calendar className="h-4 w-4 mr-2" />
                        {new Date(booking.date).toLocaleDateString()}
                      </div>
                      <div className="flex items-center">
                        <Clock className="h-4 w-4 mr-2" />
                        {booking.startTime} - {booking.endTime}
                      </div>
                    </div>
                    {booking.notes && (
                      <p className="text-sm text-gray-600 mt-2">
                        <strong>Notas:</strong> {booking.notes}
                      </p>
                    )}
                  </div>
                  <div className="text-right">
                    <div className="text-lg font-bold text-gray-900">${booking.totalCost}</div>
                    <div className="text-sm text-gray-500">{booking.guests} invitados</div>
                  </div>
                </div>
                
                <div className="flex justify-end space-x-2 pt-4 border-t border-gray-200">
                  <button className="text-blue-600 hover:text-blue-800 p-2 hover:bg-blue-50 rounded-lg transition-colors">
                    <Eye className="h-4 w-4" />
                  </button>
                  {booking.status === 'pending' && (
                    <>
                      <button className="text-green-600 hover:text-green-800 p-2 hover:bg-green-50 rounded-lg transition-colors">
                        <CheckCircle className="h-4 w-4" />
                      </button>
                      <button className="text-red-600 hover:text-red-800 p-2 hover:bg-red-50 rounded-lg transition-colors">
                        <XCircle className="h-4 w-4" />
                      </button>
                    </>
                  )}
                  <button className="text-gray-600 hover:text-gray-800 p-2 hover:bg-gray-50 rounded-lg transition-colors">
                    <Edit className="h-4 w-4" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Quick Stats */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Áreas Más Populares</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Salón de Eventos</span>
                <span className="text-sm font-medium text-gray-900">45 reservas</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Gimnasio</span>
                <span className="text-sm font-medium text-gray-900">120 reservas</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">Piscina</span>
                <span className="text-sm font-medium text-gray-900">89 reservas</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Horarios Más Solicitados</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">18:00 - 22:00</span>
                <span className="text-sm font-medium text-gray-900">35%</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">10:00 - 14:00</span>
                <span className="text-sm font-medium text-gray-900">28%</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-700">14:00 - 18:00</span>
                <span className="text-sm font-medium text-gray-900">22%</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Próximas Reservas</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-sm text-gray-700">Salón de Eventos</span>
                  <div className="text-xs text-gray-500">María García</div>
                </div>
                <span className="text-sm text-gray-500">20 Ene</span>
              </div>
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-sm text-gray-700">Terraza BBQ</span>
                  <div className="text-xs text-gray-500">Ana Martínez</div>
                </div>
                <span className="text-sm text-gray-500">18 Ene</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}