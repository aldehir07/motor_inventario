from app.modules.configuracion.configuracion_ml import ConfiguracionML

class DetectorExcesoInventario:

    def __init__(self):
        self.config = ConfiguracionML()

    def detectar(
        self,
        stock_actual: int,
        stock_maximo: int,
        demanda_diaria: float,
    ) -> tuple[bool, str]:
        """
        Detecta si un producto posee exceso de inventario.
        """

        if demanda_diaria <= 0:
            return (
                stock_actual > stock_maximo,
                "No existe demanda registrada."
            )

        dias = stock_actual / demanda_diaria

        if (
            stock_actual <= stock_maximo
            and dias <= self.config.dias_exceso_inventario
        ):
            return False, "Inventario normal."

        exceso = max(
            0,
            stock_actual - stock_maximo,
        )

        motivo = (
            f"Exceso de {exceso} unidades "
            f"({dias:.1f} días de inventario)."
        )

        return True, motivo