import {
  Alert,
  Box,
  CircularProgress,
  List,
  ListItem,
  Typography,
} from "@mui/material";

import { useProductos } from "../../features/productos/hooks/useProductos";

function ProductosPage() {
  const {
    data,
    isLoading,
    isError,
    error,
  } = useProductos();

  if (isLoading) {
    return (
      <Box sx={{ p: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (isError) {
    return (
      <Box sx={{ p: 4 }}>
        <Alert severity="error">
          Error al obtener los productos:{" "}
          {error.message}
        </Alert>
      </Box>
    );
  }

  const productos = data?.data.items ?? [];

  return (
    <Box sx={{ p: 4 }}>
      <Typography
        variant="h4"
        gutterBottom
      >
        Productos
      </Typography>

      <Typography
        color="text.secondary"
        sx={{ mb: 3 }}
      >
        Productos registrados en el sistema.
      </Typography>

      <List>
        {productos.map((producto) => (
          <ListItem key={producto.id}>
            {producto.codigo} - {producto.nombre}
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default ProductosPage;