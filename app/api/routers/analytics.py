from typing import Annotated
from fastapi import APIRouter, Depends, status
from app.api.dependencies.analytics import get_analytics_service
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.analytics_response import (
    DashboardResumenResponse,
    VentaPorMesResponse,
    CompraPorMesResponse,
    RotacionInventarioResponse,
    ABCResponse,
)
from app.api.utils.responses import success_response
from app.modules.analytics.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

@router.get(
    "/dashboard",
    response_model=ApiResponse[DashboardResumenResponse],
    status_code=status.HTTP_200_OK,
    summary="Obyener resumen del dashboard"
)
def obtner_dashboard(
    service: Annotated[
        AnalyticsService,
        Depends(get_analytics_service)
    ]
):
    resumen = service.obtener_dashboard()
    return success_response(
        resumen,
        "Resumen de dashboard obtenido correctamente."
    )

@router.get(
    "/ventas-mes",
    response_model=ApiResponse[list[VentaPorMesResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener ventas acumuladas por mes",
)
def obtener_ventas_por_mes(
    service: Annotated[
        AnalyticsService,
        Depends(get_analytics_service),
    ]
):
    ventas = service.obtener_ventas_por_mes()
    return success_response(
        ventas,
        "Ventas por mes obtenidas correctamente."
    )

@router.get(
    "/compras-mes",
    response_model=ApiResponse[list[CompraPorMesResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener compras acumuladas por mes",
)
def obtener_compras_por_mes(
    service: Annotated[
        AnalyticsService,
        Depends(get_analytics_service),
    ]
):
    compras = service.obtener_compras_por_mes()
    return success_response(
        compras,
        "Compras por mes obtenidas correctamente."
    )
@router.get(
    "/rotacion",
    response_model=ApiResponse[list[RotacionInventarioResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener rotación del inventario por producto",
)
def obtener_rotacion(
    service: Annotated[
        AnalyticsService,
        Depends(get_analytics_service),
    ]
):
    rotacion = service.obtener_rotacion_inventario()
    return success_response(
        rotacion,
        "Rotación de inventario obtenida correctamente."
    )
@router.get(
    "/abc",
    response_model=ApiResponse[list[ABCResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener clasificación ABC de productos",
)
def obtener_abc(
    service: Annotated[
        AnalyticsService,
        Depends(get_analytics_service),
    ]
):
    abc = service.obtener_abc()
    return success_response(
        abc,
        "Clasificación ABC obtenida correctamente."
    )