from dotenv import load_dotenv
import os

# Cargar variables del archvo .env
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DATABASE_URL = os.getenv("DATABASE_URL")
    LOG_LEVEL = os.getenv("LOG_LEVEL")


settings = Settings()