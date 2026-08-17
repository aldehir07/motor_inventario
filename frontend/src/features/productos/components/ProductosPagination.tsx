import {
    Box,
    Pagination,
    Typography,
} from "@mui/material";

interface ProductosPaginationProps {
    pagina: number;
    paginas: number;
    total: number;
    limite: number;
    onChange: (pagina: number) => void;
}

function ProductosPagination({
    pagina,
    paginas,
    total,
    limite,
    onChange,
}: ProductosPaginationProps) {
    if (paginas <= 1) {
        return null;
    }

    const desde =
        (pagina - 1) * limite + 1;

    const hasta = Math.min(
        pagina * limite,
        total,
    );

    return (
        <Box
            sx={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                mt: 3,
                gap: 2,
                flexWrap: "wrap",
            }}
        >
            <Typography
                variant="body2"
                color="text.secondary"
            >
                Mostrando {desde}-{hasta} de {total} productos
            </Typography>

            <Pagination
                count={paginas}
                page={pagina}
                onChange={(_, nuevaPagina) =>
                    onChange(nuevaPagina)
                }
                color="primary"
                shape="rounded"
            />
        </Box>
    );
}

export default ProductosPagination;