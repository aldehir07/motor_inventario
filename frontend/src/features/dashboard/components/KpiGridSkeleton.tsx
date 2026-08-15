import {
    Grid,
    Skeleton,
    Card,
    CardContent,
} from "@mui/material";

function KpiGridSkeleton() {
    return (
        <Grid container spacing={2}>
            {Array.from({ length: 7 }).map((_, index) => (
                <Grid
                    key={index}
                    size={{
                        xs: 12,
                        sm: 6,
                        md: index < 4 ? 3 : 4,
                    }}
                >
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
                            <Skeleton
                                variant="text"
                                width="40%"
                            />

                            <Skeleton
                                variant="text"
                                width="60%"
                                height={50}
                            />

                            <Skeleton
                                variant="text"
                                width="70%"
                            />
                        </CardContent>
                    </Card>
                </Grid>
            ))}
        </Grid>
    );
}

export default KpiGridSkeleton;