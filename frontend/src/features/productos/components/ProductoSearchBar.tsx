import {
  InputAdornment,
  TextField,
} from "@mui/material";

import SearchIcon from "@mui/icons-material/Search";

interface ProductoSearchBarProps {
  value: string;
  onChange: (value: string) => void;
}

function ProductoSearchBar({
  value,
  onChange,
}: ProductoSearchBarProps) {
  return (
    <TextField
      fullWidth
      label="Buscar productos"
      placeholder="Nombre, código o SKU"
      value={value}
      onChange={(event) =>
        onChange(event.target.value)
      }
      slotProps={{
        input: {
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        },
      }}
    />
  );
}

export default ProductoSearchBar;