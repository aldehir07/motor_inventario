from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.ventas.services.venta_service import (
    VentaService,
)


def get_venta_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> VentaService:

    return VentaService(db)