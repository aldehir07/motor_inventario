from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
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

router = APIRouter(

    prefix="/productos",

    tags=["Productos"],

)

@router.get(

    "",

    response_model=PaginatedResponse[
        ProductoResponse
    ],

    status_code=200,

    summary="Listar productos",

    description="Obtiene los productos paginados.",

)

def listar_productos(

    pagina: int = Query(
        default=1,
        ge=1,
    ),

    limite: int = Query(
        default=20,
        ge=1,
        le=100,
    ),

    db: Annotated[
        Session,
        Depends(get_db),
    ] = None,

):

    service = CatalogoService(db)

    resultado = service.listar_productos(
        pagina=pagina,
        limite=limite,
    )

    return resultado
@router.get(
    "/{producto_id}",
    response_model=ProductoResponse,
    status_code=200,
    summary="Obtener un producto",
    description="Obtiene un producto mediante su identificador",
)
def obtener_productor(
    producto_id: int, 
    db: Annotated[
        Session, 
        Depends(get_db),
        ],
):
    service = CatalogoService(db)

    return service.obtener_producto_port_id(
        producto_id
    )

@router.post(
    "",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear producto",
    description="Registra un nuevo producto en el catálogo.",
)
def crear_producto(

    request: ProductoCreateRequest,

    db: Annotated[
        Session,
        Depends(get_db),
    ],

):

    service = CatalogoService(db)

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

)
def actualizar_producto(

    producto_id: int,

    request: ProductoUpdateRequest,

    db: Annotated[
        Session,
        Depends(get_db),
    ],

):

    service = CatalogoService(db)

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
)
def desactivar_producto(

    producto_id: int,

    db: Annotated[
        Session,
        Depends(get_db),
    ],

):

    service = CatalogoService(db)

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

    db: Annotated[
        Session,
        Depends(get_db),
    ],

):

    service = CatalogoService(db)

    return service.obtener_producto_por_codigo(
        codigo
    )