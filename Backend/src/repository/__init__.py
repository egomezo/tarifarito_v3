from injector import Module, singleton

from .anios_repository import AniosRepository
from .empresas_repository import EmpresasRepository
from .mercados_repository import MercadosRepository
from .empresa_mercado_repository import EmpresaMercadoRepository
from .gestor.ntolerancia_repository import NtoleranciaRepository


class RepositoryModule(Module):
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def configure(self, binder):
        anios_repository = AniosRepository(self.db)
        empresas_repository = EmpresasRepository(self.db)
        mercados_repository = MercadosRepository(self.db)
        empresa_mercado_repository = EmpresaMercadoRepository(self.db)
        ntolerancia_repository = NtoleranciaRepository(self.mongodb)

        binder.bind(AniosRepository, to=anios_repository, scope=singleton)
        binder.bind(EmpresasRepository, to=empresas_repository, scope=singleton)
        binder.bind(MercadosRepository, to=mercados_repository, scope=singleton)
        binder.bind(EmpresaMercadoRepository, to=empresa_mercado_repository, scope=singleton)
        binder.bind(NtoleranciaRepository, to=ntolerancia_repository, scope=singleton)