import {
  Alert,
  Box,
  Button,
  CircularProgress,
  Typography,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

import { useState } from "react";

import { useProductos } from "../../features/productos/hooks/useProductos";

import ProductosTable from "../../features/productos/components/ProductosTable";

import ProductosPagination from "../../features/productos/components/ProductosPagination";

import ProductoSearchBar from "../../features/productos/components/ProductoSearchBar";

import ProductoFilters from "../../features/productos/components/ProductoFilters";

import { useDebouncedValue } from "../../features/productos/hooks/useDebouncedValue";
import ProductoCreateDialog from "../../features/productos/components/ProductoCreateDialog";
import type { Producto } from "../../features/productos/types/producto";
import ProductoEditDialog from "../../features/productos/components/ProductoEditDialog";

function ProductosPage() {
  const [openCreateDialog, setOpenCreateDialog] = useState(false);
  const [productoEditar, setProductoEditar] = useState<Producto | null>(null);
  const [pagina, setPagina] = useState(1);

  const [busqueda, setBusqueda] =
    useState("");

  const busquedaDebounced = useDebouncedValue(busqueda, 400,);

  const [activo, setActivo] =
    useState<boolean | null>(true);

  const [precioMin, setPrecioMin] =
    useState("");

  const [precioMax, setPrecioMax] =
    useState("");

  const [categoriaId, setCategoriaId] =
    useState<number | null>(null);

  const [proveedorId, setProveedorId] =
    useState<number | null>(null);

  const [marcaId, setMarcaId] =
    useState<number | null>(null);

  const [unidadMedidaId, setUnidadMedidaId] =
    useState<number | null>(null);

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
      busquedaDebounced.trim() || undefined,

    categoria_id: categoriaId ?? undefined,
    proveedor_id: proveedorId ?? undefined,
    marca_id: marcaId ?? undefined,
    unidad_medida_id: unidadMedidaId ?? undefined,

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

  const handleCategoriaChange = (
    value: number | null,
  ) => {
    setCategoriaId(value);
    setPagina(1);
  };

  const handleProveedorChange = (
    value: number | null,
  ) => {
    setProveedorId(value);
    setPagina(1);
  };

  const handleMarcaChange = (
    value: number | null,
  ) => {
    setMarcaId(value);
    setPagina(1);
  };

  const handleUnidadMedidaChange = (
    value: number | null,
  ) => {
    setUnidadMedidaId(value);
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

  const handleEditarProducto = (
    producto: Producto,
  ) => {
    setProductoEditar(producto)
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
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
          mb: 3,
        }}
      >
        <Box>
          <Typography
            variant="h4"
            gutterBottom
            sx={{ fontWeight: "bold" }}
          >
            Productos
          </Typography>
          <Typography color="text.secondary">
            Productos registrados en el sistema.
          </Typography>
        </Box>
        <Button
          variant="contained"
          color="primary"
          startIcon={<AddIcon />}
          onClick={() => setOpenCreateDialog(true)}
        >
          Nuevo Producto
        </Button>
      </Box>

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

          categoriaId={categoriaId}
          proveedorId={proveedorId}
          marcaId={marcaId}
          unidadMedidaId={unidadMedidaId}

          onActivoChange={
            handleActivoChange
          }
          onPrecioMinChange={
            handlePrecioMinChange
          }
          onPrecioMaxChange={
            handlePrecioMaxChange
          }
          onCategoriaChange={
            handleCategoriaChange
          }

          onProveedorChange={
            handleProveedorChange
          }

          onMarcaChange={
            handleMarcaChange
          }

          onUnidadMedidaChange={
            handleUnidadMedidaChange
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
            onEditar={handleEditarProducto}
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
      <ProductoCreateDialog
        open={openCreateDialog}
        onClose={() => setOpenCreateDialog(false)}
      />

      <ProductoEditDialog
        open={productoEditar !== null}
        producto={productoEditar}
        onClose={() =>
          setProductoEditar(null)
        }
      />

    </Box>
  );
}

export default ProductosPage;