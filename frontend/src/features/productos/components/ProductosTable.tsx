import {
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
} from "@mui/material";

import type { Producto } from "../types/producto";

interface ProductosTableProps {
    productos: Producto[];
}

function ProductosTable({
    productos,
}: ProductosTableProps) {
    return (
        <TableContainer
            component={Paper}
            elevation={0}
            sx={{
                border: 1,
                borderColor: "divider",
            }}
        >
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>
                            <strong>Codigo</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Nombre</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Stock minimo</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Stock maximo</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Precio compra</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Precio venta</strong>
                        </TableCell>

                        <TableCell>
                            <strong>Estado</strong>
                        </TableCell>
                    </TableRow>
                </TableHead>

                <TableBody>
                    {productos.map((producto) => (
                        <TableRow
                            key={producto.id}
                            hover
                        >
                            <TableCell>
                                <Typography
                                    variant="body2"
                                    sx={{ fontWeight: "600" }}
                                >
                                    {producto.codigo}
                                </Typography>
                            </TableCell>

                            <TableCell>
                                {producto.nombre}
                            </TableCell>

                            <TableCell>
                                {producto.stock_minimo}
                            </TableCell>

                            <TableCell>
                                {producto.stock_maximo}
                            </TableCell>

                            <TableCell>
                                {producto.precio_compra_actual}
                            </TableCell>

                            <TableCell>
                                {producto.precio_venta_actual}
                            </TableCell>

                            <TableCell>
                                {producto.activo
                                    ? "Activo"
                                    : "Inactivo"
                                }
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>

        </TableContainer>
    );
}

export default ProductosTable;