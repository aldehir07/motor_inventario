from pydantic import BaseModel
from decimal import Decimal

class StockBajoItem(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    stock_actual: int

    stock_minimo: int


class ValorInventarioItem(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    stock_actual: int

    costo_unitario: Decimal

    valor_total: Decimal


