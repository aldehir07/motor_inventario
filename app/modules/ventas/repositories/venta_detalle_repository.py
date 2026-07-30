from sqlalchemy.orm import Session

from app.modules.ventas.models.venta_detalle import VentaDetalle
from app.shared.repositories.base_repository import BaseRepository


class VentaDetalleRepository(BaseRepository[VentaDetalle]):

    def __init__(self, session: Session):
        super().__init__(
            session,
            VentaDetalle,
        )