from app.modules.ml.schemas.recomendacion_compra_schema import (
    RecomendacionCompra,
)

class RecomendadorCompras:

    def __init__(self):

        pass

    def calcular_cantidad(
        self,
        demanda: float,
        stock: int,
    ) -> int:
        cantidad = max(
            0,
            round(
                demanda - stock
            )
        )

        return cantidad

    def calcular_prioridad(
        self,
        stock: int,
        minimo: int,
        riesgo_quiebre: str,
    ) -> str:
        if riesgo_quiebre == "CRITICO":
            return "CRITICA"

        if riesgo_quiebre == "ALTO":
            return "ALTA"

        if stock <= minimo:
            return "ALTA"

        if riesgo_quiebre == "MEDIO":
            return "MEDIA"

        return "BAJA"

    def recomendar(
        self,
        producto,
        demanda,
        dias_stock,
        riesgo_quibre,
        exceso_inventario,
        motivo_exceso,
        indicadores
    ):
        cantidad = self.calcular_cantidad(
            demanda,
            producto.stock_actual,
        )

        prioridad = self.calcular_prioridad(
            producto.stock_actual,
            producto.stock_minimo,
            riesgo_quiebre=riesgo_quibre
        )

        indice = self._calcular_indice_prioridad(
            producto.stock_actual,
            producto.stock_minimo,
            demanda,
            riesgo_quiebre=riesgo_quibre
        )

        return RecomendacionCompra(
            producto_id=producto.producto_id,
            codigo=producto.codigo,
            nombre=producto.nombre,
            stock_actual=producto.stock_actual,
            stock_minimo=producto.stock_minimo,
            stock_maximo=producto.stock_maximo,
            demanda_estimada=demanda,
            dias_stock=round(dias_stock, 2),
            riesgo_quibre=riesgo_quibre,
            cantidad_recomendada=cantidad,
            indice_prioridad=indice,
            prioridad=prioridad,
            motivo=self._generar_motivo(
                producto.stock_actual,
                producto.stock_minimo,
                demanda,
            ),
            clasificacion_abc=None,
            rotacion=None,
        )

    def _calcular_indice_prioridad(self,
        stock: int, 
        minimo: int, 
        demanda: float,
        riesgo_quiebre: str
    ) -> int:
        
        indice = 0

        if stock <= 0:
            indice += 100

        elif stock < minimo:
            indice += 50

        if demanda > stock:
            indice += 25

        if riesgo_quiebre == "CRITICO":
            indice += 50

        elif riesgo_quiebre == "ALTO":
            indice += 30

        elif riesgo_quiebre == "MEDIO":
            indice += 15

        return min(indice, 100)

    def _generar_motivo(
        self,
        stock: int,
        minimo: int,
        demanda: float
    ) -> str:
        if stock <= 0:
            return "Producto sin existencia."
        if stock < minimo:
            return "Stock por debajo del minimo."
        if demanda > stock:
            return "La demanda estimada supera el inventario."

        return "Inventario suficiente." 