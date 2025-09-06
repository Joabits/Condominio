/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Paleta principal del condominio Buganvillas - Resolution Blue
        primary: {
          50: '#e4f4ff',
          100: '#cfeaff',
          200: '#a8d6ff',
          300: '#74b9ff',
          400: '#3e88ff',
          500: '#135fff', // Color principal
          600: '#0044ff',
          700: '#0044ff',
          800: '#003de4',
          900: '#0029b0',
          950: '#001a80',
        },
        // Mantener algunos colores adicionales para estados
        success: {
          50: '#f0fdf4',
          500: '#22c55e',
          600: '#16a34a',
        },
        warning: {
          50: '#fffbeb',
          500: '#f59e0b',
          600: '#d97706',
        },
        error: {
          50: '#fef2f2',
          500: '#ef4444',
          600: '#dc2626',
        },
        // Grises neutros
        gray: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        }
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        'primary-gradient': 'linear-gradient(135deg, #135fff 0%, #0044ff 100%)',
        'primary-gradient-soft': 'linear-gradient(135deg, #cfeaff 0%, #a8d6ff 100%)',
      },
    },
  },
  plugins: [],
}