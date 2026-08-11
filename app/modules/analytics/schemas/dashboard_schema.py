from decimal import Decimal

from pydantic import BaseModel


class DashboardResumen(BaseModel):

    productos: int
    productos_activos: int
    stock_bajo: int
    sin_stock: int
    valor_inventario: Decimal
    compras: int
    ventas: int