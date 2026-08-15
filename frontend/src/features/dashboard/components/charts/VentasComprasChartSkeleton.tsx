import {
    Card,
    CardContent,
    Skeleton,
} from "@mui/material";

function VentasComprasChartSkeleton() {
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
                <Skeleton
                    variant="text"
                    width="25%"
                    height={32}
                />

                <Skeleton
                    variant="text"
                    width="45%"
                />

                <Skeleton
                    variant="rectangular"
                    height={350}
                    sx={{ mt: 2 }}
                />
            </CardContent>
        </Card>
    );
}

export default VentasComprasChartSkeleton;