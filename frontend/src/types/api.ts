export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message: string;
}

export interface PaginatedResult<T> {
  items: T[];
  total: number;
  pagina: number;
  limite: number;
  paginas: number;
}

export interface ApiError {
  success: boolean;
  error: string;
  message: string;
}