from app.shared.exceptions.not_found_exception import (
    NotFoundException,
)


class ProductoNoEncontradoException(NotFoundException):

    def __init__(self, producto_id: int):
        super().__init__(
            f"No existe un producto con ID {producto_id}."
        )