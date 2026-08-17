import { apiClient } from "../../../services/api/client";

import type { Producto } from "../types/producto";

import type {
  ApiResponse,
  PaginatedResult,
} from "../../../types/api";

export interface ProductosFiltros {
  busqueda?: string;
  categoria_id?: number;
  proveedor_id?: number;
  marca_id?: number;
  unidad_medida_id?: number;
  activo?: boolean;
  precio_min?: number;
  precio_max?: number;
}

export interface ListarProductosParams
  extends ProductosFiltros {
  pagina?: number;
  limite?: number;
}

export async function listarProductos(
  params: ListarProductosParams = {},
): Promise<ApiResponse<PaginatedResult<Producto>>> {
  const response = await apiClient.get<
    ApiResponse<PaginatedResult<Producto>>
  >("/productos", {
    params,
  });

  return response.data;
}