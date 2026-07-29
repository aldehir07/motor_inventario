from app.database.session import SessionLocal

from app.modules.compras.repositories.compra_repository import (
    CompraRepository,
)


def main():

    session = SessionLocal()

    try:

        repo = CompraRepository(session)

        compras = repo.get_all()

        print(compras)

    finally:

        session.close()


if __name__ == "__main__":
    main()