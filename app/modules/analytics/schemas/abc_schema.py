from decimal import Decimal

from pydantic import BaseModel


class ABCItem(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    valor: Decimal

    clasificacion: str