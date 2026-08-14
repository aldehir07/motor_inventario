import { apiClient } from "../../../services/api/client";
import { tokenStorage } from "../../../services/auth/token";

import type { ApiResponse } from "../../../types/api";
import type {
  LoginRequest,
  LoginResponse,
  Usuario,
} from "../types/auth";

export async function login(
  request: LoginRequest,
): Promise<Usuario> {
  const response = await apiClient.post<
    ApiResponse<LoginResponse>
  >("/auth/login", request);

  const data = response.data.data;

  tokenStorage.setToken(data.access_token);
  tokenStorage.setStoredUser(data.usuario);

  return data.usuario;
}

export async function obtenerUsuarioActual(): Promise<Usuario> {
  const response = await apiClient.get<ApiResponse<Usuario>>(
    "/auth/me",
  );

  return response.data.data;
}

export function cerrarSesion(): void {
  tokenStorage.clear();
}