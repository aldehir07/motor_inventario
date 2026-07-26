from sqlalchemy import select
from app.modules.catalogo.models.marca import Marca
from app.seeders.base_seeder import BaseSeeder


class MarcaSeeder(BaseSeeder):
    def run(self):

        marcas = [
            "Dell",
            "HP",
            "Lenovo",
            "Kingston",
            "Logitech",
            "Samsung",
        ]

        for nombre in marcas:

            existe = self.session.scalar(
                select(Marca).where(
                    Marca.nombre == nombre
                )
            )

            if existe:
                continue

            self.add(
                Marca(nombre=nombre)
            )

        self.commit()
