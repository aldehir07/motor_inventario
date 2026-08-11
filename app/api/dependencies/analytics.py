from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.analytics.services.analytics_service import (
    AnalyticsService,
)


def get_analytics_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> AnalyticsService:

    return AnalyticsService(db)