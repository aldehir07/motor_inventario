from sqlalchemy import select
from app.modules.catalogo.models.categoria import Categoria
from app.seeders.base_seeder import BaseSeeder

class CategoriaSeeder(BaseSeeder):
    def run(self):

        categorias = [
            ("Electrónica", "Productos electrónicos"),
            ("Oficina", "Artículos de oficina"),
            ("Limpieza", "Productos de limpieza"),
            ("Alimentos", "Productos alimenticios"),
        ]

        for nombre, descripcion in categorias:

            existe = self.session.scalar(
                select(Categoria).where(Categoria.nombre == nombre)
            )

            if existe:
                continue

            self.add(
                Categoria(
                    nombre=nombre,
                    descripcion=descripcion,
                )
            )

        self.commit()