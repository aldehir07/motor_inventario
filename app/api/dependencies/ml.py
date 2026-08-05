from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.ml.services.ml_service import (
    MLService,
)


def get_ml_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> MLService:

    return MLService(db)