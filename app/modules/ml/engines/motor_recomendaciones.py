from datetime import date

from sqlalchemy.orm import Session

from app.modules.analytics.services.analytics_service import AnalyticsService
from app.modules.ml.datasets.dataset_builder import DatasetBuilder
from app.modules.ml.predictors.demanda_predictor import DemandaPredictor
from app.modules.ml.services.recomendador_compras import RecomendadorCompras

class MotorRecomendaciones:

    def __init__(
        self,
        session: Session,
    ):

        self.session = session

        self.dataset_builder = DatasetBuilder(session)

        self.predictor = DemandaPredictor()

        self.analytics = AnalyticsService(session)

        self.recomendador = RecomendadorCompras()

    def _obtener_indicadores(self):
        return {
            "abc": {},
            "rotacion": {}
        }

    def recomendar_compras(self):
        df = self.dataset_builder.construir_dataset_inventario()
    
        recomendaciones = []
    
        indicadores = self._obtener_indicadores()

        hoy = date.today()
    
        for producto in df.itertuples():
            demanda = self.predictor.predecir(
                anio=hoy.year,
                mes=hoy.month,
                dia=hoy.day
            )
            recomendacion = self.recomendador.recomendar(
                producto,
                demanda,
                indicadores
            )
            recomendaciones.append(recomendacion)
    
        return recomendaciones
    