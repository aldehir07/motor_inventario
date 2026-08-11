from datetime import date
from sqlalchemy.orm import Session

from app.modules.catalogo.repositories.catalogo_repository import CatalogoRepository
from app.modules.ml.engines.motor_recomendaciones import MotorRecomendaciones
from app.modules.ml.predictors.demanda_predictor import DemandaPredictor
from app.shared.exceptions.not_found_exception import NotFoundException


class MLService:

    def __init__(self, session: Session):
        self.session = session
        self.predictor = DemandaPredictor()
        self.motor = MotorRecomendaciones(session)
        self.producto_repository = CatalogoRepository(session)

    def predecir_demanda(
        self,
        producto_id: int,
        fecha: date,
    ) -> float:
        # 1. Validar que el producto existe y obtener sus detalles
        producto = self.producto_repository.get_by_id(producto_id)
        if not producto:
            raise NotFoundException(f"El producto con ID {producto_id} no existe.")

        # 2. Ejecutar la predicción usando los atributos del producto y la fecha
        return self.predictor.predecir(
            producto_id=producto.id,
            categoria_id=producto.categoria_id,
            marca_id=producto.marca_id,
            fecha=fecha,
        )

    def recomendar_comprar(self):
        return self.motor.recomendar_compras()

# from sqlalchemy.orm import Session
# from datetime import date

# from app.modules.ml.datasets.dataset_builder import DatasetBuilder

# from app.modules.ml.engines.motor_recomendaciones import (
#     MotorRecomendaciones,
# )
# from app.modules.ml.predictors.demanda_predictor import (
#     DemandaPredictor,
# )


# class MLService:

#     def __init__(
#         self,
#         session: Session,
#     ):

#         self.session = session
#         self.predictor = DemandaPredictor()
#         self.motor = MotorRecomendaciones(session)

#     def predecir_demanda(
#         self,
#         anio: int,
#         mes: int,
#         dia: int,
#     ) -> float:

#         return self.predictor.predecir(
#             anio,
#             mes,
#             dia,
#         )

#     def recomendar_comprar(self):
#         return self.motor.recomendar_compras()

    
    