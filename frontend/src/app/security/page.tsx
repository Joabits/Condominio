"use client";

import { useState } from "react";
import { 
  Shield, 
  Camera, 
  AlertTriangle, 
  UserCheck, 
  Car,
  Eye,
  MapPin,
  Clock,
  User,
  Bell,
  ChevronRight
} from "lucide-react";

export default function SecurityPage() {
  const [selectedCamera, setSelectedCamera] = useState(1);

  const cameras = [
    {
      id: 1,
      name: "Entrada Principal",
      location: "Vestíbulo",
      status: "online",
      lastDetection: "Hace 2 min",
      aiFeatures: ["Reconocimiento Facial", "Control de Acceso"]
    },
    {
      id: 2,
      name: "Parking Norte",
      location: "Estacionamiento",
      status: "online",
      lastDetection: "Hace 5 min",
      aiFeatures: ["OCR Placas", "Detección Vehículos"]
    },
    {
      id: 3,
      name: "Piscina",
      location: "Área Común",
      status: "online",
      lastDetection: "Hace 10 min",
      aiFeatures: ["Detección Personas", "Horarios"]
    },
    {
      id: 4,
      name: "Salida Emergencia",
      location: "Planta Baja",
      status: "offline",
      lastDetection: "Hace 2 horas",
      aiFeatures: ["Control Acceso"]
    }
  ];

  const recentAlerts = [
    {
      id: 1,
      type: "warning",
      title: "Persona No Autorizada",
      description: "Detectada persona desconocida en área restringida",
      location: "Parking Norte",
      time: "hace 15 min",
      confidence: 94,
      status: "pendiente"
    },
    {
      id: 2,
      type: "info",
      title: "Vehículo Registrado",
      description: "Placa ABC-123 identificada correctamente",
      location: "Entrada Principal",
      time: "hace 22 min",
      confidence: 99,
      status: "resuelto"
    },
    {
      id: 3,
      type: "error",
      title: "Acceso Denegado",
      description: "Intento de acceso con credenciales inválidas",
      location: "Puerta Principal",
      time: "hace 35 min",
      confidence: 87,
      status: "investigando"
    }
  ];

  const accessLog = [
    {
      id: 1,
      person: "Juan Pérez",
      type: "Propietario",
      action: "Entrada",
      method: "Reconocimiento Facial",
      time: "14:23",
      confidence: 98
    },
    {
      id: 2,
      person: "María González",
      type: "Visitante",
      action: "Entrada",
      method: "Código Acceso",
      time: "14:15",
      confidence: 100
    },
    {
      id: 3,
      person: "Carlos Rodríguez",
      type: "Propietario",
      action: "Salida",
      method: "Tarjeta",
      time: "14:10",
      confidence: 100
    }
  ];

  const getAlertColor = (type: string) => {
    switch (type) {
      case "warning": return "bg-yellow-100 border-yellow-200 text-yellow-800";
      case "error": return "bg-red-100 border-red-200 text-red-800";
      case "info": return "bg-blue-100 border-blue-200 text-blue-800";
      default: return "bg-gray-100 border-gray-200 text-gray-800";
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case "online": return "bg-green-100 text-green-800";
      case "offline": return "bg-red-100 text-red-800";
      default: return "bg-gray-100 text-gray-800";
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <Shield className="h-8 w-8 text-blue-600" />
              <h1 className="ml-3 text-2xl font-bold text-gray-900">Centro de Seguridad</h1>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2 bg-green-100 px-3 py-1 rounded-full">
                <div className="h-2 w-2 bg-green-500 rounded-full animate-pulse"></div>
                <span className="text-sm font-medium text-green-800">Sistema Activo</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Cámaras en Vivo */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-sm border border-gray-200">
              <div className="p-6 border-b border-gray-200">
                <h2 className="text-xl font-semibold text-gray-900 flex items-center">
                  <Camera className="h-5 w-5 mr-2" />
                  Monitoreo en Tiempo Real
                </h2>
              </div>

              {/* Video Principal */}
              <div className="p-6">
                <div className="bg-gray-900 rounded-lg mb-4 aspect-video flex items-center justify-center">
                  <div className="text-center text-white">
                    <Camera className="h-16 w-16 mx-auto mb-4 opacity-50" />
                    <p className="text-lg font-medium">Cámara {selectedCamera}: {cameras.find(c => c.id === selectedCamera)?.name}</p>
                    <p className="text-sm opacity-75">Transmisión en vivo con IA activa</p>
                  </div>
                </div>

                {/* Grid de Cámaras */}
                <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                  {cameras.map((camera) => (
                    <div
                      key={camera.id}
                      onClick={() => setSelectedCamera(camera.id)}
                      className={`relative bg-gray-800 rounded-lg aspect-video cursor-pointer border-2 transition-all ${
                        selectedCamera === camera.id ? 'border-blue-500' : 'border-transparent hover:border-gray-400'
                      }`}
                    >
                      <div className="absolute inset-0 flex items-center justify-center">
                        <Camera className="h-8 w-8 text-white opacity-50" />
                      </div>
                      <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-2">
                        <p className="text-white text-xs font-medium">{camera.name}</p>
                        <div className="flex items-center space-x-1">
                          <div className={`h-2 w-2 rounded-full ${
                            camera.status === 'online' ? 'bg-green-500' : 'bg-red-500'
                          }`}></div>
                          <span className="text-xs text-gray-300">{camera.status}</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>

                {/* Información de IA */}
                <div className="mt-6 bg-blue-50 rounded-lg p-4">
                  <h3 className="font-medium text-blue-900 mb-2">🤖 Capacidades de IA Activas</h3>
                  <div className="flex flex-wrap gap-2">
                    {cameras.find(c => c.id === selectedCamera)?.aiFeatures.map((feature, index) => (
                      <span key={index} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm">
                        {feature}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Panel Lateral */}
          <div className="space-y-6">
            {/* Alertas Recientes */}
            <div className="bg-white rounded-xl shadow-sm border border-gray-200">
              <div className="p-6 border-b border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900 flex items-center">
                  <AlertTriangle className="h-5 w-5 mr-2" />
                  Alertas Recientes
                </h3>
              </div>
              <div className="p-6 space-y-4">
                {recentAlerts.map((alert) => (
                  <div key={alert.id} className={`p-4 rounded-lg border ${getAlertColor(alert.type)}`}>
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-medium">{alert.title}</h4>
                      <span className="text-xs px-2 py-1 bg-white rounded">{alert.confidence}% IA</span>
                    </div>
                    <p className="text-sm mb-2">{alert.description}</p>
                    <div className="flex justify-between text-xs">
                      <span className="flex items-center">
                        <MapPin className="h-3 w-3 mr-1" />
                        {alert.location}
                      </span>
                      <span className="flex items-center">
                        <Clock className="h-3 w-3 mr-1" />
                        {alert.time}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Log de Accesos */}
            <div className="bg-white rounded-xl shadow-sm border border-gray-200">
              <div className="p-6 border-b border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900 flex items-center">
                  <UserCheck className="h-5 w-5 mr-2" />
                  Accesos Recientes
                </h3>
              </div>
              <div className="p-6 space-y-3">
                {accessLog.map((log) => (
                  <div key={log.id} className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
                    <div className="flex-shrink-0">
                      <div className="h-8 w-8 bg-blue-100 rounded-full flex items-center justify-center">
                        <User className="h-4 w-4 text-blue-600" />
                      </div>
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium text-gray-900">{log.person}</p>
                      <p className="text-xs text-gray-500">{log.type} • {log.method}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-sm text-gray-900">{log.action}</p>
                      <p className="text-xs text-gray-500">{log.time}</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className="border-t border-gray-200 px-6 py-3">
                <button className="text-sm text-blue-600 hover:text-blue-700 font-medium flex items-center">
                  Ver historial completo
                  <ChevronRight className="h-4 w-4 ml-1" />
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Estadísticas de IA */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center">
              <Eye className="h-8 w-8 text-blue-600" />
              <div className="ml-4">
                <p className="text-2xl font-bold text-gray-900">234</p>
                <p className="text-sm text-gray-600">Detecciones IA Hoy</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center">
              <UserCheck className="h-8 w-8 text-green-600" />
              <div className="ml-4">
                <p className="text-2xl font-bold text-gray-900">98.7%</p>
                <p className="text-sm text-gray-600">Precisión Facial</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center">
              <Car className="h-8 w-8 text-purple-600" />
              <div className="ml-4">
                <p className="text-2xl font-bold text-gray-900">45</p>
                <p className="text-sm text-gray-600">Vehículos Detectados</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center">
              <AlertTriangle className="h-8 w-8 text-red-600" />
              <div className="ml-4">
                <p className="text-2xl font-bold text-gray-900">3</p>
                <p className="text-sm text-gray-600">Alertas Activas</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}