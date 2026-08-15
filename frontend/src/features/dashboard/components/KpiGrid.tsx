import {
  Grid,
} from "@mui/material";

import KpiCard from "./KpiCard";

import type { DashboardResumen } from "../../analytics/types/analytics";

interface KpiGridProps {
  data: DashboardResumen;
}

function KpiGrid({
  data,
}: KpiGridProps) {
  const valorInventario = new Intl.NumberFormat(
    "es-PA",
    {
      style: "currency",
      currency: "USD",
      minimumFractionDigits: 2,
    }
  ).format(data.valor_inventario);

  return (
    <Grid
      container
      spacing={2}
    >
      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <KpiCard
          title="Productos"
          value={data.productos}
          description="Productos registrados"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <KpiCard
          title="Productos activos"
          value={data.productos_activos}
          description="Productos disponibles"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <KpiCard
          title="Stock bajo"
          value={data.stock_bajo}
          description="Requieren atención"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <KpiCard
          title="Sin stock"
          value={data.sin_stock}
          description="Productos agotados"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 4 }}>
        <KpiCard
          title="Valor del inventario"
          value={valorInventario}
          description="Valor actual del inventario"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 4 }}>
        <KpiCard
          title="Compras"
          value={data.compras}
          description="Compras registradas"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 12, md: 4 }}>
        <KpiCard
          title="Ventas"
          value={data.ventas}
          description="Ventas registradas"
        />
      </Grid>
    </Grid>
  );
}

export default KpiGrid;