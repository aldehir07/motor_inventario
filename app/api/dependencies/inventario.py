from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.inventario.services.inventario_service import (
    InventarioService,
)


def get_inventario_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> InventarioService:

    return InventarioService(db)