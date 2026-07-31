from pathlib import Path

import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression

class DemandaTrainer:

    def __init__(self):

        self.model = LinearRegression()

    def entrenar(
        self,
        df: pd.DataFrame,
    ):

        X = df[
            [
                "anio",
                "mes",
                "dia",
            ]
        ]

        y = df["cantidad"]

        self.model.fit(
            X,
            y,
        )

    def guardar_modelo(self):
        carpeta = Path(
            "app/modules/ml/models"
        )

        carpeta.mkdir(
            parents=True,
            exist_ok=True,
        )

        ruta = carpeta / "demanda_model.pkl"

        joblib.dump(
            self.model,
            ruta,
        )

    def entrenar_y_guardar(
        self,
        df: pd.DataFrame,
    ):

        self.entrenar(df)

        self.guardar_modelo()