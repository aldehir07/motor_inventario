from decimal import Decimal

# pyrefly: ignore [missing-import]
from pydantic import BaseModel


class ProductoFilter(BaseModel):

    busqueda: str | None = None

    categoria_id: int | None = None

    proveedor_id: int | None = None

    marca_id: int | None = None

    unidad_medida_id: int | None = None

    activo: bool | None = True

    precio_min: Decimal | None = None

    precio_max: Decimal | None = None