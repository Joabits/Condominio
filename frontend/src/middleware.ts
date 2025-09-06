import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Rutas que requieren autenticación
const protectedRoutes = [
  '/dashboard',
  '/profile',
  '/settings',
  '/notifications',
  '/areas',
  '/payments',
  '/reports',
];

// Rutas que solo pueden acceder usuarios no autenticados
const authRoutes = ['/login'];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  
  // Verificar si el usuario tiene token de autenticación
  const token = request.cookies.get('access_token')?.value;
  const isAuthenticated = !!token;

  // Si la ruta requiere autenticación y el usuario no está autenticado
  if (protectedRoutes.some(route => pathname.startsWith(route)) && !isAuthenticated) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Si el usuario está autenticado y trata de acceder a rutas de auth
  if (authRoutes.some(route => pathname.startsWith(route)) && isAuthenticated) {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }

  // Redirigir la página raíz al dashboard si está autenticado, sino al login
  if (pathname === '/') {
    if (isAuthenticated) {
      return NextResponse.redirect(new URL('/dashboard', request.url));
    } else {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
};