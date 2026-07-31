from pathlib import Path

import joblib
import pandas as pd

class DemandaPredictor:

    def __init__(self):

        ruta = Path(
            "app/modules/ml/models/demanda_model.pkl"
        )

        self.model = joblib.load(ruta)

    def _crear_dataframe(
        self,
        anio: int,
        mes: int,
        dia: int,
    ) -> pd.DataFrame:

        return pd.DataFrame(
            {
                "anio": [anio],
                "mes": [mes],
                "dia": [dia],
            }
        )

    def predecir(
        self,
        anio: int,
        mes: int,
        dia: int,
    ) -> float:

        X = self._crear_dataframe(
            anio,
            mes,
            dia,
        )

        resultado = self.model.predict(X)

        return float(resultado[0])