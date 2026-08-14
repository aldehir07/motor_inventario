import { Button, Box, Typography } from "@mui/material";

import { useAuth } from "../features/auth/hooks/useAuth";

function DashboardPage() {
  const { usuario, logout } = useAuth();

  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Box>
          <Typography variant="h4">Dashboard</Typography>

          <Typography color="text.secondary">
            Resumen general del sistema.
          </Typography>
        </Box>

        <Box sx={{ textAlign: "right" }}>
          <Typography variant="body2">
            {usuario?.email}
          </Typography>
          <Typography variant="caption" color="text.secondary">
            {usuario?.rol}
          </Typography>
          <Box>
            <Button
              size="small"
              onClick={logout}
              sx={{ mt: 1 }}
            >
              Cerrar sesión
            </Button>
          </Box>
        </Box>
      </Box>
    </Box>
  );
}

export default DashboardPage;