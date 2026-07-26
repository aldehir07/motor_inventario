from app.database.session import SessionLocal

from app.modules.catalogo.services.catalogo_service import CatalogoService

from app.modules.catalogo.schemas.producto_filter import ProductoFilter



def main():

    session = SessionLocal()

    try:

        service = CatalogoService(session)


        filtros = ProductoFilter(
            nombre="Laptop",
            activo=True
        )


        productos = service.filtrar_productos(
            filtros
        )


        print(
            f"Encontrados: {len(productos)}"
        )


        for producto in productos:

            print(
                producto.codigo,
                producto.nombre
            )


    finally:

        session.close()



if __name__ == "__main__":
    main()