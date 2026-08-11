from app.database.session import SessionLocal
from app.modules.catalogo.services.catalogo_service import CatalogoService


def main():

    session = SessionLocal()

    try:

        service = CatalogoService(session)


        producto = service.obtener_producto_por_codigo(
            "P000001"
        )


        print("===================")
        print("Producto encontrado")
        print("===================")

        print(
            producto.nombre
        )

        print(
            producto.precio_venta_actual
        )


    except Exception as e:

        print(
            f"Error: {e}"
        )


    finally:

        session.close()



if __name__ == "__main__":
    main()