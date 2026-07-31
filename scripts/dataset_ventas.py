from app.database.session import SessionLocal

from app.modules.ml.datasets.dataset_builder import DatasetBuilder


def main():

    session = SessionLocal()

    try:

        builder = DatasetBuilder(session)

        df = builder.construir_dataset_ventas()

        print("=" * 80)
        print("DATASET DE VENTAS")
        print("=" * 80)

        print(df)

        print()

        print(df.info())

    finally:

        session.close()


if __name__ == "__main__":
    main()