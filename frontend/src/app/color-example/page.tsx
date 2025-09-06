"use client";

import React from 'react';

/**
 * Ejemplos de uso de la paleta Resolution Blue en React/Next.js
 * Este componente demuestra cómo usar los colores correctamente
 */
export default function ColorExamplePage() {
  const colorShades = [
    { name: '50', class: 'bg-primary-50', textClass: 'text-primary-900' },
    { name: '100', class: 'bg-primary-100', textClass: 'text-primary-900' },
    { name: '200', class: 'bg-primary-200', textClass: 'text-primary-900' },
    { name: '300', class: 'bg-primary-300', textClass: 'text-primary-900' },
    { name: '400', class: 'bg-primary-400', textClass: 'text-white' },
    { name: '500', class: 'bg-primary-500', textClass: 'text-white' },
    { name: '600', class: 'bg-primary-600', textClass: 'text-white' },
    { name: '700', class: 'bg-primary-700', textClass: 'text-white' },
    { name: '800', class: 'bg-primary-800', textClass: 'text-white' },
    { name: '900', class: 'bg-primary-900', textClass: 'text-white' },
    { name: '950', class: 'bg-primary-950', textClass: 'text-white' },
  ];

  return (
    <div className="min-h-screen bg-primary-50">
      {/* Header */}
      <header className="bg-primary-950 text-primary-100 shadow-lg">
        <div className="container mx-auto px-6 py-4">
          <h1 className="text-2xl font-bold">Paleta Resolution Blue</h1>
          <p className="text-primary-300">Condominio Buganvillas</p>
        </div>
      </header>

      <div className="container mx-auto px-6 py-8">
        {/* Título principal */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-primary-900 mb-2">
            Condominio Buganvillas
          </h1>
          <p className="text-xl text-primary-700">
            Sistema de Gestión Inteligente
          </p>
        </div>

        {/* Cards de ejemplo */}
        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-primary-900 mb-6">
            Cards con la nueva paleta:
          </h2>

          {/* Card principal */}
          <div className="bg-gradient-to-br from-primary-50 to-primary-100 border border-primary-200 rounded-2xl p-6 shadow-lg mb-6">
            <div className="flex items-start space-x-4">
              <div className="bg-primary-500 p-3 rounded-xl">
                <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
              </div>
              <div>
                <h3 className="text-xl font-bold text-primary-900 mb-1">
                  Dashboard Principal
                </h3>
                <p className="text-primary-700">
                  Vista general del condominio
                </p>
              </div>
            </div>
          </div>

          {/* Grid de cards */}
          <div className="grid md:grid-cols-3 gap-6">
            <div className="bg-white border border-primary-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
              <div className="bg-primary-100 p-3 rounded-lg w-fit mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-primary-900 mb-2">Residentes</h3>
              <p className="text-primary-700">Gestiona la información de los residentes</p>
            </div>

            <div className="bg-white border border-primary-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
              <div className="bg-primary-100 p-3 rounded-lg w-fit mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-primary-900 mb-2">Pagos</h3>
              <p className="text-primary-700">Control de cuotas y pagos mensuales</p>
            </div>

            <div className="bg-white border border-primary-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
              <div className="bg-primary-100 p-3 rounded-lg w-fit mb-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-primary-900 mb-2">Seguridad</h3>
              <p className="text-primary-700">Sistema de acceso y vigilancia</p>
            </div>
          </div>
        </section>

        {/* Botones de ejemplo */}
        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-primary-900 mb-6">
            Botones con la nueva paleta:
          </h2>

          <div className="space-y-4 max-w-md">
            {/* Botón principal */}
            <button className="w-full bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 px-6 rounded-xl transition-colors duration-200 flex items-center justify-center space-x-2">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
              </svg>
              <span>Iniciar Sesión</span>
            </button>

            {/* Botón secundario */}
            <button className="w-full border-2 border-primary-300 text-primary-600 hover:bg-primary-50 font-semibold py-3 px-6 rounded-xl transition-colors duration-200 flex items-center justify-center space-x-2">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
              </svg>
              <span>Registrarse</span>
            </button>

            {/* Botón de texto */}
            <button className="w-full text-primary-600 hover:text-primary-700 font-semibold py-3 px-6 rounded-xl hover:bg-primary-50 transition-colors duration-200 flex items-center justify-center space-x-2">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>¿Necesitas ayuda?</span>
            </button>
          </div>
        </section>

        {/* Campos de entrada */}
        <section className="mb-12 max-w-md">
          <h2 className="text-2xl font-semibold text-primary-900 mb-6">
            Campos de entrada:
          </h2>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-primary-700 mb-2">
                Correo electrónico
              </label>
              <input
                type="email"
                placeholder="tu@email.com"
                className="w-full px-4 py-3 border border-primary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-primary-700 mb-2">
                Contraseña
              </label>
              <input
                type="password"
                placeholder="••••••••"
                className="w-full px-4 py-3 border border-primary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
              />
            </div>
          </div>
        </section>

        {/* Gradiente de fondo */}
        <section className="mb-12">
          <div className="bg-gradient-to-r from-primary-500 to-primary-700 rounded-2xl p-8 text-center text-white">
            <div className="bg-white/10 p-4 rounded-xl w-fit mx-auto mb-4">
              <svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <h3 className="text-2xl font-bold mb-2">Seguridad Inteligente</h3>
            <p className="text-primary-100">Con IA y reconocimiento facial</p>
          </div>
        </section>

        {/* Paleta de colores */}
        <section>
          <h2 className="text-2xl font-semibold text-primary-900 mb-6">
            Paleta de colores Resolution Blue:
          </h2>

          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            {colorShades.map((shade) => (
              <div
                key={shade.name}
                className={`${shade.class} border border-primary-200 rounded-lg p-4 text-center`}
              >
                <span className={`font-semibold ${shade.textClass}`}>
                  {shade.name}
                </span>
              </div>
            ))}
          </div>

          {/* Información adicional */}
          <div className="mt-8 bg-primary-50 border border-primary-200 rounded-xl p-6">
            <h3 className="text-lg font-semibold text-primary-900 mb-3">
              Uso de los colores:
            </h3>
            <ul className="space-y-2 text-primary-700">
              <li>• <strong>primary-50 a primary-200:</strong> Fondos suaves y elementos secundarios</li>
              <li>• <strong>primary-300 a primary-400:</strong> Bordes y elementos de separación</li>
              <li>• <strong>primary-500:</strong> Color principal para botones y enlaces</li>
              <li>• <strong>primary-600 a primary-700:</strong> Estados hover y elementos activos</li>
              <li>• <strong>primary-800 a primary-950:</strong> Textos principales y encabezados</li>
            </ul>
          </div>
        </section>
      </div>
    </div>
  );
}