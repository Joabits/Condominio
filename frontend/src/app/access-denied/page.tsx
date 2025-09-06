'use client';

import { useRouter } from 'next/navigation';
import { Building2, Smartphone, AlertCircle, ArrowLeft } from 'lucide-react';

export default function AccessDeniedPage() {
  const router = useRouter();

  return (
    <div className="min-h-screen bg-gradient-to-br from-red-600 via-orange-600 to-red-800 flex items-center justify-center p-4">
      <div className="max-w-md w-full space-y-8">
        {/* Header */}
        <div className="text-center">
          <div className="flex justify-center items-center mb-6">
            <AlertCircle className="h-16 w-16 text-white" />
          </div>
          <h2 className="text-3xl font-bold text-white">
            Acceso Denegado
          </h2>
          <p className="mt-2 text-red-100">
            Esta aplicación es solo para administradores
          </p>
        </div>

        {/* Content */}
        <div className="bg-white rounded-lg shadow-xl p-8">
          <div className="text-center space-y-6">
            {/* Error Message */}
            <div className="bg-red-50 border border-red-200 rounded-md p-4">
              <div className="flex items-center justify-center mb-2">
                <Building2 className="h-6 w-6 text-red-500" />
              </div>
              <h3 className="font-semibold text-red-800 mb-2">
                Solo Administradores
              </h3>
              <p className="text-red-700 text-sm">
                Esta aplicación web está diseñada únicamente para la administración del condominio.
              </p>
            </div>

            {/* Mobile App Info */}
            <div className="bg-blue-50 border border-blue-200 rounded-md p-4">
              <div className="flex items-center justify-center mb-2">
                <Smartphone className="h-6 w-6 text-blue-500" />
              </div>
              <h3 className="font-semibold text-blue-800 mb-2">
                ¿Eres Residente?
              </h3>
              <p className="text-blue-700 text-sm mb-3">
                Los propietarios, inquilinos y personal deben usar la <strong>aplicación móvil</strong> del condominio.
              </p>
              <div className="space-y-2">
                <div className="bg-white rounded p-2">
                  <p className="text-xs text-gray-600">
                    <strong>Aplicación Móvil disponible para:</strong>
                  </p>
                  <ul className="text-xs text-gray-500 mt-1 space-y-1">
                    <li>• Propietarios</li>
                    <li>• Inquilinos</li>
                    <li>• Personal de Seguridad</li>
                    <li>• Personal de Mantenimiento</li>
                  </ul>
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="space-y-3">
              <button
                onClick={() => router.back()}
                className="w-full flex items-center justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50"
              >
                <ArrowLeft className="h-4 w-4 mr-2" />
                Volver
              </button>
              
              <button
                onClick={() => router.push('/login')}
                className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
              >
                Ir al Login de Administrador
              </button>
            </div>

            {/* Contact Info */}
            <div className="bg-gray-50 rounded-md p-4">
              <p className="text-xs text-gray-600 text-center mb-2">
                <strong>¿Necesitas ayuda?</strong>
              </p>
              <div className="text-xs text-gray-500 space-y-1">
                <p>Contacta a la administración:</p>
                <p>📧 administracion@lastorres.com</p>
                <p>📞 +591 3 123-4567</p>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center">
          <p className="text-red-100 text-sm">
            Condominio Buganvillas - Sistema de Gestión v1.0
          </p>
        </div>
      </div>
    </div>
  );
}