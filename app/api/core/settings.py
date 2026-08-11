from pydantic import BaseModel


class APISettings(BaseModel):

    title: str = "Motor Inteligente para Inventario"

    description: str = (
        "API REST para la gestión de inventario, "
        "analytics y motor inteligente."
    )

    version: str = "1.0.0"

    docs_url: str = "/docs"

    redoc_url: str = "/redoc"

    openapi_url: str = "/openapi.json"


settings = APISettings()