from sqlalchemy import select
from app.modules.catalogo.models.unidad_medida import UnidadMedida
from app.seeders.base_seeder import BaseSeeder

class UnidadMedidaSeeder(BaseSeeder):
    def run(self):

        unidades = [

            ("Unidad", "UND"),
            ("Caja", "CJ"),
            ("Kilogramo", "KG"),
            ("Litro", "LT"),
            ("Metro", "MT"),

        ]

        for nombre, abreviatura in unidades:
            existe = self.session.scalar(
                select(UnidadMedida).where(
                    UnidadMedida.abreviatura == abreviatura
                )
            )

            if existe:
                continue

            self.add(
                UnidadMedida(
                    nombre=nombre,
                    abreviatura=abreviatura,
                )
            )

        self.commit()