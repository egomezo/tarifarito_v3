from injector import Module, singleton

from .anios_service import AniosService
from .empresas_service import EmpresasService
from .mercados_service import MercadosService
from .empresa_mercado_service import EmpresaMercadoService
from .gestor.ntolerancia_service import NtoleranciaService
from .gestor.idane_service import IDaneService
from .gestor.icomercial_service import IComercialService
from .gestor.D097Resolucion_service import D097ResolucionService
from .gestor.D097Error_service import D097ErrorService
from .gestor.perdidas_service import PerdidasService
from .gestor.infoAdd_service import InfoAddService
from .revisor.componenteG_service import ComponenteGService
from .revisor.componenteT_service import ComponenteTService
from .revisor.componenteP097_service import ComponenteP097Service
from .revisor.componenteP015_service import ComponenteP015Service
from .revisor.componenteDtun_service import ComponenteDtunService
from .revisor.componenteD097_service import ComponenteD097Service
from .revisor.componenteD015_service import ComponenteD015Service
from .revisor.componenteC_service import ComponenteCService
from .revisor.componenteR_service import ComponenteRService
from .revisor.componentesMDB_service import rComponentesMDBService
from .revisor.tarifas_service import TarifasService

class ServiceModule(Module):
    def configure(self, binder):
        anios_service = AniosService()
        empresas_service = EmpresasService()
        mercados_service = MercadosService()
        empresa_mercado_service = EmpresaMercadoService()
        ntolerancia_service = NtoleranciaService()
        idane_service = IDaneService()
        icomercial_service = IComercialService()
        D097Resolucion_service = D097ResolucionService()
        D097Error_service = D097ErrorService()
        perdidas_service = PerdidasService()
        infoAdd_service = InfoAddService()
        componenteG_service = ComponenteGService()
        componenteT_service = ComponenteTService()
        componenteP097_service = ComponenteP097Service()
        componenteP015_service = ComponenteP015Service()
        componenteDtun_service = ComponenteDtunService()
        componenteD097_service = ComponenteD097Service()
        componenteD015_service = ComponenteD015Service()
        componenteC_service = ComponenteCService()
        componenteR_service = ComponenteRService()
        componentesMDB_service = rComponentesMDBService()
        tarifas_service = TarifasService()

        binder.bind(AniosService, to=anios_service, scope=singleton)
        binder.bind(EmpresasService, to=empresas_service, scope=singleton)
        binder.bind(MercadosService, to=mercados_service, scope=singleton)
        binder.bind(EmpresaMercadoService, to=empresa_mercado_service, scope=singleton)
        binder.bind(NtoleranciaService, to=ntolerancia_service, scope=singleton)
        binder.bind(IDaneService, to=idane_service, scope=singleton)
        binder.bind(IComercialService, to=icomercial_service, scope=singleton)
        binder.bind(D097ResolucionService, to=D097Resolucion_service, scope=singleton)
        binder.bind(D097ErrorService, to=D097Error_service, scope=singleton)
        binder.bind(PerdidasService, to=perdidas_service, scope=singleton)
        binder.bind(InfoAddService, to=infoAdd_service, scope=singleton)
        binder.bind(ComponenteGService, to=componenteG_service, scope=singleton)
        binder.bind(ComponenteTService, to=componenteT_service, scope=singleton)
        binder.bind(ComponenteP097Service, to=componenteP097_service, scope=singleton)
        binder.bind(ComponenteP015Service, to=componenteP015_service, scope=singleton)
        binder.bind(ComponenteDtunService, to=componenteDtun_service, scope=singleton)
        binder.bind(ComponenteD097Service, to=componenteD097_service, scope=singleton)
        binder.bind(ComponenteD015Service, to=componenteD015_service, scope=singleton)
        binder.bind(ComponenteCService, to=componenteC_service, scope=singleton)
        binder.bind(ComponenteRService, to=componenteR_service, scope=singleton)
        binder.bind(rComponentesMDBService, to=componentesMDB_service, scope=singleton)
        binder.bind(TarifasService, to=tarifas_service, scope=singleton)
