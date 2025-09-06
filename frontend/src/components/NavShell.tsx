'use client';

import { usePathname } from 'next/navigation';
import Navigation from '@/components/Navigation';

type Props = {
  children: React.ReactNode;
};

export default function NavShell({ children }: Props) {
  const pathname = usePathname();
  const hideNav = pathname === '/login' || pathname === '/access-denied';

  return (
    <>
      {!hideNav && <Navigation />}
      <main className="lg:ml-0">{children}</main>
    </>
  );
}
