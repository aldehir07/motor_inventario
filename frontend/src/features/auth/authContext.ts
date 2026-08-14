import { createContext } from "react";

import type { LoginRequest, Usuario } from "./types/auth";

export interface AuthContextValue {
  usuario: Usuario | null;
  isAuthenticated: boolean;
  cargando: boolean;
  login: (request: LoginRequest) => Promise<void>;
  logout: () => void;
}

export const AuthContext = createContext<
  AuthContextValue | undefined
>(undefined);