import { useQuery } from "@tanstack/react-query";

import { obtenerComprasPorMes } from "../services/analytics.service";

export function useComprasPorMes() {
    return useQuery({
        queryKey: ["analytics", "compras-mes"],
        queryFn: obtenerComprasPorMes,
    });
}