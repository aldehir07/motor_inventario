import {
  Box,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";

import { useCategorias, useMarcas, useProveedores, useUnidadesMedida } from "../../catalogos/hooks/useCatalogos";


interface ProductoFiltersProps {
  activo: boolean | null;

  precioMin: string;
  precioMax: string;

  categoriaId: number | null;
  proveedorId: number | null;
  marcaId: number | null;
  unidadMedidaId: number | null;

  onActivoChange: (
    value: boolean | null,
  ) => void;

  onPrecioMinChange: (
    value: string,
  ) => void;

  onPrecioMaxChange: (
    value: string,
  ) => void;

  onCategoriaChange: (
    value: number | null,
  ) => void;

  onProveedorChange: (
    value: number | null,
  ) => void;

  onMarcaChange: (
    value: number | null,
  ) => void;

  onUnidadMedidaChange: (
    value: number | null,
  ) => void;
}

function ProductoFilters({
  activo,
  precioMin,
  precioMax,
  categoriaId,
  marcaId,
  proveedorId,
  unidadMedidaId,
  onActivoChange,
  onPrecioMinChange,
  onPrecioMaxChange,
  onCategoriaChange,
  onMarcaChange,
  onProveedorChange,
  onUnidadMedidaChange,
}: ProductoFiltersProps) {

  const {
    data: categoriasData,
    isLoading: categoriasLoading,
  } = useCategorias();
  const {
    data: marcasData,
    isLoading: marcasLoading,
  } = useMarcas();
  const {
    data: proveedoresData,
    isLoading: proveedoresLoading,
  } = useProveedores();
  const {
    data: unidadesData,
    isLoading: unidadesLoading,
  } = useUnidadesMedida();
  const categorias = categoriasData?.data ?? [];
  const marcas = marcasData?.data ?? [];
  const proveedores = proveedoresData?.data ?? [];
  const unidades = unidadesData?.data ?? [];

  return (
    <Box
      sx={{
        display: "grid",
        gridTemplateColumns: {
          xs: "1fr",
          sm: "repeat(3, 1fr)",
        },
        gap: 2,
      }}
    >
      <FormControl fullWidth>
        <InputLabel id="estado-producto-label">
          Estado
        </InputLabel>

        <Select
          labelId="estado-producto-label"
          value={
            activo === null
              ? "todos"
              : activo
                ? "activos"
                : "inactivos"
          }
          label="Estado"
          onChange={(event) => {
            const value = event.target.value;

            if (value === "todos") {
              onActivoChange(null);
              return;
            }

            onActivoChange(
              value === "activos",
            );
          }}
        >
          <MenuItem value="activos">
            Activos
          </MenuItem>

          <MenuItem value="inactivos">
            Inactivos
          </MenuItem>

          <MenuItem value="todos">
            Todos
          </MenuItem>
        </Select>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="categoria-producto-label">
          Categoría
        </InputLabel>

        <Select<string | number>
          labelId="categoria-producto-label"
          value={categoriaId ?? ""}
          label="Categoría"
          disabled={categoriasLoading}
          onChange={(event) => {
            const value = event.target.value;

            onCategoriaChange(
              value === ""
                ? null
                : Number(value),
            );
          }}
        >
          <MenuItem value="">
            Todas
          </MenuItem>

          {categorias.map((categoria) => (
            <MenuItem
              key={categoria.id}
              value={categoria.id}
            >
              {categoria.nombre}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="marca-producto-label">
          Marca
        </InputLabel>

        <Select<string | number>
          labelId="marca-producto-label"
          value={marcaId ?? ""}
          label="Marca"
          disabled={marcasLoading}
          onChange={(event) => {
            const value = event.target.value;

            onMarcaChange(
              value === ""
                ? null
                : Number(value),
            );
          }}
        >
          <MenuItem value="">
            Todas
          </MenuItem>

          {marcas.map((marca) => (
            <MenuItem
              key={marca.id}
              value={marca.id}
            >
              {marca.nombre}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="proveedor-producto-label">
          Proveedor
        </InputLabel>

        <Select<string | number>
          labelId="proveedor-producto-label"
          value={proveedorId ?? ""}
          label="Proveedor"
          disabled={proveedoresLoading}
          onChange={(event) => {
            const value = event.target.value;

            onProveedorChange(
              value === ""
                ? null
                : Number(value),
            );
          }}
        >
          <MenuItem value="">
            Todos
          </MenuItem>

          {proveedores.map((proveedor) => (
            <MenuItem
              key={proveedor.id}
              value={proveedor.id}
            >
              {proveedor.nombre}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="unidad-medida-producto-label">
          Unidad de medida
        </InputLabel>

        <Select<string | number>
          labelId="unidad-medida-producto-label"
          value={unidadMedidaId ?? ""}
          label="Unidad de medida"
          disabled={unidadesLoading}
          onChange={(event) => {
            const value = event.target.value;

            onUnidadMedidaChange(
              value === ""
                ? null
                : Number(value),
            );
          }}
        >
          <MenuItem value="">
            Todas
          </MenuItem>

          {unidades.map((unidad) => (
            <MenuItem
              key={unidad.id}
              value={unidad.id}
            >
              {unidad.nombre} ({unidad.abreviatura})
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <TextField
        fullWidth
        label="Precio mínimo"
        type="number"
        value={precioMin}
        onChange={(event) =>
          onPrecioMinChange(
            event.target.value,
          )
        }
        slotProps={{
          htmlInput: {
            min: 0,
            step: "0.01",
          },
        }}
      />

      <TextField
        fullWidth
        label="Precio máximo"
        type="number"
        value={precioMax}
        onChange={(event) =>
          onPrecioMaxChange(
            event.target.value,
          )
        }
        slotProps={{
          htmlInput: {
            min: 0,
            step: "0.01",
          },
        }}
      />
    </Box>
  );
}

export default ProductoFilters;