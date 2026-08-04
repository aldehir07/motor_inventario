from app.modules.configuracion.configuracion_ml import (
    ConfiguracionML,
)

class CalculadoraCobertura:

    def __init__(self,):

        self.config = ConfiguracionML()

    def calcular_stock_objetivo(
        self,
        demanda_diaria: float,
    ) -> int:
        """
        Calcula el inventario objetivo según
        la demanda diaria estimada.
        """

        return round(
            demanda_diaria * self.config.dias_cobertura
        )

    def calcular_compra(
        self,
        stock_actual: int,
        demanda_diaria: float,
    ) -> int:
        """
        Calcula la cantidad sugerida para compra.
        """

        objetivo = self.calcular_stock_objetivo(
            demanda_diaria
        )

        return max(
            0,
            objetivo - stock_actual,
        )

    def obtener_cobertura(self) -> int:
        """
        Devuelve la cantidad de días de cobertura
        configurados para el cálculo.
        """

        return self.config.dias_cobertura