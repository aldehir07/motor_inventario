from app.database.session import SessionLocal

from app.modules.compras.services.compra_service import CompraService


def main():

    session = SessionLocal()

    try:

        service = CompraService(session)

        compra = service.confirmar_compra(2)

        print("=" * 50)
        print("COMPRA CONFIRMADA")
        print("=" * 50)
        print(f"ID: {compra.id}")
        print(f"Documento: {compra.numero_documento}")
        print(f"Estado: {compra.estado}")

    finally:
        session.close()


if __name__ == "__main__":
    main()