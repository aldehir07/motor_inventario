import {
    Alert,
    Box,
    Card,
    CardContent,
    Typography,
} from "@mui/material";

import {
    CartesianGrid,
    Legend,
    Line,
    LineChart,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import type {
    VentaPorMes,
    CompraPorMes,
} from "../../../analytics/types/analytics";

interface VentasComprasChartProps {
    ventas: VentaPorMes[];
    compras: CompraPorMes[];
}

interface ChartData {
    periodo: string;
    ventas: number;
    compras: number;
}

function VentasComprasChart({
    ventas,
    compras,
}: VentasComprasChartProps) {

    const dataMap = new Map<string, ChartData>();

    ventas.forEach((item) => {
        const periodo = `${item.anio}-${String(item.mes).padStart(2, "0")}`;

        dataMap.set(periodo, {
            periodo,
            ventas: item.total,
            compras: 0,
        });
    });

    compras.forEach((item) => {
        const periodo = `${item.anio}-${String(item.mes).padStart(2, "0")}`;

        const existente = dataMap.get(periodo);

        if (existente) {
            existente.compras = item.total;
        } else {
            dataMap.set(periodo, {
                periodo,
                ventas: 0,
                compras: item.total,
            });
        }
    });

    const data = Array.from(dataMap.values()).sort(
        (a, b) =>
            a.periodo.localeCompare(b.periodo)
    );
    if (data.length === 0) {
        return (
            <Card
                elevation={0}
                sx={{
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
                        Ventas y compras
                    </Typography>

                    <Alert
                        severity="info"
                        sx={{ mt: 3 }}
                    >
                        No hay información histórica de
                        ventas y compras disponible.
                    </Alert>
                </CardContent>
            </Card>
        );
    }

    return (
        <Card
            elevation={0}
            sx={{
                border: 1,
                borderColor: "divider",
                borderRadius: 2,
            }}
        >
            <CardContent>
                <Box sx={{ mb: 3 }}>
                    <Typography
                        variant="h6"
                        sx={{ fontWeight: "600" }}
                    >
                        Ventas y compras
                    </Typography>

                    <Typography
                        variant="body2"
                        color="text.secondary"
                    >
                        Comparación mensual de compras y ventas.
                    </Typography>
                </Box>

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
                        <LineChart data={data}>
                            <CartesianGrid
                                strokeDasharray="3 3"
                            />

                            <XAxis
                                dataKey="periodo"
                            />

                            <YAxis />

                            <Tooltip />

                            <Legend />

                            <Line
                                type="monotone"
                                dataKey="ventas"
                                name="Ventas"
                                stroke="#1976d2"
                                strokeWidth={2}
                                dot={false}
                            />

                            <Line
                                type="monotone"
                                dataKey="compras"
                                name="Compras"
                                stroke="#2e7d32"
                                strokeWidth={2}
                                dot={false}
                            />
                        </LineChart>
                    </ResponsiveContainer>
                </Box>
            </CardContent>
        </Card>
    );
}

export default VentasComprasChart;