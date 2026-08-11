from datetime import date

from sqlalchemy.orm import Session

from app.modules.analytics.services.analytics_service import AnalyticsService
from app.modules.ml.datasets.dataset_builder import DatasetBuilder
from app.modules.ml.predictors.demanda_predictor import DemandaPredictor
from app.modules.ml.services.recomendador_compras import RecomendadorCompras
from app.modules.ml.services.predictor_quiebre_stock import (PredictorQuiebreStock)
from app.modules.ml.services.detector_exceso_inventario import DetectorExcesoInventario
from app.modules.ml.services.detector_rotacion import DetectorRotacion

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

        self.predictor_quiebre = PredictorQuiebreStock()

        self.detector_exceso = DetectorExcesoInventario()
        self.detector_rotacion = DetectorRotacion()

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
                producto_id=producto.producto_id,
                categoria_id=producto.categoria_id,
                marca_id=producto.marca_id,

                fecha=hoy,
            )
            rotacion = self.detector_rotacion.clasificar(
                demanda
            )
            dias_stock = self.predictor_quiebre.predecir(
                stock_actual=producto.stock_actual,
                demanda_diaria=demanda
            )
            riesgo = self.predictor_quiebre.clasificar_riesgo(
                dias_stock
            )
            exceso_inventario, motivo_exceso = (
                self.detector_exceso.detectar(
                    stock_actual=producto.stock_actual,
                    stock_maximo=producto.stock_maximo,
                    demanda_diaria=demanda,
                )
            )
            recomendacion = self.recomendador.recomendar(
                producto=producto,
                demanda=demanda,
                dias_stock=dias_stock,
                riesgo_quiebre=riesgo,
                exceso_inventario=exceso_inventario,
                motivo_exceso=motivo_exceso,
                rotacion=rotacion,
                indicadores=indicadores
            )
            recomendaciones.append(recomendacion)
    
        return recomendaciones
    