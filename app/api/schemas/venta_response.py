from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class VentaDetalleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    producto_id: int
    cantidad: int
    precio_unitario: Decimal
    subtotal: Decimal


class VentaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    numero_documento: str
    fecha: date
    subtotal: Decimal
    impuesto: Decimal
    total: Decimal
    estado: str
    detalles: list[VentaDetalleResponse]