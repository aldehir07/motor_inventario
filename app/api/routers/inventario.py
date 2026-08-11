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

from app.api.schemas.reporte_inventario_response import (
    StockBajoResponse,
    ValorInventarioResponse,
    ValorTotalInventarioResponse,
)

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

@router.get(
    "/reportes/stock-bajo",
    response_model=ApiResponse[list[StockBajoResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener productos con stock bajo",
)
def obtener_stock_bajo(
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    productos = service.obtener_stock_bajo()

    return success_response(
        productos,
        "Productos con stock bajo obtenidos correctamente.",
    )


@router.get(
    "/reportes/sin-stock",
    response_model=ApiResponse[list[StockBajoResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener productos sin stock",
)
def obtener_sin_stock(
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    productos = service.obtener_sin_stock()

    return success_response(
        productos,
        "Productos sin stock obtenidos correctamente.",
    )


@router.get(
    "/reportes/valor",
    response_model=ApiResponse[list[ValorInventarioResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener valor de inventario por producto",
)
def obtener_valor_inventario(
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    productos = service.obtener_valor_inventario()

    return success_response(
        productos,
        "Valor de inventario obtenido correctamente.",
    )


@router.get(
    "/reportes/valor-total",
    response_model=ApiResponse[
        ValorTotalInventarioResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Obtener valor total del inventario",
)
def obtener_valor_total_inventario(
    service: Annotated[
        InventarioService,
        Depends(get_inventario_service),
    ],
):
    valor_total = service.obtener_valor_total_inventario()

    data = ValorTotalInventarioResponse(
        valor_total=valor_total,
    )

    return success_response(
        data,
        "Valor total del inventario obtenido correctamente.",
    )