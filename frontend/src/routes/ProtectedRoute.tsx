import { Box, CircularProgress } from "@mui/material";
import { Navigate } from "react-router-dom";
import type { ReactNode } from "react";

import { useAuth } from "../features/auth/hooks/useAuth";

function ProtectedRoute({
  children,
}: {
  children: ReactNode;
}) {
  const { isAuthenticated, cargando } = useAuth();

  if (cargando) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          p: 6,
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}

export default ProtectedRoute;