from app.seeders.base_seeder import BaseSeeder
from app.seeders.catalogo.categoria_seeder import CategoriaSeeder
from app.seeders.catalogo.marca_seeder import MarcaSeeder
from app.seeders.catalogo.proveedor_seeder import ProveedorSeeder
from app.seeders.catalogo.unidad_medida_seeder import UnidadMedidaSeeder


class CatalogoSeeder(BaseSeeder):

    def run(self):
        CategoriaSeeder(self.session).run()
        MarcaSeeder(self.session).run()
        ProveedorSeeder(self.session).run()
        UnidadMedidaSeeder(self.session).run()
        
        