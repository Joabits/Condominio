"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function DashboardPage() {
  const router = useRouter();

  useEffect(() => {
    // Redirigir a la página principal
    router.replace('/');
  }, [router]);

  return null;
}