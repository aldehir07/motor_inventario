from app.modules.inventario.exceptions.stock_insuficiente_exception import (
    StockInsuficienteException,
)


class Stock:

    def __init__(self, cantidad: int):
        self._cantidad = cantidad

    @property
    def actual(self) -> int:
        return self._cantidad

    def entrada(self, cantidad: int):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self._cantidad += cantidad

    def salida(self, cantidad: int):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self._cantidad:
            raise StockInsuficienteException(
                self._cantidad,
                cantidad,
            )

        self._cantidad -= cantidad