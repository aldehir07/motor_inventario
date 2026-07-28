from app.database.session import SessionLocal

from app.modules.inventario.schemas.movimiento_schema import RegistrarEntrada
from app.modules.inventario.services.inventario_service import InventarioService


def main():

    session = SessionLocal()

    try:

        service = InventarioService(session)

        inventario = service.registrar_entrada(
            RegistrarEntrada(
                producto_id=1,
                cantidad=20,
                motivo="Compra inicial",
                referencia="OC-000001",
            )
        )

        print("=" * 40)
        print("Entrada registrada")
        print("=" * 40)
        print(f"Producto: {inventario.producto_id}")
        print(f"Stock actual: {inventario.stock_actual}")

    finally:
        session.close()


if __name__ == "__main__":
    main()