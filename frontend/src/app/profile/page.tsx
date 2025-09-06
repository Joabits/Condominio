'use client';

import { useState, useEffect } from 'react';
import Navigation from '../../components/Navigation';
import apiService, { PerfilUsuario } from '../../services/api';
import { 
  User,
  Mail,
  Phone,
  MapPin,
  Calendar,
  Shield,
  Edit,
  Save,
  X,
  Camera,
  Key,
  Bell,
  Settings,
  CreditCard,
  Building,
  Users,
  AlertCircle,
  CheckCircle,
  Loader
} from 'lucide-react';

export default function ProfilePage() {
  const [userProfile, setUserProfile] = useState<PerfilUsuario | null>(null);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState('profile');

  // Estado para el formulario de edición
  const [editForm, setEditForm] = useState({
    first_name: '',
    last_name: '',
    email: '',
    telefono: '',
    ci: ''
  });

  // Estado para cambio de contraseña
  const [passwordForm, setPasswordForm] = useState({
    current_password: '',
    new_password: '',
    confirm_password: ''
  });

  useEffect(() => {
    loadUserProfile();
  }, []);

  const loadUserProfile = async () => {
    try {
      setLoading(true);
      // Por ahora usaremos datos simulados del administrador
      // En una implementación real, obtendrías el perfil del usuario autenticado
      const usuarios = await apiService.getUsuarios();
      const adminUser = usuarios.find(u => u.tipo_usuario.tipo === 'ADMINISTRADOR');
      
      if (adminUser) {
        setUserProfile(adminUser);
        setEditForm({
          first_name: adminUser.user.first_name,
          last_name: adminUser.user.last_name,
          email: adminUser.user.email,
          telefono: adminUser.telefono || '',
          ci: adminUser.ci
        });
      }
      setError(null);
    } catch (err) {
      setError('Error al cargar el perfil');
      console.error('Error loading profile:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = () => {
    setEditing(true);
    setError(null);
    setSuccess(null);
  };

  const handleCancel = () => {
    setEditing(false);
    if (userProfile) {
      setEditForm({
        first_name: userProfile.user.first_name,
        last_name: userProfile.user.last_name,
        email: userProfile.user.email,
        telefono: userProfile.telefono || '',
        ci: userProfile.ci
      });
    }
  };

  const handleSave = async () => {
    try {
      setSaving(true);
      setError(null);
      
      // Aquí implementarías la actualización del perfil
      // await apiService.updateUserProfile(userProfile.id, editForm);
      
      // Simulación de guardado exitoso
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      setSuccess('Perfil actualizado correctamente');
      setEditing(false);
      
      // Recargar el perfil
      await loadUserProfile();
    } catch (err) {
      setError('Error al actualizar el perfil');
      console.error('Error updating profile:', err);
    } finally {
      setSaving(false);
    }
  };

  const handlePasswordChange = async () => {
    if (passwordForm.new_password !== passwordForm.confirm_password) {
      setError('Las contraseñas no coinciden');
      return;
    }

    try {
      setSaving(true);
      setError(null);
      
      // Aquí implementarías el cambio de contraseña
      // await apiService.changePassword(passwordForm);
      
      // Simulación de cambio exitoso
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      setSuccess('Contraseña cambiada correctamente');
      setPasswordForm({
        current_password: '',
        new_password: '',
        confirm_password: ''
      });
    } catch (err) {
      setError('Error al cambiar la contraseña');
      console.error('Error changing password:', err);
    } finally {
      setSaving(false);
    }
  };

  const tabs = [
    { id: 'profile', name: 'Perfil', icon: User },
    { id: 'security', name: 'Seguridad', icon: Shield },
    { id: 'notifications', name: 'Notificaciones', icon: Bell },
    { id: 'preferences', name: 'Preferencias', icon: Settings }
  ];

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Navigation />
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-center h-64">
            <Loader className="h-8 w-8 animate-spin text-blue-600" />
          </div>
        </div>
      </div>
    );
  }

  if (error && !userProfile) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Navigation />
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <AlertCircle className="h-12 w-12 text-red-600 mx-auto mb-4" />
            <p className="text-gray-600">{error}</p>
            <button 
              onClick={loadUserProfile}
              className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
            >
              Reintentar
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation user={{
        name: userProfile ? `${userProfile.user.first_name} ${userProfile.user.last_name}` : 'Usuario',
        email: userProfile ? userProfile.user.email : '',
        role: userProfile ? userProfile.tipo_usuario.tipo : 'Administrador'
      }} />
      
      <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Mi Perfil</h1>
          <p className="mt-2 text-gray-600">Gestiona tu información personal y configuración de cuenta</p>
        </div>

        {/* Alerts */}
        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 rounded-lg p-4">
            <div className="flex">
              <AlertCircle className="h-5 w-5 text-red-400" />
              <div className="ml-3">
                <p className="text-sm text-red-800">{error}</p>
              </div>
              <button
                onClick={() => setError(null)}
                className="ml-auto text-red-400 hover:text-red-600"
              >
                <X className="h-5 w-5" />
              </button>
            </div>
          </div>
        )}

        {success && (
          <div className="mb-6 bg-green-50 border border-green-200 rounded-lg p-4">
            <div className="flex">
              <CheckCircle className="h-5 w-5 text-green-400" />
              <div className="ml-3">
                <p className="text-sm text-green-800">{success}</p>
              </div>
              <button
                onClick={() => setSuccess(null)}
                className="ml-auto text-green-400 hover:text-green-600"
              >
                <X className="h-5 w-5" />
              </button>
            </div>
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
              {/* Profile Summary */}
              <div className="text-center mb-6">
                <div className="w-20 h-20 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
                  <User className="h-10 w-10 text-white" />
                </div>
                <h3 className="text-lg font-semibold text-gray-900">
                  {userProfile ? `${userProfile.user.first_name} ${userProfile.user.last_name}` : 'Usuario'}
                </h3>
                <p className="text-sm text-gray-500">
                  {userProfile ? userProfile.tipo_usuario.tipo : 'Administrador'}
                </p>
                <p className="text-sm text-gray-500">
                  {userProfile ? userProfile.condominio.nombre : 'Condominio Buganvillas'}
                </p>
              </div>

              {/* Navigation Tabs */}
              <nav className="space-y-1">
                {tabs.map((tab) => (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`w-full flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                      activeTab === tab.id
                        ? 'bg-blue-50 text-blue-700 border-r-2 border-blue-700'
                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                    }`}
                  >
                    <tab.icon className="h-4 w-4 mr-3" />
                    {tab.name}
                  </button>
                ))}
              </nav>
            </div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200">
              {/* Profile Tab */}
              {activeTab === 'profile' && (
                <div className="p-6">
                  <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold text-gray-900">Información Personal</h2>
                    {!editing ? (
                      <button
                        onClick={handleEdit}
                        className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                      >
                        <Edit className="h-4 w-4 mr-2" />
                        Editar
                      </button>
                    ) : (
                      <div className="flex space-x-2">
                        <button
                          onClick={handleCancel}
                          className="flex items-center px-4 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 transition-colors"
                        >
                          <X className="h-4 w-4 mr-2" />
                          Cancelar
                        </button>
                        <button
                          onClick={handleSave}
                          disabled={saving}
                          className="flex items-center px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors disabled:opacity-50"
                        >
                          {saving ? (
                            <Loader className="h-4 w-4 mr-2 animate-spin" />
                          ) : (
                            <Save className="h-4 w-4 mr-2" />
                          )}
                          Guardar
                        </button>
                      </div>
                    )}
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Nombre
                      </label>
                      {editing ? (
                        <input
                          type="text"
                          value={editForm.first_name}
                          onChange={(e) => setEditForm({ ...editForm, first_name: e.target.value })}
                          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                      ) : (
                        <p className="text-gray-900">{userProfile?.user.first_name}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Apellido
                      </label>
                      {editing ? (
                        <input
                          type="text"
                          value={editForm.last_name}
                          onChange={(e) => setEditForm({ ...editForm, last_name: e.target.value })}
                          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                      ) : (
                        <p className="text-gray-900">{userProfile?.user.last_name}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Email
                      </label>
                      {editing ? (
                        <input
                          type="email"
                          value={editForm.email}
                          onChange={(e) => setEditForm({ ...editForm, email: e.target.value })}
                          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                      ) : (
                        <p className="text-gray-900">{userProfile?.user.email}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Teléfono
                      </label>
                      {editing ? (
                        <input
                          type="tel"
                          value={editForm.telefono}
                          onChange={(e) => setEditForm({ ...editForm, telefono: e.target.value })}
                          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                      ) : (
                        <p className="text-gray-900">{userProfile?.telefono || 'No especificado'}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Cédula de Identidad
                      </label>
                      {editing ? (
                        <input
                          type="text"
                          value={editForm.ci}
                          onChange={(e) => setEditForm({ ...editForm, ci: e.target.value })}
                          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                      ) : (
                        <p className="text-gray-900">{userProfile?.ci}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Rol
                      </label>
                      <p className="text-gray-900">{userProfile?.tipo_usuario.tipo}</p>
                    </div>

                    <div className="md:col-span-2">
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Condominio
                      </label>
                      <p className="text-gray-900">{userProfile?.condominio.nombre}</p>
                      <p className="text-sm text-gray-500">{userProfile?.condominio.direccion}</p>
                    </div>
                  </div>
                </div>
              )}

              {/* Security Tab */}
              {activeTab === 'security' && (
                <div className="p-6">
                  <h2 className="text-xl font-semibold text-gray-900 mb-6">Seguridad</h2>
                  
                  <div className="space-y-6">
                    <div className="bg-gray-50 rounded-lg p-4">
                      <h3 className="text-lg font-medium text-gray-900 mb-4">Cambiar Contraseña</h3>
                      
                      <div className="space-y-4">
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-2">
                            Contraseña Actual
                          </label>
                          <input
                            type="password"
                            value={passwordForm.current_password}
                            onChange={(e) => setPasswordForm({ ...passwordForm, current_password: e.target.value })}
                            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                          />
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-2">
                            Nueva Contraseña
                          </label>
                          <input
                            type="password"
                            value={passwordForm.new_password}
                            onChange={(e) => setPasswordForm({ ...passwordForm, new_password: e.target.value })}
                            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                          />
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-2">
                            Confirmar Nueva Contraseña
                          </label>
                          <input
                            type="password"
                            value={passwordForm.confirm_password}
                            onChange={(e) => setPasswordForm({ ...passwordForm, confirm_password: e.target.value })}
                            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                          />
                        </div>

                        <button
                          onClick={handlePasswordChange}
                          disabled={saving || !passwordForm.current_password || !passwordForm.new_password || !passwordForm.confirm_password}
                          className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
                        >
                          {saving ? (
                            <Loader className="h-4 w-4 mr-2 animate-spin" />
                          ) : (
                            <Key className="h-4 w-4 mr-2" />
                          )}
                          Cambiar Contraseña
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* Notifications Tab */}
              {activeTab === 'notifications' && (
                <div className="p-6">
                  <h2 className="text-xl font-semibold text-gray-900 mb-6">Notificaciones</h2>
                  <p className="text-gray-600">Configuración de notificaciones en desarrollo...</p>
                </div>
              )}

              {/* Preferences Tab */}
              {activeTab === 'preferences' && (
                <div className="p-6">
                  <h2 className="text-xl font-semibold text-gray-900 mb-6">Preferencias</h2>
                  <p className="text-gray-600">Configuración de preferencias en desarrollo...</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}