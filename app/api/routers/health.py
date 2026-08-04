from fastapi import APIRouter

from app.api.schemas.health_schema import HealthResponse
from app.api.services.health_service import HealthService

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

service = HealthService()

@router.get("", response_model=HealthResponse)

def health():
    """
    Verifica que la API se encuentre disponible
    """

    return service.obtener_estado()