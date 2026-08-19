import {
    useMutation,
    useQueryClient,
} from "@tanstack/react-query";

import {
    actualizarProducto,
    type ProductoUpdateInput,
} from "../services/productos.service";

interface ActualizarProductoVariables {
    productoId: number;
    input: ProductoUpdateInput;
}

export function useActualizarProducto() {
    const queryClient =
        useQueryClient();

    return useMutation({
        mutationFn: ({
            productoId,
            input,
        }: ActualizarProductoVariables) =>
            actualizarProducto(
                productoId,
                input,
            ),

        onSuccess: () => {
            queryClient.invalidateQueries({
                queryKey: ["productos"],
            });
        },
    });
}