from app.database.session import SessionLocal

from app.modules.analytics.services.analytics_service import (
    AnalyticsService,
)


def main():

    session = SessionLocal()

    try:

        service = AnalyticsService(session)

        datos = service.obtener_rotacion_inventario()

        print("=" * 100)
        print("ROTACIÓN DE INVENTARIO")
        print("=" * 100)

        for item in datos:

            print(

                f"{item.codigo:<12}"

                f"{item.nombre:<35}"

                f"Stock:{item.stock_actual:<6}"

                f"Vendidos:{item.vendidos:<6}"

                f"Rotación:{item.rotacion}"

            )

    finally:

        session.close()


if __name__ == "__main__":
    main()