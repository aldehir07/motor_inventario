from sqlalchemy.orm import Session
from app.modules.ml.predictors.demanda_predictor import (
    DemandaPredictor,
)


class MLService:

    def __init__(
        self,
        session: Session,
    ):

        self.session = session
        self.predictor = DemandaPredictor()

    def predecir_demanda(
        self,
        anio: int,
        mes: int,
        dia: int,
    ) -> float:

        return self.predictor.predecir(
            anio,
            mes,
            dia,
        )