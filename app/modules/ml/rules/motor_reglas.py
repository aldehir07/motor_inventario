class MotorReglas:

    def __init__(self):
        pass

    def evaluar(
        self,
        stock_actual: int,
        stock_minimo: int,
        demanda: float,
        riesgo_quiebre: str,
        exceso_inventario: bool,
        rotacion: str,
    ) -> tuple[str, str, int]:
        """
        Devuelve:

        prioridad,
        motivo,
        indice
        """

        indice = self._calcular_indice(
            stock_actual=stock_actual,
            stock_minimo=stock_minimo,
            demanda=demanda,
            riesgo_quiebre=riesgo_quiebre,
        )

        if exceso_inventario:

            return (
                "BAJA",
                "Existe exceso de inventario.",
                indice,
            )

        if riesgo_quiebre == "CRITICO":

            return (
                "CRITICA",
                "Riesgo crítico de quiebre.",
                indice,
            )

        if riesgo_quiebre == "ALTO":

            return (
                "ALTA",
                "Riesgo alto de quiebre.",
                indice,
            )

        if rotacion == "MUY BAJA":

            return (
                "BAJA",
                "Producto de muy baja rotación.",
                indice,
            )

        return (
            "MEDIA",
            "Condición normal.",
            indice,
        )

    def _calcular_indice(
        self,
        stock_actual: int,
        stock_minimo: int,
        demanda: float,
        riesgo_quiebre: str,
    ) -> int:

        indice = 0

        if stock_actual <= 0:
            indice += 100

        elif stock_actual < stock_minimo:
            indice += 50

        if demanda > stock_actual:
            indice += 25

        if riesgo_quiebre == "CRITICO":
            indice += 50

        elif riesgo_quiebre == "ALTO":
            indice += 30

        elif riesgo_quiebre == "MEDIO":
            indice += 15

        return min(indice, 100)