from app.config.settings import settings
from app.config.logger import logger
from app.database.connection import engine
from sqlalchemy import text

def main():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        logger.success("Conexion con PostgreSQL establecida correctamente")

    except Exception as error:
        logger.exception(error)
        
if __name__ == "__main__":
    main()
