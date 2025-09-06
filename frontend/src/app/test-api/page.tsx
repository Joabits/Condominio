'use client';

import { useState } from 'react';
import apiService from '../../services/api';

export default function TestApiPage() {
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const testResidentsAPI = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiService.getUsuarios();
      setResult(data);
      console.log('Residentes loaded:', data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error desconocido');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const testStatsAPI = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiService.getEstadisticas();
      setResult(data);
      console.log('Estadísticas loaded:', data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error desconocido');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Test API Connection</h1>
        
        <div className="bg-white rounded-lg shadow p-6">
          <div className="space-y-4">
            <button
              onClick={testResidentsAPI}
              disabled={loading}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
            >
              {loading ? 'Cargando...' : 'Test Usuarios API'}
            </button>
            
            <button
              onClick={testStatsAPI}
              disabled={loading}
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 disabled:opacity-50 ml-4"
            >
              {loading ? 'Cargando...' : 'Test Estadísticas API'}
            </button>
          </div>

          {error && (
            <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
              Error: {error}
            </div>
          )}

          {result && (
            <div className="mt-4">
              <h3 className="text-lg font-semibold mb-2">Resultado:</h3>
              <pre className="bg-gray-100 p-4 rounded overflow-auto max-h-96">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}