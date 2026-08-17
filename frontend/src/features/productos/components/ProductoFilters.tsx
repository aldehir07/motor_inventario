import {
  Box,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";

interface ProductoFiltersProps {
  activo: boolean | null;
  precioMin: string;
  precioMax: string;

  onActivoChange: (
    value: boolean | null,
  ) => void;

  onPrecioMinChange: (
    value: string,
  ) => void;

  onPrecioMaxChange: (
    value: string,
  ) => void;
}

function ProductoFilters({
  activo,
  precioMin,
  precioMax,
  onActivoChange,
  onPrecioMinChange,
  onPrecioMaxChange,
}: ProductoFiltersProps) {
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