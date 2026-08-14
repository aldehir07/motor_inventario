export type RolUsuario = "ADMIN" | "USUARIO";

export interface Usuario {
  id: number;
  nombre_completo: string;
  email: string;
  rol: RolUsuario;
  activo: boolean;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  usuario: Usuario;
}