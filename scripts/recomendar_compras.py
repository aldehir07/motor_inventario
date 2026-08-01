from app.database.session import SessionLocal
from app.modules.ml.services.ml_service import MLService


def main():

    session = SessionLocal()

    try:

        service = MLService(session)

        recomendaciones = service.recomendar_comprar()

        print("=" * 80)
        print("RECOMENDACIONES DE COMPRA")
        print("=" * 80)

        for item in recomendaciones:

            print()

            print(f"Producto : {item.codigo} - {item.nombre}")
            print(f"Stock    : {item.stock_actual}")
            print(f"Demanda  : {item.demanda_estimada:.2f}")
            print(f"Comprar  : {item.cantidad_recomendada}")
            print(f"Prioridad: {item.prioridad}")
            print(f"Motivo   : {item.motivo}")

    finally:

        session.close()


if __name__ == "__main__":
    main()