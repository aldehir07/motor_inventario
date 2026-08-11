from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.compras.models.compra_detalle import CompraDetalle
from app.shared.repositories.base_repository import BaseRepository


class CompraDetalleRepository(
    BaseRepository[CompraDetalle]
):

    def __init__(
        self,
        session: Session,
    ):
        super().__init__(
            session,
            CompraDetalle,
        )


    def get_by_compra(
        self,
        compra_id: int,
    ) -> list[CompraDetalle]:

        stmt = (
            select(CompraDetalle)
            .where(
                CompraDetalle.compra_id == compra_id
            )
        )

        return list(
            self.session.scalars(stmt)
        )