from sqlalchemy import select
from app.modules.catalogo.models.proveedor import Proveedor
from app.seeders.base_seeder import BaseSeeder


class ProveedorSeeder(BaseSeeder):
    def run(self):
        proveedores = [

            ("Dell Panamá"),
            ("HP Panamá"),
            ("Lenovo Panamá"),
            ("Distribuidora Central"),

        ]

        for nombre in proveedores:

            existe = self.session.scalar(
                select(Proveedor).where(
                    Proveedor.nombre == nombre
                )
            )

            if existe:
                continue

            self.add(
                Proveedor(
                    nombre=nombre
                )
            )

        self.commit()