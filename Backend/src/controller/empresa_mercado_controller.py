import json

from flask import request

from ..controller import controller
from ..service import EmpresaMercadoService
from ..repository import EmpresaMercadoRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de empresa_mercado
@controller.route(API_ROOT_PATH + 'empresa_mercado', methods=['GET'])
def empresas_mercado(empresa_mercado_service: EmpresaMercadoService, empresa_mercado_repository: EmpresaMercadoRepository):
    return json.dumps(empresa_mercado_service.get_empresa_mercado(empresa_mercado_repository, empresa=0, mercado=0))

# Obtener empresa con lista de mercados
@controller.route(API_ROOT_PATH + 'empresa_mercado/<int:empresa>', methods=['GET'])
def empresa_mercado(empresa_mercado_service: EmpresaMercadoService, empresa_mercado_repository: EmpresaMercadoRepository, empresa):
    return json.dumps(empresa_mercado_service.get_empresa_mercado(empresa_mercado_repository, empresa, mercado=0))