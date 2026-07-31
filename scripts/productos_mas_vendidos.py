from app.database.session import SessionLocal

from app.modules.ventas.services.venta_service import (
    VentaService,
)


def main():

    session = SessionLocal()

    try:

        service = VentaService(session)

        productos = (
            service.obtener_productos_mas_vendidos()
        )

        print("=" * 90)
        print("PRODUCTOS MÁS VENDIDOS")
        print("=" * 90)

        if not productos:

            print("No existen ventas confirmadas.")

            return

        posicion = 1

        for producto in productos:

            print(

                f"{posicion:>2}. "

                f"{producto.codigo:<12}"

                f"{producto.nombre:<35}"

                f"Vendidos: {producto.cantidad_vendida}"

            )

            posicion += 1

    finally:

        session.close()


if __name__ == "__main__":
    main()