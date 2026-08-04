from fastapi import FastAPI

from app.api.core.settings import settings
from app.api.routers.health import router as health_router
from app.api.core.cors import configure_cors
from app.api.exceptions.handlers import generic_exception_handler


app = FastAPI(

    title=settings.title,

    description=settings.description,

    version=settings.version,

    docs_url=settings.docs_url,

    redoc_url=settings.redoc_url,

    openapi_url=settings.openapi_url,

)

configure_cors(app)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.include_router(
    health_router
)