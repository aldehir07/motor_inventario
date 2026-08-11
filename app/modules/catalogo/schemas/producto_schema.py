from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class ProductoCreate(BaseModel):
    categoria_id : int
    proveedor_id: int
    marca_id: int
    unidad_medida_id: int

    codigo: str = Field(..., min_length=1, max_length=30)
    sku: str = Field(..., min_length=1, max_length=50)
    nombre: str = Field(..., min_length=1, max_length=150)
    descripcion: str | None = None
    precio_compra_actual: Decimal = Field(gt=0)
    precio_venta_actual: Decimal = Field(gt=0)
    stock_minimo: int = Field(default=0, ge=0)
    stock_maximo: int = Field(default=100, ge=0)


class ProductoUpdate(BaseModel):

    nombre: str | None = Field(default=None, min_length=3, max_length=150)
    descripcion: str | None = None
    precio_compra_actual: Decimal | None = Field(default=None, gt=0)
    precio_venta_actual: Decimal | None = Field(default=None, gt=0)
    stock_minimo: int | None = Field(default=None, ge=0)
    stock_maximo: int | None = Field(default=None, ge=0)
    activo: bool | None = None

class ProductoResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    id: int
    codigo: str
    sku: str
    nombre: str
    descripcion: str | None
    precio_compra_actual: Decimal
    precio_venta_actual: Decimal
    stock_minimo: int
    stock_maximo: int
    activo: bool

class ProductoUpdate(BaseModel):

    nombre: str | None = None
    descripcion: str | None = None
    precio_compra_actual: Decimal | None = None
    precio_venta_actual: Decimal | None = None
    stock_minimo: int | None = None
    stock_maximo: int | None = None
    categoria_id: int | None = None
    proveedor_id: int | None = None
    marca_id: int | None = None
    unidad_medida_id: int | None = None