from app.database.session import SessionLocal

from app.modules.analytics.services.analytics_service import (
    AnalyticsService,
)


def main():

    session = SessionLocal()

    try:

        service = AnalyticsService(session)

        dashboard = service.obtener_dashboard()

        print("=" * 70)
        print("DASHBOARD EJECUTIVO")
        print("=" * 70)

        print(f"Productos registrados : {dashboard.productos}")

        print(f"Productos activos     : {dashboard.productos_activos}")

        print(f"Stock bajo            : {dashboard.stock_bajo}")

        print(f"Sin stock             : {dashboard.sin_stock}")

        print(f"Compras               : {dashboard.compras}")

        print(f"Ventas                : {dashboard.ventas}")

        print(f"Valor inventario      : {dashboard.valor_inventario}")

    finally:

        session.close()


if __name__ == "__main__":
    main()