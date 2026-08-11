from pydantic import BaseModel


class ProductoResponse(BaseModel):

    id: int

    codigo: str

    sku: str

    nombre: str

    descripcion: str | None

    precio_compra_actual: float

    precio_venta_actual: float

    stock_minimo: int

    stock_maximo: int

    activo: bool

    class Config:
        from_attributes = True