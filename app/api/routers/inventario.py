from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.inventario import get_inventario_service
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.inventario_response import InventarioResponse
from app.api.schemas.movimiento_inventario_request import (
    AjusteStockRequest,
    EntradaInventarioRequest,
    SalidaInventarioRequest,
)
from app.api.utils.responses import success_response
from app.modules.inventario.schemas.movimiento_schema import (
    AjustarStock,
    RegistrarEntrada,
    RegistrarSalida,
)
from app.modules.inventario.services.inventario_service import (
    InventarioService,
)
from app.api.schemas.kardex_response import KardexResponse

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"],
)

@router.post(
    "/entradas",
    response_model=ApiResponse[InventarioResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Registrar entrada de inventario"
)
def registrar_entrada(
    request: EntradaInventarioRequest,
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ]
):
    data = RegistrarEntrada(
        **request.model_dump()
    )
    inventario = service.registrar_entrada(data)

    return success_response(
        inventario,
        "Entrada registrada correctamente."
    )

@router.post(
    "/salidas",
    response_model=ApiResponse[InventarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Registrar salida de inventario",
)
def registrar_salida(
    request: SalidaInventarioRequest,
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ]
):
    data = RegistrarSalida(
        **request.model_dump()
    )
    inventario = service.registrar_salida(data)

    return success_response(
        inventario,
        "Salida registrada correctamente."
    )

@router.post(
    "/ajustes",
    response_model=ApiResponse[InventarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Ajustar stock de inventario",
)
def ajustar_stock(
    request: AjusteStockRequest,
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    data = AjustarStock(
        **request.model_dump()
    )

    inventario = service.ajustar_stock(data)

    return success_response(
        inventario,
        "Stock ajustado correctamente.",
    )

@router.get(
    "/{producto_id}/kardex",
    response_model=ApiResponse[list[KardexResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener Kardex de un producto",
)
def obtener_kardex(
    producto_id: int,
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    kardex = service.obtener_kardex(producto_id)

    return success_response(
        kardex,
        "Kardex obtenido correctamente.",
    )