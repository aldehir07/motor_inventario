from app.database.session import SessionLocal

from app.modules.ml.services.ml_service import (
    MLService,
)


def main():

    session = SessionLocal()

    try:

        service = MLService(session)

        demanda = service.predecir_demanda(
            anio=2026,
            mes=8,
            dia=15,
        )

        print("=" * 60)
        print("PREDICCIÓN DE DEMANDA")
        print("=" * 60)
        print(f"Demanda estimada: {demanda:.2f}")

    finally:

        session.close()


if __name__ == "__main__":
    main()