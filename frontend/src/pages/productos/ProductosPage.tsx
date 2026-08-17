import {
  Alert,
  Box,
  CircularProgress,
  Typography,
} from "@mui/material";

import { useState } from "react";

import { useProductos } from "../../features/productos/hooks/useProductos";

import ProductosTable from "../../features/productos/components/ProductosTable";

import ProductosPagination from "../../features/productos/components/ProductosPagination";

import ProductoSearchBar from "../../features/productos/components/ProductoSearchBar";

import ProductoFilters from "../../features/productos/components/ProductoFilters";

function ProductosPage() {
  const [pagina, setPagina] = useState(1);

  const [busqueda, setBusqueda] =
    useState("");

  const [activo, setActivo] =
    useState<boolean | null>(true);

  const [precioMin, setPrecioMin] =
    useState("");

  const [precioMax, setPrecioMax] =
    useState("");

  const limite = 20;

  const {
    data,
    isLoading,
    isFetching,
    isError,
    error,
  } = useProductos({
    pagina,
    limite,
    busqueda:
      busqueda.trim() || undefined,
    activo: activo ?? undefined,
    precio_min:
      precioMin !== ""
        ? Number(precioMin)
        : undefined,
    precio_max:
      precioMax !== ""
        ? Number(precioMax)
        : undefined,
  });

  const handleBusquedaChange = (
    value: string,
  ) => {
    setBusqueda(value);
    setPagina(1);
  };

  const handleActivoChange = (
    value: boolean | null,
  ) => {
    setActivo(value);
    setPagina(1);
  };

  const handlePrecioMinChange = (
    value: string,
  ) => {
    setPrecioMin(value);
    setPagina(1);
  };

  const handlePrecioMaxChange = (
    value: string,
  ) => {
    setPrecioMax(value);
    setPagina(1);
  };

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

  const resultado = data?.data;

  const productos =
    resultado?.items ?? [];

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

      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          gap: 2,
          mb: 3,
        }}
      >
        <ProductoSearchBar
          value={busqueda}
          onChange={
            handleBusquedaChange
          }
        />

        <ProductoFilters
          activo={activo}
          precioMin={precioMin}
          precioMax={precioMax}
          onActivoChange={
            handleActivoChange
          }
          onPrecioMinChange={
            handlePrecioMinChange
          }
          onPrecioMaxChange={
            handlePrecioMaxChange
          }
        />
      </Box>

      {isFetching && (
        <Box sx={{ mb: 2 }}>
          <Typography
            variant="body2"
            color="text.secondary"
          >
            Actualizando resultados...
          </Typography>
        </Box>
      )}

      {productos.length === 0 ? (
        <Alert severity="info">
          No se encontraron productos
          con los filtros seleccionados.
        </Alert>
      ) : (
        <>
          <ProductosTable
            productos={productos}
          />

          {resultado && (
            <ProductosPagination
              pagina={resultado.pagina}
              paginas={resultado.paginas}
              total={resultado.total}
              limite={resultado.limite}
              onChange={setPagina}
            />
          )}
        </>
      )}
    </Box>
  );
}

export default ProductosPage;