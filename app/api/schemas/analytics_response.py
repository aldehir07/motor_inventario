from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class DashboardResumenResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    productos: int
    productos_activos: int
    stock_bajo: int
    sin_stock: int
    valor_inventario: Decimal
    compras: int
    ventas: int


class VentaPorMesResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    anio: int
    mes: int
    total: Decimal


class CompraPorMesResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    anio: int
    mes: int
    total: Decimal


class RotacionInventarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    producto_id: int
    codigo: str
    nombre: str
    stock_actual: int
    vendidos: int
    rotacion: Decimal
    

class ABCResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    producto_id: int
    codigo: str
    nombre: str
    valor: Decimal
    clasificacion: str