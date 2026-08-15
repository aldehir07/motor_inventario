import {
  Alert,
  Box,
  Typography,
} from "@mui/material";

import { useDashboard } from "../features/analytics/hooks/useDashboard";
import { useVentasPorMes } from "../features/analytics/hooks/useVentasPorMes";
import { useComprasPorMes } from "../features/analytics/hooks/useComprasPorMes";
import { useRotacion } from "../features/analytics/hooks/useRotacion";
import { useABC } from "../features/analytics/hooks/useABC";

import KpiGrid from "../features/dashboard/components/KpiGrid";
import KpiGridSkeleton from "../features/dashboard/components/KpiGridSkeleton";

import VentasComprasChart from "../features/dashboard/components/charts/VentasComprasChart";
import VentasComprasChartSkeleton from "../features/dashboard/components/charts/VentasComprasChartSkeleton";

import RotacionTable from "../features/dashboard/components/analytics/RotacionTable";
import ABCChart from "../features/dashboard/components/analytics/ABCChart";
import AnalyticsSkeleton from "../features/dashboard/components/analytics/AnalyticsSkeleton";


function DashboardPage() {
  const dashboardQuery = useDashboard();

  const ventasQuery = useVentasPorMes();

  const comprasQuery = useComprasPorMes();

  const rotacionQuery = useRotacion();

  const abcQuery = useABC();


  const dashboard = dashboardQuery.data?.data;

  const ventas = ventasQuery.data?.data ?? [];

  const compras = comprasQuery.data?.data ?? [];

  const rotacion = rotacionQuery.data?.data ?? [];

  const abc = abcQuery.data?.data ?? [];


  return (
    <Box>
      <Box sx={{ mb: 4 }}>
        <Typography
          variant="h4"
          sx={{ fontWeight: "600" }}
          gutterBottom
        >
          Dashboard
        </Typography>

        <Typography
          variant="body1"
          color="text.secondary"
        >
          Resumen general del inventario.
        </Typography>
      </Box>


      {/* KPIs */}
      <Box>
        {dashboardQuery.isLoading && (
          <KpiGridSkeleton />
        )}

        {dashboardQuery.isError && (
          <Alert severity="error">
            No fue posible obtener los
            indicadores del dashboard.
          </Alert>
        )}

        {dashboard && (
          <KpiGrid data={dashboard} />
        )}
      </Box>


      {/* Ventas y compras */}
      <Box sx={{ mt: 3 }}>
        {(
          ventasQuery.isLoading ||
          comprasQuery.isLoading
        ) && (
            <VentasComprasChartSkeleton />
          )}

        {(
          ventasQuery.isError ||
          comprasQuery.isError
        ) && (
            <Alert severity="error">
              No fue posible obtener la
              información de ventas y compras.
            </Alert>
          )}

        {!ventasQuery.isLoading &&
          !comprasQuery.isLoading &&
          !ventasQuery.isError &&
          !comprasQuery.isError && (
            <VentasComprasChart
              ventas={ventas}
              compras={compras}
            />
          )}
      </Box>


      {/* Analytics de inventario */}
      <Box
        sx={{
          mt: 3,
          display: "grid",
          gridTemplateColumns: {
            xs: "1fr",
            lg: "1fr 1fr",
          },
          gap: 3,
        }}
      >
        {(
          rotacionQuery.isLoading ||
          abcQuery.isLoading
        ) && (
            <AnalyticsSkeleton />
          )}

        {(
          rotacionQuery.isError ||
          abcQuery.isError
        ) && (
            <Alert severity="error">
              No fue posible obtener los
              analytics de inventario.
            </Alert>
          )}

        {!rotacionQuery.isLoading &&
          !abcQuery.isLoading &&
          !rotacionQuery.isError &&
          !abcQuery.isError && (
            <>
              <ABCChart data={abc} />

              <RotacionTable
                data={rotacion}
              />
            </>
          )}
      </Box>
    </Box>
  );
}


export default DashboardPage;