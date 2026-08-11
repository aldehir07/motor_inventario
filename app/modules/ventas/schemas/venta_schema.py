from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class VentaDetalleCreate(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)


class VentaCreate(BaseModel):
    numero_documento: str = Field(
        min_length=1,
        max_length=50,
    )

    fecha: date

    impuesto: Decimal = Field(ge=0)

    detalles: list[VentaDetalleCreate]


class VentaDetalleResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    producto_id: int
    cantidad: int
    precio_unitario: Decimal
    subtotal: Decimal


class VentaResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    numero_documento: str
    fecha: date

    subtotal: Decimal
    impuesto: Decimal
    total: Decimal

    estado: str

    detalles: list[VentaDetalleResponse]