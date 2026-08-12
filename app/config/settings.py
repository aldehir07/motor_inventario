import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Motor Inteligente para Inventarios",
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
    )

    JWT_ALGORITHM = os.getenv(
        "JWT_ALGORITHM",
        "HS256",
    )

    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
            "30",
        )
    )

    ADMIN_EMAIL = os.getenv(
        "ADMIN_EMAIL",
    )

    ADMIN_PASSWORD = os.getenv(
        "ADMIN_PASSWORD",
    )


settings = Settings()