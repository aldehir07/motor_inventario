import { useState } from "react";
import {
  Alert,
  Button,
  CircularProgress,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControl,
  FormHelperText,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import {
  useCategorias,
  useMarcas,
  useProveedores,
  useUnidadesMedida,
} from "../../catalogos/hooks/useCatalogos";
import { crearProducto, type ProductoCreateInput } from "../services/productos.service";

interface ProductoCreateDialogProps {
  open: boolean;
  onClose: () => void;
}

export default function ProductoCreateDialog({
  open,
  onClose,
}: ProductoCreateDialogProps) {
  const queryClient = useQueryClient();

  // Estado del formulario
  const [codigo, setCodigo] = useState("");
  const [sku, setSku] = useState("");
  const [nombre, setNombre] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [categoriaId, setCategoriaId] = useState<string | number>("");
  const [proveedorId, setProveedorId] = useState<string | number>("");
  const [marcaId, setMarcaId] = useState<string | number>("");
  const [unidadMedidaId, setUnidadMedidaId] = useState<string | number>("");
  const [precioCompra, setPrecioCompra] = useState("");
  const [precioVenta, setPrecioVenta] = useState("");
  const [stockMinimo, setStockMinimo] = useState("0");
  const [stockMaximo, setStockMaximo] = useState("100");

  // Estado de errores
  const [formErrors, setFormErrors] = useState<Record<string, string>>({});
  const [generalError, setGeneralError] = useState<string | null>(null);

  // Obtener opciones de los catálogos
  const { data: categoriasData, isLoading: catLoading } = useCategorias();
  const { data: marcasData, isLoading: marLoading } = useMarcas();
  const { data: proveedoresData, isLoading: provLoading } = useProveedores();
  const { data: unidadesData, isLoading: uniLoading } = useUnidadesMedida();

  const categorias = categoriasData?.data ?? [];
  const marcas = marcasData?.data ?? [];
  const proveedores = proveedoresData?.data ?? [];
  const unidades = unidadesData?.data ?? [];

  // Resetear formulario
  const handleReset = () => {
    setCodigo("");
    setSku("");
    setNombre("");
    setDescripcion("");
    setCategoriaId("");
    setProveedorId("");
    setMarcaId("");
    setUnidadMedidaId("");
    setPrecioCompra("");
    setPrecioVenta("");
    setStockMinimo("0");
    setStockMaximo("100");
    setFormErrors({});
    setGeneralError(null);
  };

  const handleClose = () => {
    handleReset();
    onClose();
  };

  // Mutación para creación
  const mutation = useMutation({
    mutationFn: crearProducto,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["productos"] });
      handleClose();
    },
    onError: (err: any) => {
      const msg = err.response?.data?.message || err.message || "Ocurrió un error inesperado al guardar.";
      setGeneralError(msg);
    },
  });

  // Validaciones del formulario
  const validate = (): boolean => {
    const errors: Record<string, string> = {};

    if (!codigo.trim()) errors.codigo = "El código es requerido.";
    else if (codigo.length > 30) errors.codigo = "El código no debe exceder 30 caracteres.";

    if (!sku.trim()) errors.sku = "El SKU es requerido.";
    else if (sku.length > 50) errors.sku = "El SKU no debe exceder 50 caracteres.";

    if (!nombre.trim()) errors.nombre = "El nombre es requerido.";
    else if (nombre.length > 150) errors.nombre = "El nombre no debe exceder 150 caracteres.";

    if (categoriaId === "") errors.categoriaId = "La categoría es requerida.";
    if (proveedorId === "") errors.proveedorId = "El proveedor es requerido.";
    if (marcaId === "") errors.marcaId = "La marca es requerida.";
    if (unidadMedidaId === "") errors.unidadMedidaId = "La unidad de medida es requerida.";

    const pCompra = Number(precioCompra);
    if (!precioCompra.trim()) {
      errors.precioCompra = "El precio de compra es requerido.";
    } else if (isNaN(pCompra) || pCompra <= 0) {
      errors.precioCompra = "El precio debe ser un número mayor a 0.";
    }

    const pVenta = Number(precioVenta);
    if (!precioVenta.trim()) {
      errors.precioVenta = "El precio de venta es requerido.";
    } else if (isNaN(pVenta) || pVenta <= 0) {
      errors.precioVenta = "El precio debe ser un número mayor a 0.";
    }

    const sMin = Number(stockMinimo);
    if (!stockMinimo.trim()) {
      errors.stockMinimo = "El stock mínimo es requerido.";
    } else if (isNaN(sMin) || sMin < 0) {
      errors.stockMinimo = "El stock mínimo debe ser mayor o igual a 0.";
    }

    const sMax = Number(stockMaximo);
    if (!stockMaximo.trim()) {
      errors.stockMaximo = "El stock máximo es requerido.";
    } else if (isNaN(sMax) || sMax < 0) {
      errors.stockMaximo = "El stock máximo debe ser mayor o igual a 0.";
    }

    if (!errors.stockMinimo && !errors.stockMaximo && sMin > sMax) {
      errors.stockMinimo = "El stock mínimo no puede superar al stock máximo.";
      errors.stockMaximo = "El stock máximo no puede ser menor al stock mínimo.";
    }

    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setGeneralError(null);

    if (!validate()) return;

    const payload: ProductoCreateInput = {
      categoria_id: Number(categoriaId),
      proveedor_id: Number(proveedorId),
      marca_id: Number(marcaId),
      unidad_medida_id: Number(unidadMedidaId),
      codigo: codigo.trim(),
      sku: sku.trim(),
      nombre: nombre.trim(),
      descripcion: descripcion.trim() || null,
      precio_compra_actual: Number(precioCompra),
      precio_venta_actual: Number(precioVenta),
      stock_minimo: Number(stockMinimo),
      stock_maximo: Number(stockMaximo),
    };

    mutation.mutate(payload);
  };

  const isPending = mutation.isPending;

  return (
    <Dialog open={open} onClose={isPending ? undefined : handleClose} maxWidth="md" fullWidth>
      <DialogTitle sx={{ fontWeight: "bold" }}>Crear Nuevo Producto</DialogTitle>
      <form onSubmit={handleSubmit}>
        <DialogContent dividers>
          {generalError && (
            <Alert severity="error" sx={{ mb: 3 }}>
              {generalError}
            </Alert>
          )}

          <Grid container spacing={2}>
            {/* Código */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="Código"
                value={codigo}
                disabled={isPending}
                error={!!formErrors.codigo}
                helperText={formErrors.codigo}
                onChange={(e) => setCodigo(e.target.value)}
              />
            </Grid>

            {/* SKU */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="SKU"
                value={sku}
                disabled={isPending}
                error={!!formErrors.sku}
                helperText={formErrors.sku}
                onChange={(e) => setSku(e.target.value)}
              />
            </Grid>

            {/* Nombre */}
            <Grid item xs={12}>
              <TextField
                fullWidth
                label="Nombre"
                value={nombre}
                disabled={isPending}
                error={!!formErrors.nombre}
                helperText={formErrors.nombre}
                onChange={(e) => setNombre(e.target.value)}
              />
            </Grid>

            {/* Descripción */}
            <Grid item xs={12}>
              <TextField
                fullWidth
                label="Descripción"
                multiline
                rows={3}
                value={descripcion}
                disabled={isPending}
                onChange={(e) => setDescripcion(e.target.value)}
              />
            </Grid>

            {/* Categoría */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth error={!!formErrors.categoriaId}>
                <InputLabel id="dialog-categoria-label">Categoría</InputLabel>
                <Select
                  labelId="dialog-categoria-label"
                  value={categoriaId}
                  label="Categoría"
                  disabled={isPending || catLoading}
                  onChange={(e) => setCategoriaId(e.target.value)}
                >
                  <MenuItem value=""><em>Seleccione...</em></MenuItem>
                  {categorias.map((cat) => (
                    <MenuItem key={cat.id} value={cat.id}>
                      {cat.nombre}
                    </MenuItem>
                  ))}
                </Select>
                {formErrors.categoriaId && (
                  <FormHelperText>{formErrors.categoriaId}</FormHelperText>
                )}
              </FormControl>
            </Grid>

            {/* Proveedor */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth error={!!formErrors.proveedorId}>
                <InputLabel id="dialog-proveedor-label">Proveedor</InputLabel>
                <Select
                  labelId="dialog-proveedor-label"
                  value={proveedorId}
                  label="Proveedor"
                  disabled={isPending || provLoading}
                  onChange={(e) => setProveedorId(e.target.value)}
                >
                  <MenuItem value=""><em>Seleccione...</em></MenuItem>
                  {proveedores.map((prov) => (
                    <MenuItem key={prov.id} value={prov.id}>
                      {prov.nombre}
                    </MenuItem>
                  ))}
                </Select>
                {formErrors.proveedorId && (
                  <FormHelperText>{formErrors.proveedorId}</FormHelperText>
                )}
              </FormControl>
            </Grid>

            {/* Marca */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth error={!!formErrors.marcaId}>
                <InputLabel id="dialog-marca-label">Marca</InputLabel>
                <Select
                  labelId="dialog-marca-label"
                  value={marcaId}
                  label="Marca"
                  disabled={isPending || marLoading}
                  onChange={(e) => setMarcaId(e.target.value)}
                >
                  <MenuItem value=""><em>Seleccione...</em></MenuItem>
                  {marcas.map((m) => (
                    <MenuItem key={m.id} value={m.id}>
                      {m.nombre}
                    </MenuItem>
                  ))}
                </Select>
                {formErrors.marcaId && (
                  <FormHelperText>{formErrors.marcaId}</FormHelperText>
                )}
              </FormControl>
            </Grid>

            {/* Unidad de Medida */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth error={!!formErrors.unidadMedidaId}>
                <InputLabel id="dialog-unidad-label">Unidad de medida</InputLabel>
                <Select
                  labelId="dialog-unidad-label"
                  value={unidadMedidaId}
                  label="Unidad de medida"
                  disabled={isPending || uniLoading}
                  onChange={(e) => setUnidadMedidaId(e.target.value)}
                >
                  <MenuItem value=""><em>Seleccione...</em></MenuItem>
                  {unidades.map((u) => (
                    <MenuItem key={u.id} value={u.id}>
                      {u.nombre} ({u.abreviatura})
                    </MenuItem>
                  ))}
                </Select>
                {formErrors.unidadMedidaId && (
                  <FormHelperText>{formErrors.unidadMedidaId}</FormHelperText>
                )}
              </FormControl>
            </Grid>

            {/* Precio Compra */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="Precio de compra"
                type="number"
                slotProps={{ htmlInput: { min: 0, step: "0.01" } }}
                value={precioCompra}
                disabled={isPending}
                error={!!formErrors.precioCompra}
                helperText={formErrors.precioCompra}
                onChange={(e) => setPrecioCompra(e.target.value)}
              />
            </Grid>

            {/* Precio Venta */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="Precio de venta"
                type="number"
                slotProps={{ htmlInput: { min: 0, step: "0.01" } }}
                value={precioVenta}
                disabled={isPending}
                error={!!formErrors.precioVenta}
                helperText={formErrors.precioVenta}
                onChange={(e) => setPrecioVenta(e.target.value)}
              />
            </Grid>

            {/* Stock Mínimo */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="Stock mínimo"
                type="number"
                slotProps={{ htmlInput: { min: 0 } }}
                value={stockMinimo}
                disabled={isPending}
                error={!!formErrors.stockMinimo}
                helperText={formErrors.stockMinimo}
                onChange={(e) => setStockMinimo(e.target.value)}
              />
            </Grid>

            {/* Stock Máximo */}
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="Stock máximo"
                type="number"
                slotProps={{ htmlInput: { min: 0 } }}
                value={stockMaximo}
                disabled={isPending}
                error={!!formErrors.stockMaximo}
                helperText={formErrors.stockMaximo}
                onChange={(e) => setStockMaximo(e.target.value)}
              />
            </Grid>
          </Grid>
        </DialogContent>
        <DialogActions sx={{ p: 2 }}>
          <Button onClick={handleClose} disabled={isPending} color="inherit">
            Cancelar
          </Button>
          <Button
            type="submit"
            disabled={isPending}
            variant="contained"
            color="primary"
            startIcon={isPending ? <CircularProgress size={20} color="inherit" /> : null}
          >
            {isPending ? "Guardando..." : "Guardar"}
          </Button>
        </DialogActions>
      </form>
    </Dialog>
  );
}
