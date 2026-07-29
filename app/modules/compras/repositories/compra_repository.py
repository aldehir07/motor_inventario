from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.modules.compras.models.compra import Compra
from app.shared.repositories.base_repository import BaseRepository


class CompraRepository(BaseRepository[Compra]):

    def __init__(self, session: Session):
        super().__init__(
            session,
            Compra,
        )


    def get_by_numero_documento(
        self,
        numero_documento: str,
    ) -> Compra | None:

        stmt = select(Compra).where(
            Compra.numero_documento == numero_documento
        )

        return self.session.scalar(stmt)


    def get_by_proveedor(
        self,
        proveedor_id: int,
    ) -> list[Compra]:

        stmt = (
            select(Compra)
            .where(
                Compra.proveedor_id == proveedor_id
            )
            .order_by(
                Compra.fecha.desc()
            )
        )

        return list(
            self.session.scalars(stmt)
        )

    def get_by_id_with_detalles(
        self,
        compra_id: int,
    ) -> Compra | None:

        stmt = (
            select(Compra)
            .options(
                joinedload(Compra.detalles)
            )
            .where(
                Compra.id == compra_id
            )
        )

        result = self.session.execute(stmt)

        return result.unique().scalar_one_or_none()