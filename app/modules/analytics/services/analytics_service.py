from decimal import Decimal

from sqlalchemy.orm import Session

from app.modules.analytics.repositories.analytics_repository import (
    AnalyticsRepository,
)
from app.modules.analytics.schemas.dashboard_schema import (
    DashboardResumen,
)
from app.modules.inventario.services.inventario_service import (
    InventarioService,
)
from app.modules.analytics.schemas.ventas_mes_schema import (
    VentaPorMes,
)

from app.modules.analytics.schemas.compras_mes_schema import (
    CompraPorMes,
)
from app.modules.analytics.schemas.rotacion_schema import (
    RotacionInventarioItem,
)
from app.modules.analytics.schemas.abc_schema import (
    ABCItem,
)

class AnalyticsService:

    def __init__(self, session: Session):

        self.session = session

        self.analytics_repository = AnalyticsRepository(session)

        self.inventario_service = InventarioService(session)

    def obtener_dashboard(
        self,
    ) -> DashboardResumen:

        valor = (
            self.inventario_service
            .obtener_valor_total_inventario()
        )

        stock_bajo = len(
            self.inventario_service
            .obtener_stock_bajo()
        )

        return DashboardResumen(

            productos=self.analytics_repository.total_productos(),

            productos_activos=self.analytics_repository.productos_activos(),

            stock_bajo=stock_bajo,

            sin_stock=self.analytics_repository.productos_sin_stock(),

            valor_inventario=valor,

            compras=self.analytics_repository.total_compras(),

            ventas=self.analytics_repository.total_ventas(),

        )

    def obtener_ventas_por_mes(
        self,
    ) -> list[VentaPorMes]:

        filas = (
            self.analytics_repository
            .ventas_por_mes()
        )

        return [

            VentaPorMes(

                anio=int(fila.anio),

                mes=int(fila.mes),

                total=fila.total,

            )

            for fila in filas

        ]

    def obtener_compras_por_mes(
        self,
    ) -> list[CompraPorMes]:

        filas = (
            self.analytics_repository
            .compras_por_mes()
        )

        return [

            CompraPorMes(

                anio=int(fila.anio),

                mes=int(fila.mes),

                total=fila.total,

            )

            for fila in filas

        ]

    def obtener_rotacion_inventario(
        self,
    ) -> list[RotacionInventarioItem]:

        filas = (
            self.analytics_repository
            .rotacion_inventario()
        )

        resultado = []

        for fila in filas:

            if fila.stock_actual > 0:

                rotacion = (
                    Decimal(fila.vendidos)
                    / Decimal(fila.stock_actual)
                )

            else:

                rotacion = Decimal("0")

            resultado.append(

                RotacionInventarioItem(

                    producto_id=fila.id,

                    codigo=fila.codigo,

                    nombre=fila.nombre,

                    stock_actual=fila.stock_actual,

                    vendidos=fila.vendidos,

                    rotacion=rotacion.quantize(
                        Decimal("0.01")
                    ),

                )

            )

        return resultado

    def obtener_abc(
        self,
    ) -> list[ABCItem]:

        filas = (
            self.analytics_repository
            .valor_productos()
        )

        total = len(filas)

        resultado = []

        for indice, fila in enumerate(filas):

            porcentaje = (indice + 1) / total

            if porcentaje <= 0.20:

                clase = "A"

            elif porcentaje <= 0.50:

                clase = "B"

            else:

                clase = "C"

            resultado.append(

                ABCItem(

                    producto_id=fila.id,

                    codigo=fila.codigo,

                    nombre=fila.nombre,

                    valor=fila.valor,

                    clasificacion=clase,

                )

            )

        return resultado

    