from app.database.session import SessionLocal

from app.modules.inventario.services.inventario_service import (
    InventarioService,
)


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        productos = service.obtener_sin_stock()

        print("=" * 80)
        print("PRODUCTOS SIN STOCK")
        print("=" * 80)

        if not productos:
            print("No existen productos sin stock.")
            return

        for p in productos:

            print(
                f"{p.codigo:<12}"
                f"{p.nombre:<35}"
                f"Stock: {p.stock_actual}"
            )

    finally:

        session.close()


if __name__ == "__main__":
    main()