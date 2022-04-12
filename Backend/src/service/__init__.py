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
