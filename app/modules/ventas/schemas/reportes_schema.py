
from pydantic import BaseModel


class ProductoMasVendidoItem(BaseModel):
    producto_id: int
    codigo: str
    nombre: str
    cantidad_vendida: int