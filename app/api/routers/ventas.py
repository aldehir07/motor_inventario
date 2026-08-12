from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.ventas import get_venta_service
from app.api.dependencies.auth import require_roles
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.venta_create_request import VentaCreateRequest
from app.api.schemas.venta_response import VentaResponse
from app.api.utils.responses import success_response
from app.modules.ventas.schemas.venta_schema import VentaCreate
from app.modules.ventas.services.venta_service import VentaService

from app.api.schemas.reporte_venta_response import (
    ProductoMasVendidoResponse,
)

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
    "/{ventas_id}/confirmar",
    response_model=ApiResponse[VentaResponse],
    status_code=status.HTTP_200_OK,
    summary="Confirmar venta",
    dependencies=[
        Depends(require_roles({RolUsuario.ADMIN}))
    ],
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

@router.get(
    "/reportes/productos-mas-vendidos",
    response_model=ApiResponse[
        list[ProductoMasVendidoResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Obtener productos mas vendidos."
)
def obtener_productos_mas_vendidos(
    service: Annotated[
        VentaService,
        Depends(get_venta_service),
    ]
):
    productos = service.obtener_productos_mas_vendidos()

    return success_response(
        productos,
        "Productos mas vendidos obtenidos correctamente."
    )

@router.get(
    "/{venta_id}",
    response_model=ApiResponse[VentaResponse],
    status_code=status.HTTP_200_OK,
    summary="Obtener una venta",
)
def obtener_venta(
    venta_id: int,
    service: Annotated[
        VentaService,
        Depends(get_venta_service),
    ],
):
    venta = service.obtener_venta_por_id(venta_id)

    return success_response(
        venta,
        "Venta obtenida correctamente.",
    )