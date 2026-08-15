import { useQuery } from "@tanstack/react-query";

import { obtenerRotacion } from "../services/analytics.service";

export function useRotacion() {
    return useQuery({
        queryKey: ["analytics", "rotacion"],
        queryFn: obtenerRotacion,
    });
}