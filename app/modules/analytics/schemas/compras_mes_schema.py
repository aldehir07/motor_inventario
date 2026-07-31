from decimal import Decimal

from pydantic import BaseModel


class CompraPorMes(BaseModel):

    anio: int

    mes: int

    total: Decimal