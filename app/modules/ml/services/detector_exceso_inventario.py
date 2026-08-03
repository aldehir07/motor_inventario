class DetectorExcesoInventario:

    def __init__(self):
        pass

    def detectar(
        self,
        stock_actual: int,
        stock_maximo: int,
        demanda_diaria: float,
    ) -> tuple[bool, str]:
        """
        Detecta si un producto posee exceso de inventario.
        """

        if stock_actual <= stock_maximo:
            return False, "Inventario normal."

        exceso = stock_actual - stock_maximo

        dias = (
            float("inf")
            if demanda_diaria <= 0
            else stock_actual / demanda_diaria
        )

        motivo = (
            f"Exceso de {exceso} unidades "
            f"({dias:.1f} días de inventario)."
        )

        return True, motivo