from app.database.session import SessionLocal

from app.modules.analytics.services.analytics_service import (
    AnalyticsService,
)


def main():

    session = SessionLocal()

    try:

        service = AnalyticsService(session)

        datos = service.obtener_abc()

        print("=" * 90)
        print("ABC ANALYSIS")
        print("=" * 90)

        for item in datos:

            print(

                f"{item.codigo:<12}"

                f"{item.nombre:<35}"

                f"{item.valor:<15}"

                f"Clase {item.clasificacion}"

            )

    finally:

        session.close()


if __name__ == "__main__":
    main()