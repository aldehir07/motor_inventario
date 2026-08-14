import { useCallback, useEffect, useMemo, useState } from "react";
import type { ReactNode } from "react";

import {
  cerrarSesion,
  login as loginService,
  obtenerUsuarioActual,
} from "./services/auth.service";
import { tokenStorage } from "../../services/auth/token";

import { AuthContext, type AuthContextValue } from "./authContext";
import type { LoginRequest, Usuario } from "./types/auth";

function AuthProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [usuario, setUsuario] = useState<Usuario | null>(null);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    let activo = true;

    if (!tokenStorage.getToken()) {
      setCargando(false);
      return;
    }

    obtenerUsuarioActual()
      .then((user) => {
        if (activo) {
          setUsuario(user);
        }
      })
      .catch(() => tokenStorage.clear())
      .finally(() => {
        if (activo) {
          setCargando(false);
        }
      });

    return () => {
      activo = false;
    };
  }, []);

  const login = useCallback(async (request: LoginRequest) => {
    const user = await loginService(request);
    setUsuario(user);
  }, []);

  const logout = useCallback(() => {
    cerrarSesion();
    setUsuario(null);
    window.location.assign("/login");
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({
      usuario,
      isAuthenticated: usuario !== null,
      cargando,
      login,
      logout,
    }),
    [usuario, cargando, login, logout],
  );

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export default AuthProvider;