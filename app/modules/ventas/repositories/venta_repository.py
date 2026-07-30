from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.modules.ventas.models.venta import Venta
from app.shared.repositories.base_repository import BaseRepository


class VentaRepository(BaseRepository[Venta]):

    def __init__(self, session: Session):
        super().__init__(session, Venta)

    def get_by_numero_documento(
        self,
        numero_documento: str,
    ) -> Venta | None:

        stmt = select(Venta).where(
            Venta.numero_documento == numero_documento
        )

        return self.session.scalar(stmt)

    def get_by_id_with_detalles(
        self,
        venta_id: int,
    ) -> Venta | None:

        stmt = (
            select(Venta)
            .options(
                joinedload(Venta.detalles)
            )
            .where(
                Venta.id == venta_id
            )
        )

        result = self.session.execute(stmt)

        return result.unique().scalar_one_or_none()