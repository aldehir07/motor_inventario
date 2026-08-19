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

export interface ListarProductosParams {
  pagina?: number;
  limite?: number;

  busqueda?: string;

  categoria_id?: number;
  proveedor_id?: number;
  marca_id?: number;
  unidad_medida_id?: number;

  activo?: boolean;

  precio_min?: number;
  precio_max?: number;
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

export interface ProductoCreateInput {
  categoria_id: number;
  proveedor_id: number;
  marca_id: number;
  unidad_medida_id: number;
  codigo: string;
  sku: string;
  nombre: string;
  descripcion?: string | null;
  precio_compra_actual: number;
  precio_venta_actual: number;
  stock_minimo: number;
  stock_maximo: number;
}

export async function crearProducto(
  input: ProductoCreateInput,
): Promise<ApiResponse<Producto>> {
  const response = await apiClient.post<ApiResponse<Producto>>(
    "/productos",
    input,
  );
  return response.data;
}


export interface ProductoUpdateInput {
  nombre?: string;
  descripcion?: string | null;
  precio_compra_actual?: number;
  precio_venta_actual?: number;
  stock_minimo?: number;
  stock_maximo?: number;
  activo?: boolean;
}

export async function actualizarProducto(
  productoId: number,
  input: ProductoUpdateInput,
): Promise<ApiResponse<Producto>> {
  const response = await apiClient.put<
    ApiResponse<Producto>
  >(
    `/productos/${productoId}`,
    input,
  );

  return response.data;
}