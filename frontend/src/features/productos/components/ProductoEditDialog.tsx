import {
    Alert,
    Box,
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    FormControlLabel,
    Switch,
    TextField,
} from "@mui/material";

import { useEffect, useState } from "react";

import type { Producto } from "../types/producto";

import {
    useActualizarProducto,
} from "../hooks/useActualizarProducto";

interface ProductoEditDialogProps {
    open: boolean;
    producto: Producto | null;
    onClose: () => void;
}

interface FormErrors {
    nombre?: string;
    precio_compra_actual?: string;
    precio_venta_actual?: string;
    stock_minimo?: string;
    stock_maximo?: string;
}

function ProductoEditDialog({
    open,
    producto,
    onClose,
}: ProductoEditDialogProps) {
    const actualizarProducto =
        useActualizarProducto();

    const [nombre, setNombre] =
        useState("");

    const [descripcion, setDescripcion] =
        useState("");

    const [precioCompra, setPrecioCompra] =
        useState("");

    const [precioVenta, setPrecioVenta] =
        useState("");

    const [stockMinimo, setStockMinimo] =
        useState("");

    const [stockMaximo, setStockMaximo] =
        useState("");

    const [activo, setActivo] =
        useState(true);

    const [errors, setErrors] =
        useState<FormErrors>({});

    useEffect(() => {
        if (!producto) {
            return;
        }

        setNombre(producto.nombre);

        setDescripcion(
            producto.descripcion ?? "",
        );

        setPrecioCompra(
            String(producto.precio_compra_actual),
        );

        setPrecioVenta(
            String(producto.precio_venta_actual),
        );

        setStockMinimo(
            String(producto.stock_minimo),
        );

        setStockMaximo(
            String(producto.stock_maximo),
        );

        setActivo(producto.activo);

        setErrors({});
    }, [producto]);

    const validarFormulario = (): boolean => {
        const nuevosErrores: FormErrors = {};

        if (nombre.trim().length < 3) {
            nuevosErrores.nombre =
                "El nombre debe tener al menos 3 caracteres.";
        }

        const compra =
            Number(precioCompra);

        if (
            precioCompra === "" ||
            !Number.isFinite(compra) ||
            compra <= 0
        ) {
            nuevosErrores.precio_compra_actual =
                "El precio de compra debe ser mayor que 0.";
        }

        const venta =
            Number(precioVenta);

        if (
            precioVenta === "" ||
            !Number.isFinite(venta) ||
            venta <= 0
        ) {
            nuevosErrores.precio_venta_actual =
                "El precio de venta debe ser mayor que 0.";
        }

        const minimo =
            Number(stockMinimo);

        if (
            stockMinimo === "" ||
            !Number.isInteger(minimo) ||
            minimo < 0
        ) {
            nuevosErrores.stock_minimo =
                "El stock mínimo debe ser un entero mayor o igual a 0.";
        }

        const maximo =
            Number(stockMaximo);

        if (
            stockMaximo === "" ||
            !Number.isInteger(maximo) ||
            maximo < 0
        ) {
            nuevosErrores.stock_maximo =
                "El stock máximo debe ser un entero mayor o igual a 0.";
        }

        if (
            Number.isFinite(minimo) &&
            Number.isFinite(maximo) &&
            minimo > maximo
        ) {
            nuevosErrores.stock_maximo =
                "El stock máximo debe ser mayor o igual al stock mínimo.";
        }

        setErrors(nuevosErrores);

        return (
            Object.keys(nuevosErrores)
                .length === 0
        );
    };

    const handleSubmit = async () => {
        if (!producto) {
            return;
        }

        if (!validarFormulario()) {
            return;
        }

        await actualizarProducto.mutateAsync({
            productoId: producto.id,

            input: {
                nombre: nombre.trim(),

                descripcion:
                    descripcion.trim() || null,

                precio_compra_actual:
                    Number(precioCompra),

                precio_venta_actual:
                    Number(precioVenta),

                stock_minimo:
                    Number(stockMinimo),

                stock_maximo:
                    Number(stockMaximo),

                activo,
            },
        });

        onClose();
    };

    const handleClose = () => {
        if (actualizarProducto.isPending) {
            return;
        }

        onClose();
    };

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            fullWidth
            maxWidth="sm"
        >
            <DialogTitle>
                Editar producto
            </DialogTitle>

            <DialogContent>
                <Box
                    sx={{
                        display: "flex",
                        flexDirection: "column",
                        gap: 2,
                        mt: 1,
                    }}
                >
                    {actualizarProducto.isError && (
                        <Alert severity="error">
                            No fue posible actualizar
                            el producto. Intenta nuevamente.
                        </Alert>
                    )}

                    <TextField
                        label="Nombre"
                        value={nombre}
                        onChange={(event) =>
                            setNombre(event.target.value)
                        }
                        error={Boolean(errors.nombre)}
                        helperText={errors.nombre}
                        fullWidth
                        required
                    />

                    <TextField
                        label="Descripción"
                        value={descripcion}
                        onChange={(event) =>
                            setDescripcion(
                                event.target.value,
                            )
                        }
                        multiline
                        minRows={3}
                        fullWidth
                    />

                    <TextField
                        label="Precio de compra"
                        type="number"
                        value={precioCompra}
                        onChange={(event) =>
                            setPrecioCompra(
                                event.target.value,
                            )
                        }
                        error={Boolean(
                            errors.precio_compra_actual,
                        )}
                        helperText={
                            errors.precio_compra_actual
                        }
                        slotProps={{
                            htmlInput: {
                                min: 0,
                                step: "0.01",
                            },
                        }}
                        fullWidth
                        required
                    />

                    <TextField
                        label="Precio de venta"
                        type="number"
                        value={precioVenta}
                        onChange={(event) =>
                            setPrecioVenta(
                                event.target.value,
                            )
                        }
                        error={Boolean(
                            errors.precio_venta_actual,
                        )}
                        helperText={
                            errors.precio_venta_actual
                        }
                        slotProps={{
                            htmlInput: {
                                min: 0,
                                step: "0.01",
                            },
                        }}
                        fullWidth
                        required
                    />

                    <TextField
                        label="Stock mínimo"
                        type="number"
                        value={stockMinimo}
                        onChange={(event) =>
                            setStockMinimo(
                                event.target.value,
                            )
                        }
                        error={Boolean(
                            errors.stock_minimo,
                        )}
                        helperText={
                            errors.stock_minimo
                        }
                        slotProps={{
                            htmlInput: {
                                min: 0,
                                step: 1,
                            },
                        }}
                        fullWidth
                        required
                    />

                    <TextField
                        label="Stock máximo"
                        type="number"
                        value={stockMaximo}
                        onChange={(event) =>
                            setStockMaximo(
                                event.target.value,
                            )
                        }
                        error={Boolean(
                            errors.stock_maximo,
                        )}
                        helperText={
                            errors.stock_maximo
                        }
                        slotProps={{
                            htmlInput: {
                                min: 0,
                                step: 1,
                            },
                        }}
                        fullWidth
                        required
                    />

                    <FormControlLabel
                        control={
                            <Switch
                                checked={activo}
                                onChange={(event) =>
                                    setActivo(
                                        event.target.checked,
                                    )
                                }
                            />
                        }
                        label={
                            activo
                                ? "Producto activo"
                                : "Producto inactivo"
                        }
                    />
                </Box>
            </DialogContent>

            <DialogActions>
                <Button
                    onClick={handleClose}
                    disabled={
                        actualizarProducto.isPending
                    }
                >
                    Cancelar
                </Button>

                <Button
                    variant="contained"
                    onClick={handleSubmit}
                    disabled={
                        actualizarProducto.isPending
                    }
                >
                    {actualizarProducto.isPending
                        ? "Guardando..."
                        : "Guardar cambios"}
                </Button>
            </DialogActions>
        </Dialog>
    );
}

export default ProductoEditDialog;