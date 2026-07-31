from decimal import Decimal

from pydantic import BaseModel


class VentaPorMes(BaseModel):

    anio: int

    mes: int

    total: Decimal