from app.database.session import SessionLocal

from app.modules.ml.datasets.dataset_builder import DatasetBuilder
from app.modules.ml.features.feature_engineering import (
    FeatureEngineering,
)
from app.modules.ml.training.demanda_trainer import (
    DemandaTrainer,
)


def main():

    session = SessionLocal()

    try:

        builder = DatasetBuilder(session)

        df = builder.construir_dataset_ventas()

        engineer = FeatureEngineering()

        df = engineer.preparar_dataset(df)

        trainer = DemandaTrainer()

        trainer.entrenar_y_guardar(df)

        print("=" * 60)
        print("MODELO ENTRENADO")
        print("=" * 60)
        print("Archivo generado:")
        print("app/modules/ml/models/demanda_model.pkl")

    finally:

        session.close()


if __name__ == "__main__":
    main()