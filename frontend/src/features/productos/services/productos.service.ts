import { apiClient } from "../../../services/api/client";

import type { Producto } from "../types/producto";

import type {
  ApiResponse,
  PaginatedResult,
} from "../../../types/api";

export async function listarProductos(
  pagina = 1,
  limite = 20,
): Promise<ApiResponse<PaginatedResult<Producto>>> {
  const response = await apiClient.get<
    ApiResponse<PaginatedResult<Producto>>
  >("/productos", {
    params: {
      pagina,
      limite,
    },
  });

  return response.data;
}