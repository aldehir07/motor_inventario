from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from app.modules.ml.features.feature_engineering import (
    FeatureEngineering,
)


class DemandaTrainer:

    def __init__(self):

        self.feature_engineering = FeatureEngineering()

        self.model = RandomForestRegressor(
            n_estimators=200,
            random_state=42,
        )

    def entrenar(
        self,
        df: pd.DataFrame,
    ):

        df = self.feature_engineering.preparar_dataset(
            df,
        )

        X, y = self.feature_engineering.obtener_features_target(
            df,
        )

        self.model.fit(
            X,
            y,
        )

    def guardar_modelo(
        self,
    ):

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

        self.entrenar(
            df,
        )

        self.guardar_modelo()