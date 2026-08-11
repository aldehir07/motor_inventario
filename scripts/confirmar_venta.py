from app.database.session import SessionLocal

from app.modules.ventas.services.venta_service import VentaService


def main():

    session = SessionLocal()

    try:

        service = VentaService(session)

        venta = service.confirmar_venta(1)

        print("=" * 50)
        print("VENTA CONFIRMADA")
        print("=" * 50)
        print(f"ID: {venta.id}")
        print(f"Documento: {venta.numero_documento}")
        print(f"Estado: {venta.estado.value}")

    finally:

        session.close()


if __name__ == "__main__":
    main()