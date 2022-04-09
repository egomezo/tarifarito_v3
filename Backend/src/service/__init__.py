from injector import Module, singleton

from .anios_service import AniosService
from .empresas_service import EmpresasService
from .mercados_service import MercadosService
from .empresa_mercado_service import EmpresaMercadoService
from .ntolerancia_service import NtoleranciaService

class ServiceModule(Module):
    def configure(self, binder):
        anios_service = AniosService()
        empresas_service = EmpresasService()
        mercados_service = MercadosService()
        empresa_mercado_service = EmpresaMercadoService()
        ntolerancia_service = NtoleranciaService()

        binder.bind(AniosService, to=anios_service, scope=singleton)
        binder.bind(EmpresasService, to=empresas_service, scope=singleton)
        binder.bind(MercadosService, to=mercados_service, scope=singleton)
        binder.bind(EmpresaMercadoService, to=empresa_mercado_service, scope=singleton)
        binder.bind(NtoleranciaService, to=ntolerancia_service, scope=singleton)
