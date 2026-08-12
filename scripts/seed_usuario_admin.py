from app.database.session import SessionLocal
from app.seeders.usuarios.usuario_seeder import UsuarioSeeder


def main():

    session = SessionLocal()

    try:

        seeder = UsuarioSeeder(session)

        seeder.run()

        print("Usuario administrador creado correctamente.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()


if __name__ == "__main__":
    main()