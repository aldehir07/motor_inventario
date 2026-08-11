from app.database.session import SessionLocal

from app.modules.analytics.services.analytics_service import (
    AnalyticsService,
)


def main():

    session = SessionLocal()

    try:

        service = AnalyticsService(session)

        datos = service.obtener_ventas_por_mes()

        print("=" * 70)
        print("VENTAS POR MES")
        print("=" * 70)

        if not datos:

            print("No existen ventas confirmadas.")

            return

        for fila in datos:

            print(
                f"{fila.anio}-{fila.mes:02d}  ->  {fila.total}"
            )

    finally:

        session.close()


if __name__ == "__main__":
    main()