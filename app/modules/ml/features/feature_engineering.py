import pandas as pd


class FeatureEngineering:

    FEATURES = [
        "producto_id",
        "categoria_id",
        "marca_id",
        "anio",
        "mes",
        "dia",
        "dia_semana",
        "trimestre",
    ]

    TARGET = "cantidad"

    def transformar_fechas(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        df["fecha"] = pd.to_datetime(df["fecha"])

        df["anio"] = df["fecha"].dt.year

        df["mes"] = df["fecha"].dt.month

        df["dia"] = df["fecha"].dt.day

        df["dia_semana"] = df["fecha"].dt.dayofweek

        df["trimestre"] = df["fecha"].dt.quarter

        return df

    def agregar_mes_nombre(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        df["nombre_mes"] = df["fecha"].dt.month_name()

        return df

    def ordenar_dataset(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        return df.sort_values(
            by=[
                "producto_id",
                "fecha",
            ]
        )

    def preparar_dataset(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = self.transformar_fechas(df)

        df = self.agregar_mes_nombre(df)

        df = self.ordenar_dataset(df)

        return df

    def obtener_features_target(
        self,
        df: pd.DataFrame,
    ) -> tuple[pd.DataFrame, pd.Series]:

        X = df[self.FEATURES]

        y = df[self.TARGET]

        return X, y