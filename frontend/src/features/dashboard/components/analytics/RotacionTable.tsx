import {
    Card,
    CardContent,
    Chip,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
} from "@mui/material";

import type { RotacionInventario } from "../../../analytics/types/analytics";

interface RotacionTableProps {
    data: RotacionInventario[];
}

function obtenerColorRotacion(
    rotacion: number
): "success" | "warning" | "error" {
    if (rotacion >= 10) {
        return "success";
    }

    if (rotacion >= 5) {
        return "warning";
    }

    return "error";
}

function RotacionTable({
    data,
}: RotacionTableProps) {
    return (
        <Card
            elevation={0}
            sx={{
                height: "100%",
                border: 1,
                borderColor: "divider",
                borderRadius: 2,
            }}
        >
            <CardContent>
                <Typography
                    variant="h6"
                    sx={{ fontWeight: "600" }}
                    gutterBottom
                >
                    Rotación de inventario
                </Typography>

                <Typography
                    variant="body2"
                    color="text.secondary"
                    sx={{ mb: 3 }}
                >
                    Productos con mayor y menor movimiento.
                </Typography>

                <TableContainer>
                    <Table size="small">
                        <TableHead>
                            <TableRow>
                                <TableCell>Producto</TableCell>
                                <TableCell>Stock</TableCell>
                                <TableCell>Vendidos</TableCell>
                                <TableCell>Rotación</TableCell>
                            </TableRow>
                        </TableHead>

                        <TableBody>
                            {data.map((producto) => (
                                <TableRow
                                    key={producto.producto_id}
                                    hover
                                >
                                    <TableCell>
                                        <Typography
                                            variant="body2"
                                            sx={{ fontWeight: "500" }}
                                        >
                                            {producto.nombre}
                                        </Typography>

                                        <Typography
                                            variant="caption"
                                            color="text.secondary"
                                        >
                                            {producto.codigo}
                                        </Typography>
                                    </TableCell>

                                    <TableCell>
                                        {producto.stock_actual}
                                    </TableCell>

                                    <TableCell>
                                        {producto.vendidos}
                                    </TableCell>

                                    <TableCell>
                                        <Chip
                                            size="small"
                                            label={Number(producto.rotacion).toFixed(2)}
                                            color={obtenerColorRotacion(
                                                Number(producto.rotacion)
                                            )}
                                        />
                                    </TableCell>
                                </TableRow>
                            ))}

                            {data.length === 0 && (
                                <TableRow>
                                    <TableCell
                                        colSpan={4}
                                        align="center"
                                    >
                                        No hay datos de rotación disponibles.
                                    </TableCell>
                                </TableRow>
                            )}
                        </TableBody>
                    </Table>
                </TableContainer>
            </CardContent>
        </Card>
    );
}

export default RotacionTable;