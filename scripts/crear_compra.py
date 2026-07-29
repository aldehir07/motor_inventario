from datetime import date
from decimal import Decimal

from app.database.session import SessionLocal

from app.modules.compras.schemas.compra_schema import (
    CompraCreate,
    CompraDetalleCreate,
)
from app.modules.compras.services.compra_service import CompraService


def main():

    session = SessionLocal()

    try:

        service = CompraService(session)

        compra = service.crear_compra(
            CompraCreate(
                proveedor_id=1,
                numero_documento="FAC-2026-001",
                fecha=date.today(),
                impuesto=Decimal("45.00"),
                detalles=[
                    CompraDetalleCreate(
                        producto_id=1,
                        cantidad=5,
                        costo_unitario=Decimal("650.00"),
                    ),
                ]
            )
        )

        print("=" * 50)
        print("COMPRA CREADA")
        print("=" * 50)
        print(f"ID: {compra.id}")
        print(f"Documento: {compra.numero_documento}")
        print(f"Proveedor: {compra.proveedor_id}")
        print(f"Estado: {compra.estado}")
        print(f"Subtotal: {compra.subtotal}")
        print(f"Impuesto: {compra.impuesto}")
        print(f"Total: {compra.total}")

    finally:
        session.close()


if __name__ == "__main__":
    main()