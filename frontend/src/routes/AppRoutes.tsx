import { Navigate, Route, Routes } from "react-router-dom";

import DashboardPage from "../pages/DashboardPage";
import LoginPage from "../pages/LoginPage";
import ProtectedRoute from "./ProtectedRoute";

import ProductosPage from "../pages/productos/ProductosPage";
import InventarioPage from "../pages/inventario/InventarioPage";
import ComprasPage from "../pages/compras/ComprasPage";
import VentasPage from "../pages/ventas/VentasPage";
import AnalyticsPage from "../pages/analytics/AnalyticsPage";
import MLPage from "../pages/ml/MLPage";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <DashboardPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/productos"
        element={
          <ProtectedRoute>
            <ProductosPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/inventario"
        element={
          <ProtectedRoute>
            <InventarioPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/compras"
        element={
          <ProtectedRoute>
            <ComprasPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/ventas"
        element={
          <ProtectedRoute>
            <VentasPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/analytics"
        element={
          <ProtectedRoute>
            <AnalyticsPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/ml"
        element={
          <ProtectedRoute>
            <MLPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="*"
        element={<Navigate to="/" replace />}
      />
    </Routes>
  );
}

export default AppRoutes;