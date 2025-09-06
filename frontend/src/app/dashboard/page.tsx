"use client";

import { useState } from "react";
import Link from "next/link";
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

export default function DashboardPage() {
  const [selectedModule, setSelectedModule] = useState("dashboard");

  const modules = [
    {
      id: "dashboard",
      name: "Dashboard",
      icon: Activity,
      description: "Vista general del condominio",
      color: "bg-primary-500"
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
      color: "bg-emerald-500"
    },
    {
      id: "residents",
      name: "Residentes",
      icon: Users,
      description: "Gestión de propietarios",
      color: "bg-primary-600"
    },
    {
      id: "areas",
      name: "Áreas Comunes",
      icon: Calendar,
      description: "Reservas y horarios",
      color: "bg-amber-500"
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
      color: "bg-primary-700"
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
      color: "text-emerald-600"
    },
    {
      type: "payment",
      message: "Pago recibido - Apt 205",
      time: "hace 15 min",
      icon: CreditCard,
      color: "text-primary-600"
    },
    {
      type: "alert",
      message: "Vehículo no autorizado detectado",
      time: "hace 32 min",
      icon: AlertTriangle,
      color: "text-red-500"
    },
    {
      type: "maintenance",
      message: "Mantenimiento programado - Ascensor A",
      time: "hace 1 hora",
      icon: Wrench,
      color: "text-orange-500"
    }
  ];

  return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 relative overflow-hidden">
        {/* Animated background elements */}
        <div className="absolute inset-0">
          <div className="absolute top-0 -left-4 w-72 h-72 bg-blue-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"></div>
          <div className="absolute top-0 -right-4 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
          <div className="absolute -bottom-8 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
        </div>
        
        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {/* Welcome Section */}
          <div className="mb-10 text-center">
            <h1 className="text-5xl font-black text-white mb-4 tracking-tight">
              <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                Condominio Buganvillas
              </span>
            </h1>
            <p className="text-xl text-blue-200 font-light max-w-3xl mx-auto">
              Sistema inteligente de administración con IA y visión artificial
            </p>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            {stats.map((stat, index) => (
              <div key={index} className="group relative bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:bg-white/20 transition-all duration-500 hover:scale-105 hover:shadow-2xl">
                {/* Gradient border */}
                <div className="absolute inset-0 bg-gradient-to-r from-blue-400 to-purple-400 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-sm -z-10"></div>
                
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-bold text-blue-300 uppercase tracking-widest mb-2">{stat.name}</p>
                    <p className="text-4xl font-black text-white">{stat.value}</p>
                  </div>
                  <div className={`flex items-center text-sm font-bold px-4 py-2 rounded-full backdrop-blur-sm ${
                    stat.changeType === 'positive' 
                      ? 'text-emerald-300 bg-emerald-500/20 border border-emerald-400/30' 
                      : 'text-red-300 bg-red-500/20 border border-red-400/30'
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
              <h3 className="text-3xl font-bold text-white mb-8 flex items-center">
                <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                  Módulos del Sistema
                </span>
              </h3>
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
                      className={`group relative bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:bg-white/20 transition-all duration-500 cursor-pointer hover:scale-105 hover:shadow-2xl ${!isActive ? 'opacity-75' : ''}`}
                    >
                      {/* Gradient border on hover */}
                      <div className="absolute inset-0 bg-gradient-to-r from-blue-400 to-purple-400 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-sm -z-10"></div>
                      
                      <div className="flex items-center space-x-5">
                        <div className={`${module.color} p-4 rounded-xl group-hover:scale-110 transition-transform duration-300 shadow-lg group-hover:shadow-xl`}>
                          <IconComponent className="h-7 w-7 text-white" />
                        </div>
                        <div>
                          <h4 className="text-xl font-bold text-white group-hover:text-blue-300 transition-colors duration-300">
                            {module.name}
                          </h4>
                          <p className="text-blue-200 font-medium">{module.description}</p>
                        </div>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </div>

            {/* Recent Activities */}
            <div className="lg:col-span-1">
              <h3 className="text-3xl font-bold text-white mb-8">
                <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                  Actividad Reciente
                </span>
              </h3>
              <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 overflow-hidden">
                <div className="p-6">
                  <div className="space-y-4">
                    {recentActivities.map((activity, index) => {
                      const IconComponent = activity.icon;
                      return (
                        <div key={index} className="flex items-start space-x-4 p-4 rounded-xl hover:bg-white/10 transition-all duration-300 border border-transparent hover:border-white/20">
                          <div className={`${activity.color} p-3 rounded-xl bg-opacity-20 backdrop-blur-sm border border-current border-opacity-30`}>
                            <IconComponent className="h-5 w-5" />
                          </div>
                          <div className="flex-1 min-w-0">
                            <p className="text-white font-semibold">{activity.message}</p>
                            <p className="text-blue-300 text-sm font-medium mt-1">{activity.time}</p>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
                <div className="border-t border-white/20 px-6 py-4 bg-white/5">
                  <button className="text-blue-300 hover:text-white font-semibold transition-colors duration-300 text-sm">
                    Ver todas las actividades →
                  </button>
                </div>
              </div>

              {/* Quick Actions */}
              <div className="mt-6 bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">
                <h4 className="text-xl font-bold text-white mb-6">Acciones Rápidas</h4>
                <div className="space-y-4">
                  <button className="w-full text-left p-4 rounded-xl bg-blue-500/20 hover:bg-blue-500/30 transition-all duration-300 border border-blue-400/30 hover:border-blue-400/50 group">
                    <div className="flex items-center space-x-3">
                      <Bell className="h-5 w-5 text-blue-300 group-hover:text-blue-200" />
                      <span className="text-white font-semibold">Nuevo Comunicado</span>
                    </div>
                  </button>
                  <button className="w-full text-left p-4 rounded-xl bg-emerald-500/20 hover:bg-emerald-500/30 transition-all duration-300 border border-emerald-400/30 hover:border-emerald-400/50 group">
                    <div className="flex items-center space-x-3">
                      <CreditCard className="h-5 w-5 text-emerald-300 group-hover:text-emerald-200" />
                      <span className="text-white font-semibold">Generar Expensas</span>
                    </div>
                  </button>
                  <button className="w-full text-left p-4 rounded-xl bg-purple-500/20 hover:bg-purple-500/30 transition-all duration-300 border border-purple-400/30 hover:border-purple-400/50 group">
                    <div className="flex items-center space-x-3">
                      <Users className="h-5 w-5 text-purple-300 group-hover:text-purple-200" />
                      <span className="text-white font-semibold">Agregar Residente</span>
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </div>

          {/* Footer Info */}
          <div className="mt-16 relative">
            <div className="bg-gradient-to-r from-blue-600/20 to-purple-600/20 backdrop-blur-lg rounded-3xl p-8 border border-white/20">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-2xl font-bold text-white mb-3 flex items-center">
                    🤖 <span className="ml-2 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">Inteligencia Artificial Activa</span>
                  </h3>
                  <p className="text-blue-200 text-lg">
                    Reconocimiento facial, detección de vehículos y predicción de morosidad funcionando
                  </p>
                </div>
                <div className="flex items-center space-x-8">
                  <div className="text-center bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/20">
                    <p className="text-3xl font-black text-white">99.8%</p>
                    <p className="text-blue-300 font-semibold">Precisión IA</p>
                  </div>
                  <div className="text-center bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/20">
                    <p className="text-3xl font-black text-white">24/7</p>
                    <p className="text-blue-300 font-semibold">Monitoreo</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  );
}