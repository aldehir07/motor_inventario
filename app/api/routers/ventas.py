from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.ventas import get_venta_service
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.venta_create_request import VentaCreateRequest
from app.api.schemas.venta_response import VentaResponse
from app.api.utils.responses import success_response
from app.modules.ventas.schemas.venta_schema import VentaCreate
from app.modules.ventas.services.venta_service import VentaService

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"],
)

@router.post(
    "",
    response_model=ApiResponse[VentaResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Crear venta"
)
def crear_venta(
    request: VentaCreateRequest,
    service: Annotated[
        VentaService,
        Depends(get_venta_service),
    ]
):
    data = VentaCreate(
        **request.model_dump()
    )

    venta = service.crear_venta(data)
    return success_response(
        venta,
        "Venta creada correctamente."
    )

@router.patch(
    "/{ventas}/confirmar",
    response_model=ApiResponse[VentaResponse],
    status_code=status.HTTP_200_OK,
    summary="Confirmar venta",
)
def confirmar_venta(
    venta_id: int,
    service: Annotated[
        VentaService,
        Depends(get_venta_service),
    ]
):
    venta = service.confirmar_venta(venta_id)

    return success_response(
        venta,
        "Venta confirmada correctamente."
    )