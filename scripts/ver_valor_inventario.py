from app.database.session import SessionLocal

from app.modules.inventario.services.inventario_service import (
    InventarioService,
)


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        items = service.obtener_valor_inventario()

        total = service.obtener_valor_total_inventario()

        print("=" * 95)
        print("VALOR DEL INVENTARIO")
        print("=" * 95)

        for item in items:

            print(
                f"{item.codigo:<12}"
                f"{item.nombre:<30}"
                f"Stock:{item.stock_actual:<6}"
                f"Costo:{item.costo_unitario:<12}"
                f"Valor:{item.valor_total}"
            )

        print()

        print("=" * 95)

        print(f"TOTAL INVENTARIO: {total}")

    finally:

        session.close()


if __name__ == "__main__":
    main()