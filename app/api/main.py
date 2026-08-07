from fastapi import FastAPI

from app.api.core.settings import settings
from app.api.routers.health import router as health_router
from app.api.core.cors import configure_cors
from app.api.exceptions.handlers import generic_exception_handler

from app.api.routers.productos import router as productos_router
from app.api.routers.inventario import router as inventario_router

from app.api.exceptions.handlers import (
    duplicate_exception_handler,
)

from app.api.exceptions.handlers import (
    not_found_exception_handler,
)

from app.shared.exceptions.not_found_exception import (
    NotFoundException,
)

from app.shared.exceptions.duplicate_exception import (
    DuplicateException,
)
from app.api.exceptions.handlers import (
    conflict_exception_handler,
)

from app.shared.exceptions.conflict_exception import (
    ConflictException,
)


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

app.add_exception_handler(
    NotFoundException,
    not_found_exception_handler,
)

app.add_exception_handler(
    DuplicateException,
    duplicate_exception_handler,
)

app.add_exception_handler(
    ConflictException,
    conflict_exception_handler,
)

app.include_router(
    health_router
)

app.include_router(productos_router)
app.include_router(inventario_router)