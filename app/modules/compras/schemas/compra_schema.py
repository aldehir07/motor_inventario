from datetime import date
from decimal import Decimal

# Pydantic:
# 2# BaseModel -> Define modelos de datos con validación automática.
# 3# ConfigDict -> Configura el comportamiento del modelo.
# 4# Field -> Permite agregar restricciones, valores por defecto y metadatos a los campos.
from pydantic import BaseModel, ConfigDict, Field

class CompraDetalleCreate(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)
    costo_unitario: Decimal = Field(gt=0)

class CompraCreate(BaseModel):
    proveedor_id: int
    numero_documento: str = Field(min_length=1, max_length=50)
    fecha: date
    impuesto: Decimal = Field(ge=0)

    detalles: list[CompraDetalleCreate]

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