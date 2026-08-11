from pathlib import Path
from datetime import date

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
        producto_id: int,
        categoria_id: int,
        marca_id: int,
        fecha: date,
    ):

        X = pd.DataFrame(
            [
                {
                    "producto_id": producto_id,
                    "categoria_id": categoria_id,
                    "marca_id": marca_id,
                    "anio": fecha.year,
                    "mes": fecha.month,
                    "dia": fecha.day,
                    "dia_semana": fecha.weekday(),
                    "trimestre": (fecha.month - 1) // 3 + 1,
                }
            ]
        )

        resultado = self.model.predict(X)

        return float(resultado[0])