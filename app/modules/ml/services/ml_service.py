from sqlalchemy.orm import Session
from datetime import date

from app.modules.ml.datasets.dataset_builder import DatasetBuilder

from app.modules.ml.engines.motor_recomendaciones import (
    MotorRecomendaciones,
)
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
        self.motor = MotorRecomendaciones(session)

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

    def recomendar_comprar(self):
        return self.motor.recomendar_compras()

    
    