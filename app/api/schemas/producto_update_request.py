from pydantic import BaseModel, ConfigDict



class ProductoUpdateRequest(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    categoria_id: int | None = None

    proveedor_id: int | None = None

    marca_id: int | None = None

    unidad_medida_id: int | None = None

    codigo: str | None = None

    sku: str | None = None

    nombre: str | None = None

    descripcion: str | None = None

    precio_compra_actual: float | None = None

    precio_venta_actual: float | None = None

    stock_minimo: int | None = None

    stock_maximo: int | None = None