from app.database.session import SessionLocal
from app.modules.catalogo.services.catalogo_service import CatalogoService


def main():

    session = SessionLocal()

    try:

        service = CatalogoService(session)


        resultado = service.listar_productos(
            pagina=1,
            limite=10
        )


        print(
            "Total:",
            resultado["total"]
        )


        print(
            "Página:",
            resultado["pagina"]
        )


        print("----------------")


        for producto in resultado["items"]:

            print(
                producto.codigo,
                producto.nombre
            )


    finally:

        session.close()



if __name__ == "__main__":
    main()