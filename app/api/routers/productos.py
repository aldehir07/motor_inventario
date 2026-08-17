from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from decimal import Decimal

from app.api.schemas.paginated_response import PaginatedResponse
from app.api.schemas.producto_response import ProductoResponse

from app.modules.catalogo.services.catalogo_service import CatalogoService

from app.api.schemas.producto_create_request import (
    ProductoCreateRequest,
)

from app.modules.catalogo.schemas.producto_schema import (
    ProductoCreate,
)

from app.api.schemas.producto_update_request import (
    ProductoUpdateRequest,
)

from app.modules.catalogo.schemas.producto_schema import (
    ProductoUpdate,
)
from app.modules.catalogo.schemas.producto_filter import ProductoFilter

from app.api.dependencies.catalogo import (
    get_catalogo_service,
)
from app.api.dependencies.auth import require_roles
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.api.utils.responses import success_response
from app.api.schemas.api_response import ApiResponse

router = APIRouter(

    prefix="/productos",

    tags=["Productos"],

)

@router.get(
    "",
    response_model=ApiResponse[
        PaginatedResponse[ProductoResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar productos",
    description="Obtiene los productos paginados y filtrados.",
)
def listar_productos(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],

    pagina: int = Query(
        default=1,
        ge=1,
    ),

    limite: int = Query(
        default=20,
        ge=1,
        le=100,
    ),

    busqueda: str | None = Query(
        default=None,
        min_length=1,
    ),

    categoria_id: int | None = Query(
        default=None,
        ge=1,
    ),

    proveedor_id: int | None = Query(
        default=None,
        ge=1,
    ),

    marca_id: int | None = Query(
        default=None,
        ge=1,
    ),

    unidad_medida_id: int | None = Query(
        default=None,
        ge=1,
    ),

    activo: bool | None = Query(
        default=True,
    ),

    precio_min: Decimal | None = Query(
        default=None,
        ge=0,
    ),

    precio_max: Decimal | None = Query(
        default=None,
        ge=0,
    ),
):
    filtros = ProductoFilter(
        busqueda=busqueda,
        categoria_id=categoria_id,
        proveedor_id=proveedor_id,
        marca_id=marca_id,
        unidad_medida_id=unidad_medida_id,
        activo=activo,
        precio_min=precio_min,
        precio_max=precio_max,
    )

    resultado = service.listar_productos(
        pagina=pagina,
        limite=limite,
        filtros=filtros,
    )

    return success_response(
        resultado,
        "Productos obtenidos correctamente.",
    )


@router.get(
    "/{producto_id}",
    response_model=ApiResponse[ProductoResponse],
    status_code=status.HTTP_200_OK
)
def obtener_productor(
    producto_id: int, 
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):

    producto = service.obtener_producto_port_id(
        producto_id
    )

    return success_response(
        producto,
        "Producto obtenido correctamente."
    )


@router.post(
    "",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear producto",
    description="Registra un nuevo producto en el catálogo.",
    dependencies=[
        Depends(require_roles({RolUsuario.ADMIN}))
    ],
)
def crear_producto(

    request: ProductoCreateRequest,
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service)
    ]

):

    data = ProductoCreate(

        **request.model_dump()

    )

    return service.crear_producto(
        data
    )


@router.put(

    "/{producto_id}",
    response_model=ProductoResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar producto",
    description="Actualiza la información de un producto.",
    dependencies=[
        Depends(require_roles({RolUsuario.ADMIN}))
    ],

)
def actualizar_producto(

    producto_id: int,
    request: ProductoUpdateRequest,
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service)
    ]

):
    data = ProductoUpdate(

        **request.model_dump(
            exclude_unset=True
        )

    )

    return service.actualizar_producto(

        producto_id,

        data,

    )


@router.patch(
    "/{producto_id}/desactivar",
    response_model=ProductoResponse,
    status_code=status.HTTP_200_OK,
    summary="Desactivar producto",
    description="Desactiva lógicamente un producto.",
    dependencies=[
        Depends(require_roles({RolUsuario.ADMIN}))
    ],
)
def desactivar_producto(

    producto_id: int,
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service)
    ]

):

    return service.desactivar_producto(
        producto_id
    )


@router.get(
    "/codigo/{codigo}",
    response_model=ProductoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener producto por código",
    description="Obtiene un producto utilizando su código.",
)
def obtener_producto_por_codigo(

    codigo: str,

    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service)
    ]

):

    return service.obtener_producto_por_codigo(
        codigo
    )