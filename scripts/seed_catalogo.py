from app.database.session import SessionLocal
from app.seeders.catalogo.catalogo_seeder import CatalogoSeeder


def main():

    session = SessionLocal()

    try:

        seeder = CatalogoSeeder(session)

        seeder.run()

        print("Catálogo inicial creado correctamente.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()


if __name__ == "__main__":
    main()