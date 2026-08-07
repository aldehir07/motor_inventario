from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class StockBajoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    producto_id: int
    codigo: str
    nombre: str
    stock_actual: int
    stock_minimo: int


class ValorInventarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    producto_id: int
    codigo: str
    nombre: str
    stock_actual: int
    costo_unitario: Decimal
    valor_total: Decimal


class ValorTotalInventarioResponse(BaseModel):
    valor_total: Decimal