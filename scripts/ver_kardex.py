from app.database.session import SessionLocal

from app.modules.inventario.services.inventario_service import (
    InventarioService,
)


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        movimientos = service.obtener_kardex(1)

        print("=" * 90)
        print("KARDEX DEL PRODUCTO")
        print("=" * 90)

        for movimiento in movimientos:

            print(
                f"{movimiento.fecha:%Y-%m-%d %H:%M} | "
                f"{movimiento.tipo.value:<8} | "
                f"{movimiento.cantidad:>4} | "
                f"{movimiento.stock_anterior:>5} -> "
                f"{movimiento.stock_nuevo:>5} | "
                f"{movimiento.motivo}"
            )

    finally:

        session.close()


if __name__ == "__main__":
    main()