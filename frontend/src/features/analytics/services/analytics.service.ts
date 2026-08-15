import { apiClient } from "../../../services/api/client";

import type {
  ABCProducto,
  CompraPorMes,
  DashboardResumen,
  RotacionInventario,
  VentaPorMes,
} from "../types/analytics";

import type {
  ApiResponse,
} from "../../../types/api";


export async function obtenerDashboard(): Promise<
  ApiResponse<DashboardResumen>
> {
  const response = await apiClient.get<
    ApiResponse<DashboardResumen>
  >("/analytics/dashboard");

  return response.data;
}


export async function obtenerVentasPorMes(): Promise<
  ApiResponse<VentaPorMes[]>
> {
  const response = await apiClient.get<
    ApiResponse<VentaPorMes[]>
  >("/analytics/ventas-mes");

  return response.data;
}


export async function obtenerComprasPorMes(): Promise<
  ApiResponse<CompraPorMes[]>
> {
  const response = await apiClient.get<
    ApiResponse<CompraPorMes[]>
  >("/analytics/compras-mes");

  return response.data;
}


export async function obtenerRotacion(): Promise<
  ApiResponse<RotacionInventario[]>
> {
  const response = await apiClient.get<
    ApiResponse<RotacionInventario[]>
  >("/analytics/rotacion");

  return response.data;
}


export async function obtenerABC(): Promise<
  ApiResponse<ABCProducto[]>
> {
  const response = await apiClient.get<
    ApiResponse<ABCProducto[]>
  >("/analytics/abc");

  return response.data;
}