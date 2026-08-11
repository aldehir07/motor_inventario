from datetime import date
from decimal import Decimal

from app.database.session import SessionLocal

from app.modules.ventas.schemas.venta_schema import (
    VentaCreate,
    VentaDetalleCreate,
)

from app.modules.ventas.services.venta_service import VentaService


def main():

    session = SessionLocal()

    try:

        service = VentaService(session)

        venta = service.crear_venta(
            VentaCreate(
                numero_documento="VTA-2026-001",
                fecha=date.today(),
                impuesto=Decimal("0.00"),
                detalles=[
                    VentaDetalleCreate(
                        producto_id=1,
                        cantidad=2,
                    )
                ],
            )
        )

        print("=" * 50)
        print("VENTA CREADA")
        print("=" * 50)
        print(f"ID: {venta.id}")
        print(f"Documento: {venta.numero_documento}")
        print(f"Estado: {venta.estado.value}")
        print(f"Total: {venta.total}")

    finally:
        session.close()


if __name__ == "__main__":
    main()