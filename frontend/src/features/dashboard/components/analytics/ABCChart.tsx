import {
    Card,
    CardContent,
    Typography,
    Box,
    Alert,
} from "@mui/material";

import {
    BarChart,
    Bar,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import type { ABCProducto } from "../../../analytics/types/analytics";

interface ABCChartProps {
    data: ABCProducto[];
}

interface ABCResumen {
    clasificacion: string;
    productos: number;
    valor: number;
}

function ABCChart({
    data,
}: ABCChartProps) {
    const resumenMap = new Map<
        string,
        ABCResumen
    >();

    data.forEach((producto) => {
        const clasificacion =
            producto.clasificacion;

        const existente =
            resumenMap.get(clasificacion);

        if (existente) {
            existente.productos += 1;
            existente.valor += Number(producto.valor);
        } else {
            resumenMap.set(clasificacion, {
                clasificacion,
                productos: 1,
                valor: Number(producto.valor),
            });
        }
    });

    const resumen = Array.from(
        resumenMap.values()
    ).sort((a, b) =>
        a.clasificacion.localeCompare(
            b.clasificacion
        )
    );
    if (resumen.length === 0) {
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
                    >
                        Clasificación ABC
                    </Typography>

                    <Alert
                        severity="info"
                        sx={{ mt: 3 }}
                    >
                        No hay información suficiente para
                        mostrar la clasificación ABC.
                    </Alert>
                </CardContent>
            </Card>
        );
    }

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
                    sx={{ fontWeight: "bold" }}
                >
                    Clasificación ABC
                </Typography>

                <Typography
                    variant="body1"
                    color="text.primary"
                    sx={{ mb: 3 }}
                >
                    Distribución del valor del inventario
                    por clasificación.
                </Typography>

                <Box
                    sx={{
                        width: "100%",
                        height: 350,
                    }}
                >
                    <ResponsiveContainer
                        width="100%"
                        height="100%"
                    >
                        <BarChart data={resumen}>
                            <CartesianGrid
                                strokeDasharray="3 3"
                            />

                            <XAxis
                                dataKey="clasificacion"
                            />

                            <YAxis />

                            <Tooltip
                                formatter={(value, name) => {
                                    if (name === "valor") {
                                        return [
                                            new Intl.NumberFormat(
                                                "es-PA",
                                                {
                                                    style: "currency",
                                                    currency: "USD",
                                                }
                                            ).format(Number(value)),
                                            "Valor",
                                        ];
                                    }

                                    return [
                                        value,
                                        "Productos",
                                    ];
                                }}
                            />

                            <Bar
                                dataKey="valor"
                                name="Valor"
                                fill="currentColor"
                            />
                        </BarChart>
                    </ResponsiveContainer>
                </Box>
            </CardContent>
        </Card>
    );
}

export default ABCChart;