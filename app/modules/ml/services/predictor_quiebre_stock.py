
class PredictorQuiebreStock:

    def __init__(self):
        pass

    def predecir(self, stock_actual: int, demanda_diaria: float) -> float:
        if demanda_diaria <= 0:
            return float("inf")

        return stock_actual / demanda_diaria

    def clasificar_riesgo(self, dias_stock: float) -> str:
        if dias_stock == float("inf"):
            return "SIN CONSUMO"
        if dias_stock <= 7:
            return "CRITICO"
        if dias_stock <= 15:
            return "ALTO"

        return "BAJO"