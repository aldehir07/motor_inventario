from app.database.session import SessionLocal

from app.modules.inventario.services.inventario_service import (
    InventarioService,
)


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        productos = service.obtener_stock_bajo()

        print("=" * 80)
        print("PRODUCTOS CON STOCK BAJO")
        print("=" * 80)

        if not productos:
            print("No hay productos con stock bajo.")
            return

        for p in productos:

            print(
                f"{p.codigo:<12}"
                f"{p.nombre:<30}"
                f"Stock:{p.stock_actual:<5}"
                f"Mínimo:{p.stock_minimo}"
            )

    finally:

        session.close()


if __name__ == "__main__":
    main()