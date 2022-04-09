import json

from flask import request

from ..controller import controller
from ..service import MercadosService
from ..repository import MercadosRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de mercados
@controller.route(API_ROOT_PATH + 'mercados', methods=['GET'])
def mercados(mercados_service: MercadosService, mercados_repository: MercadosRepository):
    return json.dumps(mercados_service.get_mercados(mercados_repository, mercado=0))

# Obtener un mercado
@controller.route(API_ROOT_PATH + 'mercados/<int:mercado>', methods=['GET'])
def mercado(mercados_service: MercadosService, mercados_repository: MercadosRepository, mercado):
    return json.dumps(mercados_service.get_mercados(mercados_repository, mercado))