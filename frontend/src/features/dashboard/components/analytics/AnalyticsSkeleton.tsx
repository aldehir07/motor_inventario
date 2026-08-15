import {
    Card,
    CardContent,
    Skeleton,
} from "@mui/material";

function AnalyticsSkeleton() {
    return (
        <>
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
                        width="35%"
                        height={32}
                    />

                    <Skeleton
                        variant="text"
                        width="55%"
                    />

                    <Skeleton
                        variant="rectangular"
                        height={350}
                        sx={{ mt: 2 }}
                    />
                </CardContent>
            </Card>

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
                        width="35%"
                        height={32}
                    />

                    <Skeleton
                        variant="text"
                        width="55%"
                    />

                    {Array.from({ length: 5 }).map(
                        (_, index) => (
                            <Skeleton
                                key={index}
                                variant="text"
                                height={45}
                            />
                        )
                    )}
                </CardContent>
            </Card>
        </>
    );
}

export default AnalyticsSkeleton;