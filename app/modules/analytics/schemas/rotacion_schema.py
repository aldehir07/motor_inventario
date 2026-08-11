from decimal import Decimal

from pydantic import BaseModel


class RotacionInventarioItem(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    stock_actual: int

    vendidos: int

    rotacion: Decimal