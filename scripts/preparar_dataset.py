from app.database.session import SessionLocal

from app.modules.ml.datasets.dataset_builder import DatasetBuilder
from app.modules.ml.features.feature_engineering import (
    FeatureEngineering,
)


def main():

    session = SessionLocal()

    try:

        builder = DatasetBuilder(session)

        df = builder.construir_dataset_ventas()

        engineer = FeatureEngineering()

        df = engineer.preparar_dataset(df)

        print("=" * 80)
        print("DATASET PREPARADO")
        print("=" * 80)

        print(df.head())

        print()

        print(df.info())

    finally:

        session.close()


if __name__ == "__main__":
    main()