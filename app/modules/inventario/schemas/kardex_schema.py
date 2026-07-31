from datetime import datetime

from pydantic import BaseModel

from app.modules.inventario.enums.tipo_movimiento import TipoMovimiento


class KardexItem(BaseModel):

    fecha: datetime

    tipo: TipoMovimiento

    cantidad: int

    stock_anterior: int

    stock_nuevo: int

    motivo: str | None

    referencia: str | None