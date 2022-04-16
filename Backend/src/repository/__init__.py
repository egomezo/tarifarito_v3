from injector import Module, singleton

from .anios_repository import AniosRepository
from .empresas_repository import EmpresasRepository
from .mercados_repository import MercadosRepository
from .empresa_mercado_repository import EmpresaMercadoRepository
from .gestor.ntolerancia_repository import NtoleranciaRepository
from .gestor.idane_repository import IDaneRepository
from .gestor.icomercial_repository import IComercialRepository
from .gestor.D097Resolucion_repository import D097ResolucionRepository
from .gestor.D097Error_repository import D097ErrorRepository
from .gestor.perdidas_repository import PerdidasRepository
from .gestor.infoAdd_repository import InfoAddRepository
from .revisor.componenteG_repository import ComponenteGRepository
from .revisor.componenteT_repository import ComponenteTRepository
from .revisor.componenteP097_repository import ComponenteP097Repository
from .revisor.componenteP015_repository import ComponenteP015Repository
from .revisor.componenteDtun_repository import ComponenteDtunRepository
from .revisor.componenteD097_repository import ComponenteD097Repository
from .revisor.componenteD015_repository import ComponenteD015Repository
from .revisor.componenteC_repository import ComponenteCRepository
from .revisor.componenteR_repository import ComponenteRRepository
from .revisor.componentesMDB_repository import rComponentesMDBRepository
from .revisor.tarifas_repository import TarifasRepository


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
        idane_repository_repository = IDaneRepository(self.mongodb)
        icomercial_repository = IComercialRepository(self.mongodb)
        D097Resolucion_repository = D097ResolucionRepository(self.mongodb)
        D097Error_repository = D097ErrorRepository(self.mongodb)
        perdidas_repository = PerdidasRepository(self.mongodb)
        infoAdd_repository = InfoAddRepository(self.mongodb)
        componenteG_repository = ComponenteGRepository(self.db, self.mongodb)
        componenteT_repository = ComponenteTRepository(self.db, self.mongodb)
        componenteP097_repository = ComponenteP097Repository(self.db, self.mongodb)
        componenteP015_repository = ComponenteP015Repository(self.db, self.mongodb)
        componenteDtun_repository = ComponenteDtunRepository(self.db, self.mongodb)
        componenteD097_repository = ComponenteD097Repository(self.db, self.mongodb)
        componenteD015_repository = ComponenteD015Repository(self.db, self.mongodb)
        componenteC_repository = ComponenteCRepository(self.db, self.mongodb)
        componenteR_repository = ComponenteRRepository(self.db, self.mongodb)
        componentesMDB_repository = rComponentesMDBRepository(self.mongodb)
        tarifas_repository = TarifasRepository(self.db, self.mongodb)

        binder.bind(AniosRepository, to=anios_repository, scope=singleton)
        binder.bind(EmpresasRepository, to=empresas_repository, scope=singleton)
        binder.bind(MercadosRepository, to=mercados_repository, scope=singleton)
        binder.bind(EmpresaMercadoRepository, to=empresa_mercado_repository, scope=singleton)
        binder.bind(NtoleranciaRepository, to=ntolerancia_repository, scope=singleton)
        binder.bind(IDaneRepository, to=idane_repository_repository, scope=singleton)
        binder.bind(IComercialRepository, to=icomercial_repository, scope=singleton)
        binder.bind(D097ResolucionRepository, to=D097Resolucion_repository, scope=singleton)
        binder.bind(D097ErrorRepository, to=D097Error_repository, scope=singleton)
        binder.bind(PerdidasRepository, to=perdidas_repository, scope=singleton)
        binder.bind(InfoAddRepository, to=infoAdd_repository, scope=singleton)
        binder.bind(ComponenteGRepository, to=componenteG_repository, scope=singleton)
        binder.bind(ComponenteTRepository, to=componenteT_repository, scope=singleton)
        binder.bind(ComponenteP097Repository, to=componenteP097_repository, scope=singleton)
        binder.bind(ComponenteP015Repository, to=componenteP015_repository, scope=singleton)
        binder.bind(ComponenteDtunRepository, to=componenteDtun_repository, scope=singleton)
        binder.bind(ComponenteD097Repository, to=componenteD097_repository, scope=singleton)
        binder.bind(ComponenteD015Repository, to=componenteD015_repository, scope=singleton)
        binder.bind(ComponenteCRepository, to=componenteC_repository, scope=singleton)
        binder.bind(ComponenteRRepository, to=componenteR_repository, scope=singleton)
        binder.bind(rComponentesMDBRepository, to=componentesMDB_repository, scope=singleton)
        binder.bind(TarifasRepository, to=tarifas_repository, scope=singleton)
        