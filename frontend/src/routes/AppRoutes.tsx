import { Navigate, Route, Routes } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import LoginPage from "../pages/LoginPage";
import DashboardPage from "../pages/DashboardPage";

import ProductosPage from "../pages/productos/ProductosPage";
import InventarioPage from "../pages/inventario/InventarioPage";
import ComprasPage from "../pages/compras/ComprasPage";
import VentasPage from "../pages/ventas/VentasPage";
import AnalyticsPage from "../pages/analytics/AnalyticsPage";
import MLPage from "../pages/ml/MLPage";

function AppRoutes() {
  return (
    <Routes>
      <Route
        path="/login"
        element={<LoginPage />}
      />

      <Route element={<MainLayout />}>
        <Route
          path="/"
          element={<DashboardPage />}
        />

        <Route
          path="/productos"
          element={<ProductosPage />}
        />

        <Route
          path="/inventario"
          element={<InventarioPage />}
        />

        <Route
          path="/compras"
          element={<ComprasPage />}
        />

        <Route
          path="/ventas"
          element={<VentasPage />}
        />

        <Route
          path="/analytics"
          element={<AnalyticsPage />}
        />

        <Route
          path="/ml"
          element={<MLPage />}
        />
      </Route>

      <Route
        path="*"
        element={<Navigate to="/" replace />}
      />
    </Routes>
  );
}

export default AppRoutes;