import { useQuery } from "@tanstack/react-query";

import { obtenerVentasPorMes } from "../services/analytics.service";

export function useVentasPorMes() {
    return useQuery({
        queryKey: ["analytics", "ventas-mes"],
        queryFn: obtenerVentasPorMes,
    });
}