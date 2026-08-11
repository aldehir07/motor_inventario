from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.inventario.enums.tipo_movimiento import (
    TipoMovimiento,
)


class KardexResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    fecha: datetime
    tipo: TipoMovimiento
    cantidad: int
    stock_anterior: int
    stock_nuevo: int
    motivo: str | None
    referencia: str | None