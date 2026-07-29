from sqlalchemy import select

from app.modules.catalogo.models.producto import Producto
from app.modules.compras.models.compra import Compra
from app.modules.inventario.models.inventario import Inventario


def test_inventory_relationships_can_be_imported() -> None:
    assert Producto.__tablename__ == "productos"
    assert Inventario.__tablename__ == "inventarios"


def test_compra_query_can_compile_with_relationships_loaded() -> None:
    stmt = select(Compra)
    compiled = str(stmt)
    assert "compras" in compiled
