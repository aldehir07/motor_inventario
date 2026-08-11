from app.database.session import SessionLocal
from app.modules.catalogo.repositories.catalogo_repository import CatalogoRepository

def main():
    session = SessionLocal()

    try:
        repo = CatalogoRepository(session)

        productos = repo.get_all()

        print(productos)

    finally:
        session.close()


if __name__ == "__main__":
    main()