import { useQuery } from "@tanstack/react-query";

import { listarProductos } from "../services/productos.service";

export function useProductos(
  pagina = 1,
  limite = 20,
) {
  return useQuery({
    queryKey: ["productos", pagina, limite],
    queryFn: () => listarProductos(pagina, limite),
  });
}