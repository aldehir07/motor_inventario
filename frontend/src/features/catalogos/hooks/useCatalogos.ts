import { useQuery } from "@tanstack/react-query";

import {
    listarCategorias,
    listarMarcas,
    listarProveedores,
    listarUnidadesMedida,
} from "../services/catalogos.service";

export function useCategorias() {
    return useQuery({
        queryKey: ["catalogos", "categorias"],
        queryFn: listarCategorias,
    });
}

export function useMarcas() {
    return useQuery({
        queryKey: ["catalogos", "marcas"],
        queryFn: listarMarcas,
    });
}

export function useProveedores() {
    return useQuery({
        queryKey: ["catalogos", "proveedores"],
        queryFn: listarProveedores,
    });
}

export function useUnidadesMedida() {
    return useQuery({
        queryKey: ["catalogos", "unidades-medida"],
        queryFn: listarUnidadesMedida,
    });
}