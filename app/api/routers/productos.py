from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.paginated_response import PaginatedResponse
from app.api.schemas.producto_response import ProductoResponse

from app.modules.catalogo.services.catalogo_service import CatalogoService

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