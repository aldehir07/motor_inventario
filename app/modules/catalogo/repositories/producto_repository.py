from app.modules.catalogo.models.producto import Producto
from app.shared.repositories.base_repository import BaseRepository

class ProductoRepository(BaseRepository[Producto]):

    def __init__(self, session):
        super().__init__(session, Producto)