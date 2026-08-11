from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.ml import get_ml_service
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.ml_response import (
    PrediccionDemandaResponse,
    RecomendacionCompraResponse,
)
from app.api.utils.responses import success_response
from app.modules.ml.services.ml_service import MLService

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"],
)


@router.get(
    "/prediccion",
    response_model=ApiResponse[PrediccionDemandaResponse],
    status_code=status.HTTP_200_OK,
    summary="Predecir demanda de un producto para una fecha",
)
def predecir_demanda(
    producto_id: int,
    fecha: date,
    service: Annotated[
        MLService,
        Depends(get_ml_service),
    ],
):
    demanda = service.predecir_demanda(
        producto_id=producto_id,
        fecha=fecha,
    )

    response_data = PrediccionDemandaResponse(
        producto_id=producto_id,
        fecha=fecha,
        demanda_estimada=demanda,
    )

    return success_response(
        response_data,
        "Predicción de demanda calculada correctamente."
    )


@router.get(
    "/recomendaciones",
    response_model=ApiResponse[list[RecomendacionCompraResponse]],
    status_code=status.HTTP_200_OK,
    summary="Obtener recomendaciones de compra inteligentes",
)
def obtener_recomendaciones(
    service: Annotated[
        MLService,
        Depends(get_ml_service),
    ]
):
    recomendaciones = service.recomendar_comprar()
    return success_response(
        recomendaciones,
        "Recomendaciones de compra obtenidas correctamente."
    )