from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CompraDetalleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    producto_id: int
    cantidad: int
    costo_unitario: Decimal
    subtotal: Decimal


class CompraResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    proveedor_id: int
    numero_documento: str
    fecha: date
    subtotal: Decimal
    impuesto: Decimal
    total: Decimal
    estado: str
    detalles: list[CompraDetalleResponse]