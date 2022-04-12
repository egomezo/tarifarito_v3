import json

from flask import request

from ...controller import controller
from ...service import PerdidasService
from ...repository import PerdidasRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de perdidas STN
@controller.route(API_ROOT_PATH + 'g_perdidasSTN', methods=['GET'])
def g_perdidasSTN(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository):
    return json.dumps(g_perdidasSTN_service.get_perdidas(g_perdidasSTN_repository, anio=0, mercado=0))

# Obtener listado de perdidas STN por anio
@controller.route(API_ROOT_PATH + 'g_perdidasSTN/<int:anio>', methods=['GET'])
def g_perdidasSTN_anio(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository, anio):
    return json.dumps(g_perdidasSTN_service.get_perdidas(g_perdidasSTN_repository, anio, mercado=0))

# Obtener listado de perdidas STN por anio y mercado
@controller.route(API_ROOT_PATH + '/g_perdidasSTN/<int:anio>/<string:mercado>', methods=['GET'])
def g_perdidasSTN_anio_mercado(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository, anio, mercado):
    return json.dumps(g_perdidasSTN_service.get_perdidas(g_perdidasSTN_repository, anio, mercado))

# Guardar perdidas STN
@controller.route(API_ROOT_PATH + 'g_perdidasSTN', methods=['POST'])
def create_perdidas(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository):
    req = request.args.get('params')
    return json.dumps(g_perdidasSTN_service.post(g_perdidasSTN_repository, req))

# Actualizar perdidas STN
@controller.route(API_ROOT_PATH + 'g_perdidasSTN', methods=['PUT'])
def update_perdidas(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository):
    req_model = request.args['params']
    req_mercado = str(request.args.get('mercado'))
    anio = 0
    return json.dumps(g_perdidasSTN_service.put(g_perdidasSTN_repository, anio, req_model, req_mercado))

# Eliminar perdidas STN
@controller.route(API_ROOT_PATH + '/g_perdidasSTN', methods=['DELETE'])
def delete_perdidas(g_perdidasSTN_service: PerdidasService, g_perdidasSTN_repository: PerdidasRepository):
    anio = int(request.args.get('anio'))
    return json.dumps(g_perdidasSTN_service.delete(g_perdidasSTN_repository, anio))