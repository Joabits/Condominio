"use client";

import { useState } from "react";
import Link from "next/link";
import ProtectedLayout from "../components/ProtectedLayout";
import { 
  Building2, 
  Users, 
  Shield, 
  CreditCard, 
  Bell, 
  Calendar,
  Camera,
  Activity,
  AlertTriangle,
  TrendingUp,
  Car,
  Wrench
} from "lucide-react";

export default function Home() {
  const [selectedModule, setSelectedModule] = useState("dashboard");

  const modules = [
    {
      id: "dashboard",
      name: "Dashboard",
      icon: Activity,
      description: "Vista general del condominio",
      color: "bg-blue-500"
    },
    {
      id: "security",
      name: "Seguridad",
      icon: Shield,
      description: "Control de acceso e IA",
      color: "bg-red-500"
    },
    {
      id: "finance",
      name: "Finanzas",
      icon: CreditCard,
      description: "Expensas y pagos",
      color: "bg-green-500"
    },
    {
      id: "residents",
      name: "Residentes",
      icon: Users,
      description: "Gestión de propietarios",
      color: "bg-purple-500"
    },
    {
      id: "areas",
      name: "Áreas Comunes",
      icon: Calendar,
      description: "Reservas y horarios",
      color: "bg-yellow-500"
    },
    {
      id: "maintenance",
      name: "Mantenimiento",
      icon: Wrench,
      description: "Servicios y reparaciones",
      color: "bg-orange-500"
    },
    {
      id: "cameras",
      name: "Cámaras",
      icon: Camera,
      description: "Monitoreo en tiempo real",
      color: "bg-indigo-500"
    },
    {
      id: "notifications",
      name: "Comunicados",
      icon: Bell,
      description: "Avisos y alertas",
      color: "bg-pink-500"
    }
  ];

  const stats = [
    {
      name: "Total Unidades",
      value: "24",
      change: "+2",
      changeType: "positive"
    },
    {
      name: "Morosidad",
      value: "8.5%",
      change: "-2.1%",
      changeType: "positive"
    },
    {
      name: "Alertas Activas",
      value: "3",
      change: "+1",
      changeType: "negative"
    },
    {
      name: "Ingresos Mes",
      value: "$45,250",
      change: "+12%",
      changeType: "positive"
    }
  ];

  const recentActivities = [
    {
      type: "access",
      message: "Juan Pérez ingresó por puerta principal",
      time: "hace 5 min",
      icon: Shield,
      color: "text-green-600"
    },
    {
      type: "payment",
      message: "Pago recibido - Apt 205",
      time: "hace 15 min",
      icon: CreditCard,
      color: "text-blue-600"
    },
    {
      type: "alert",
      message: "Vehículo no autorizado detectado",
      time: "hace 32 min",
      icon: AlertTriangle,
      color: "text-red-600"
    },
    {
      type: "maintenance",
      message: "Mantenimiento programado - Ascensor A",
      time: "hace 1 hora",
      icon: Wrench,
      color: "text-orange-600"
    }
  ];

  return (
    <ProtectedLayout>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-2">
            Panel de Administración - Condominio Buganvillas
          </h2>
          <p className="text-lg text-gray-600">
            Sistema inteligente de administración con IA y visión artificial
          </p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {stats.map((stat, index) => (
            <div key={index} className="bg-white rounded-xl shadow-sm p-6 border border-gray-200">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">{stat.name}</p>
                  <p className="text-2xl font-bold text-gray-900 mt-1">{stat.value}</p>
                </div>
                <div className={`flex items-center text-sm ${
                  stat.changeType === 'positive' ? 'text-green-600' : 'text-red-600'
                }`}>
                  <TrendingUp className="h-4 w-4 mr-1" />
                  {stat.change}
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Modules Grid */}
          <div className="lg:col-span-2">
            <h3 className="text-xl font-semibold text-gray-900 mb-6">Módulos del Sistema</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {modules.map((module) => {
                const IconComponent = module.icon;
                const moduleHref = module.id === 'security' ? '/security' 
                  : module.id === 'finance' ? '/finance'
                  : module.id === 'residents' ? '/residents'
                  : module.id === 'maintenance' ? '/maintenance'
                  : module.id === 'areas' ? '/areas'
                  : '#';
                
                const isActive = moduleHref !== '#';
                
                return (
                  <Link
                    key={module.id}
                    href={moduleHref}
                    className={`bg-white rounded-xl shadow-sm p-6 border border-gray-200 hover:shadow-md transition-shadow cursor-pointer group ${!isActive ? 'opacity-75' : ''}`}
                  >
                    <div className="flex items-center space-x-4">
                      <div className={`${module.color} p-3 rounded-lg group-hover:scale-110 transition-transform`}>
                        <IconComponent className="h-6 w-6 text-white" />
                      </div>
                      <div>
                        <h4 className="text-lg font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">
                          {module.name}
                        </h4>
                        <p className="text-sm text-gray-600">{module.description}</p>
                      </div>
                    </div>
                  </Link>
                );
              })}
            </div>
          </div>

          {/* Recent Activities */}
          <div className="lg:col-span-1">
            <h3 className="text-xl font-semibold text-gray-900 mb-6">Actividad Reciente</h3>
            <div className="bg-white rounded-xl shadow-sm border border-gray-200">
              <div className="p-6">
                <div className="space-y-4">
                  {recentActivities.map((activity, index) => {
                    const IconComponent = activity.icon;
                    return (
                      <div key={index} className="flex items-start space-x-3">
                        <div className={`${activity.color} p-1`}>
                          <IconComponent className="h-4 w-4" />
                        </div>
                        <div className="flex-1 min-w-0">
                          <p className="text-sm text-gray-900">{activity.message}</p>
                          <p className="text-xs text-gray-500">{activity.time}</p>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
              <div className="border-t border-gray-200 px-6 py-3">
                <button className="text-sm text-blue-600 hover:text-blue-700 font-medium">
                  Ver todas las actividades →
                </button>
              </div>
            </div>

            {/* Quick Actions */}
            <div className="mt-6 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <h4 className="text-lg font-semibold text-gray-900 mb-4">Acciones Rápidas</h4>
              <div className="space-y-3">
                <button className="w-full text-left p-3 rounded-lg bg-blue-50 hover:bg-blue-100 transition-colors">
                  <div className="flex items-center space-x-3">
                    <Bell className="h-5 w-5 text-blue-600" />
                    <span className="text-sm font-medium text-blue-900">Nuevo Comunicado</span>
                  </div>
                </button>
                <button className="w-full text-left p-3 rounded-lg bg-green-50 hover:bg-green-100 transition-colors">
                  <div className="flex items-center space-x-3">
                    <CreditCard className="h-5 w-5 text-green-600" />
                    <span className="text-sm font-medium text-green-900">Generar Expensas</span>
                  </div>
                </button>
                <button className="w-full text-left p-3 rounded-lg bg-purple-50 hover:bg-purple-100 transition-colors">
                  <div className="flex items-center space-x-3">
                    <Users className="h-5 w-5 text-purple-600" />
                    <span className="text-sm font-medium text-purple-900">Agregar Residente</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Footer Info */}
        <div className="mt-12 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl shadow-sm p-8 text-white">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-xl font-semibold mb-2">🤖 Inteligencia Artificial Activa</h3>
              <p className="text-blue-100">
                Reconocimiento facial, detección de vehículos y predicción de morosidad funcionando
              </p>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-center">
                <p className="text-2xl font-bold">99.8%</p>
                <p className="text-sm text-blue-100">Precisión IA</p>
              </div>
              <div className="text-center">
                <p className="text-2xl font-bold">24/7</p>
                <p className="text-sm text-blue-100">Monitoreo</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </ProtectedLayout>
  );
}
