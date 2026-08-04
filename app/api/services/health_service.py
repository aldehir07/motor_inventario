from datetime import datetime

from app.api.core.settings import settings
from app.api.schemas.health_schema import HealthResponse


class HealthService:

    def obtener_estado(self) -> HealthResponse:

        return HealthResponse(

            status="OK",

            application=settings.title,

            version=settings.version,

            timestamp=datetime.now(),

        )