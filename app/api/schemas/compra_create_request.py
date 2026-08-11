from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class CompraDetalleCreateRequest(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)
    costo_unitario: Decimal = Field(gt=0)


class CompraCreateRequest(BaseModel):
    proveedor_id: int
    numero_documento: str = Field(
        min_length=1,
        max_length=50,
    )
    fecha: date
    impuesto: Decimal = Field(ge=0)

    detalles: list[CompraDetalleCreateRequest]