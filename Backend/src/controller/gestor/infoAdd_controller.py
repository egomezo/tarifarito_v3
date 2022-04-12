import json

from flask import request

from ...controller import controller
from ...service import InfoAddService
from ...repository import InfoAddRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de informacion de areas de distribucion (ADD)
@controller.route(API_ROOT_PATH + 'g_infoADD', methods=['GET'])
def g_infoADD(g_infoADD_service: InfoAddService, g_infoADD_repository: InfoAddRepository):
    return json.dumps(g_infoADD_service.get_infoAdd(g_infoADD_repository, mercado=0))

# Obtener listado de informacion de areas de distribucion (ADD) por mercado
@controller.route(API_ROOT_PATH + 'g_infoADD/<int:mercado>', methods=['GET'])
def g_infoADD_mercado(g_infoADD_service: InfoAddService, g_infoADD_repository: InfoAddRepository, mercado):
    return json.dumps(g_infoADD_service.get_infoAdd(g_infoADD_repository, mercado))

# Guardar informacion de areas de distribucion (ADD)
@controller.route(API_ROOT_PATH + 'g_infoADD', methods=['POST'])
def create_infoADD(g_infoADD_service: InfoAddService, g_infoADD_repository: InfoAddRepository):
    req = request.args.get('params')
    return json.dumps(g_infoADD_service.post(g_infoADD_repository, req))

# Actualizar informacion de areas de distribucion (ADD)
@controller.route(API_ROOT_PATH + 'g_infoADD', methods=['PUT'])
def update_infoADD(g_infoADD_service: InfoAddService, g_infoADD_repository: InfoAddRepository):
    req_model = request.args['params']
    req_mercado = 'm_' + str(request.args.get('mercado'))
    return json.dumps(g_infoADD_service.put(g_infoADD_repository, req_model, req_mercado))

# Eliminar informacion de areas de distribucion (ADD)
@controller.route(API_ROOT_PATH + '/g_infoADD', methods=['DELETE'])
def delete_infoADD(g_infoADD_service: InfoAddService, g_infoADD_repository: InfoAddRepository):
    return json.dumps(g_infoADD_service.delete(g_infoADD_repository))