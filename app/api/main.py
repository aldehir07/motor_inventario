from fastapi import Depends, FastAPI

from app.api.core.settings import settings
from app.api.routers.health import router as health_router
from app.api.core.cors import configure_cors
from app.api.exceptions.handlers import generic_exception_handler
from app.api.dependencies.auth import get_current_user, require_roles

from app.api.routers.auth import router as auth_router
from app.api.routers.usuarios import router as usuarios_router
from app.api.routers.productos import router as productos_router
from app.api.routers.inventario import router as inventario_router
from app.api.routers.compras import router as compras_router
from app.api.routers.ventas import router as ventas_router
from app.api.routers.analytics import router as analytics_router
from app.api.routers.ml import router as ml_router

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

from app.api.exceptions.handlers import (
    credenciales_invalidas_exception_handler,
    token_invalido_exception_handler,
    usuario_inactivo_exception_handler,
    acceso_denegado_exception_handler,
)
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.modules.usuarios.exceptions.credenciales_invalidas_exception import (
    CredencialesInvalidasException,
)
from app.modules.usuarios.exceptions.token_invalido_exception import (
    TokenInvalidoException,
)
from app.modules.usuarios.exceptions.usuario_inactivo_exception import (
    UsuarioInactivoException,
)
from app.modules.usuarios.exceptions.acceso_denegado_exception import (
    AccesoDenegadoException,
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

app.add_exception_handler(
    CredencialesInvalidasException,
    credenciales_invalidas_exception_handler,
)

app.add_exception_handler(
    TokenInvalidoException,
    token_invalido_exception_handler,
)

app.add_exception_handler(
    UsuarioInactivoException,
    usuario_inactivo_exception_handler,
)

app.add_exception_handler(
    AccesoDenegadoException,
    acceso_denegado_exception_handler,
)

app.include_router(health_router)

app.include_router(auth_router)

app.include_router(
    usuarios_router,
    dependencies=[
        Depends(
            require_roles({RolUsuario.ADMIN})
        )
    ],
)

app.include_router(
    productos_router,
    dependencies=[
        Depends(get_current_user)
    ],
)
app.include_router(
    inventario_router,
    dependencies=[
        Depends(get_current_user)
    ],
)
app.include_router(
    compras_router,
    dependencies=[
        Depends(get_current_user)
    ],
)
app.include_router(
    ventas_router,
    dependencies=[
        Depends(get_current_user)
    ],
)
app.include_router(
    analytics_router,
    dependencies=[
        Depends(
            require_roles({RolUsuario.ADMIN})
        )
    ],
)
app.include_router(
    ml_router,
    dependencies=[
        Depends(
            require_roles({RolUsuario.ADMIN})
        )
    ],
)