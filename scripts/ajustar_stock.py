from app.database.session import SessionLocal

from app.modules.inventario.schemas.movimiento_schema import AjustarStock
from app.modules.inventario.services.inventario_service import InventarioService


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        inventario = service.ajustar_stock(
            AjustarStock(
                producto_id=1,
                nuevo_stock=100,
                motivo="Conteo físico",
                referencia="INV-2026-001",
            )
        )

        print("=" * 40)
        print("Stock ajustado")
        print("=" * 40)
        print(f"Producto: {inventario.producto_id}")
        print(f"Stock: {inventario.stock_actual}")

    finally:
        session.close()


if __name__ == "__main__":
    main()