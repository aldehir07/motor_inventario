from app.shared.exceptions.conflict_exception import (
    ConflictException,
)


class StockInsuficienteException(ConflictException):

    def __init__(
        self,
        disponible: int,
        solicitado: int,
    ):
        super().__init__(
            f"Stock insuficiente. Disponible: {disponible}, "
            f"solicitado: {solicitado}."
        )