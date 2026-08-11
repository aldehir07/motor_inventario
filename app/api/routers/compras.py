from typing import Annotated

from fastapi import APIRouter, Depends, status, Query

from app.api.dependencies.compras import get_compra_service
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.compra_create_request import (
    CompraCreateRequest,
)
from app.api.schemas.compra_response import CompraResponse
from app.api.utils.responses import success_response
from app.modules.compras.schemas.compra_schema import CompraCreate
from app.modules.compras.services.compra_service import CompraService


router = APIRouter(
    prefix="/compras",
    tags=["Compras"],
)


@router.post(
    "",
    response_model=ApiResponse[CompraResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Crear compra",
)
def crear_compra(
    request: CompraCreateRequest,
    service: Annotated[
        CompraService,
        Depends(get_compra_service),
    ],
):
    data = CompraCreate(
        **request.model_dump()
    )

    compra = service.crear_compra(data)

    return success_response(
        compra,
        "Compra creada correctamente.",
    )

@router.patch(
    "/{compra_id}/confirmar",
    response_model=ApiResponse[CompraResponse],
    status_code=status.HTTP_200_OK,
    summary="Confirmar compra",
)
def confirmar_compra(
    compra_id: int,
    service: Annotated[
        CompraService,
        Depends(get_compra_service),
    ],
):
    compra = service.confirmar_compra(compra_id)

    return success_response(
        compra,
        "Compra confirmada correctamente.",
    )

@router.get(
    "/{compra_id}",
    response_model=ApiResponse[CompraResponse],
    status_code=status.HTTP_200_OK,
    summary="Obtener una compra",
)
def obtener_compra(
    compra_id: int,
    service: Annotated[
        CompraService,
        Depends(get_compra_service),
    ],
):
    compra = service.obtener_compra_por_id(compra_id)

    return success_response(
        compra,
        "Compra obtenida correctamente.",
    )


@router.get(
    "",
    response_model=ApiResponse[list[CompraResponse]],
    status_code=status.HTTP_200_OK,
    summary="Listar compras por proveedor",
)
def listar_compras_por_proveedor(
    service: Annotated[
            CompraService,
            Depends(get_compra_service),
        ],
    proveedor_id: int = Query(
        ...,
        ge=1,
    ),
):
    compras = service.listar_compras_por_proveedor(
        proveedor_id
    )

    return success_response(
        compras,
        "Compras obtenidas correctamente.",
    )