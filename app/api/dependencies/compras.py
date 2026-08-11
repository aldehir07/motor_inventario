from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.compras.services.compra_service import (
    CompraService,
)


def get_compra_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> CompraService:

    return CompraService(db)