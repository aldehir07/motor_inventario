import { apiClient } from "../../../services/api/client";

import type { ApiResponse } from "../../../types/api";

import type {
    CatalogoItem,
    Proveedor,
    UnidadMedida,
} from "../types/catalogo";

export async function listarCategorias(): Promise<
    ApiResponse<CatalogoItem[]>
> {
    const response = await apiClient.get<
        ApiResponse<CatalogoItem[]>
    >("/catalogos/categorias");

    return response.data;
}

export async function listarMarcas(): Promise<
    ApiResponse<CatalogoItem[]>
> {
    const response = await apiClient.get<
        ApiResponse<CatalogoItem[]>
    >("/catalogos/marcas");

    return response.data;
}

export async function listarProveedores(): Promise<
    ApiResponse<Proveedor[]>
> {
    const response = await apiClient.get<
        ApiResponse<Proveedor[]>
    >("/catalogos/proveedores");

    return response.data;
}

export async function listarUnidadesMedida(): Promise<
    ApiResponse<UnidadMedida[]>
> {
    const response = await apiClient.get<
        ApiResponse<UnidadMedida[]>
    >("/catalogos/unidades-medida");

    return response.data;
}