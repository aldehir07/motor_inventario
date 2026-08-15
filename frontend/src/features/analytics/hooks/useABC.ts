import { useQuery } from "@tanstack/react-query";

import { obtenerABC } from "../services/analytics.service";

export function useABC() {
    return useQuery({
        queryKey: ["analytics", "abc"],
        queryFn: obtenerABC,
    });
}