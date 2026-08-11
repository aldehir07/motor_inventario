class CantidadInvalidaException(Exception):

    def __init__(self, cantidad: int):
        super().__init__(
            f"La cantidad '{cantidad}' debe ser mayor que cero."
        )