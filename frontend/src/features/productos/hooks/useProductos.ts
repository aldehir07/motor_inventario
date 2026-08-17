import { useQuery } from "@tanstack/react-query";

import {
  listarProductos,
  type ListarProductosParams,
} from "../services/productos.service";

export function useProductos(
  params: ListarProductosParams = {},
) {
  return useQuery({
    queryKey: [
      "productos",
      params,
    ],

    queryFn: () =>
      listarProductos(params),

    placeholderData: (previousData) =>
      previousData,
  });
}