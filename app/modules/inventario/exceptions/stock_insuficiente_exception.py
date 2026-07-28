class StockInsuficienteException(Exception):

    def __init__(
        self,
        disponible: int,
        solicitado: int,
    ):
        super().__init__(
            f"Stock insuficiente. Disponible: {disponible}, solicitado: {solicitado}."
        )