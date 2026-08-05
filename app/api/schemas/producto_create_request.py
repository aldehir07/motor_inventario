from pydantic import BaseModel
from pydantic import ConfigDict


class ProductoCreateRequest(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    categoria_id: int

    proveedor_id: int

    marca_id: int

    unidad_medida_id: int

    codigo: str

    sku: str

    nombre: str

    descripcion: str | None = None

    precio_compra_actual: float

    precio_venta_actual: float

    stock_minimo: int

    stock_maximo: int