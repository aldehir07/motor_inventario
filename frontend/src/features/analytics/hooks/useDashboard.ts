import { useQuery } from "@tanstack/react-query";

import { obtenerDashboard } from "../services/analytics.service";


export function useDashboard() {
  return useQuery({
    queryKey: ["analytics", "dashboard"],
    queryFn: obtenerDashboard,
  });
}