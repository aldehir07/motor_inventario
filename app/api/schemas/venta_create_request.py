from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class VentaDetalleCreateRequest(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)


class VentaCreateRequest(BaseModel):
    numero_documento: str = Field(
        min_length=1,
        max_length=50,
    )
    fecha: date
    impuesto: Decimal = Field(ge=0)

    detalles: list[VentaDetalleCreateRequest]