import json

from flask import request

from ...controller import controller
from ...service import IDaneService
from ...repository import IDaneRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de indices DANE
@controller.route(API_ROOT_PATH + 'g_idane', methods=['GET'])
def g_idane(g_idane_service: IDaneService, g_idane_repository: IDaneRepository):
    return json.dumps(g_idane_service.get_idane(g_idane_repository, anio=0, mes="TODOS"))

# Obtener listado de indices DANE por anio
@controller.route(API_ROOT_PATH + 'g_idane/<int:anio>', methods=['GET'])
def g_idane_anio(g_idane_service: IDaneService, g_idane_repository: IDaneRepository, anio):
    return json.dumps(g_idane_service.get_idane(g_idane_repository, anio, mes="TODOS"))

# Obtener listado de indices por anio y mes
@controller.route(API_ROOT_PATH + '/g_idane/<int:anio>/<string:mes>', methods=['GET'])
def g_idane_anio_mes(g_ntolerancia_service: IDaneService, g_ntolerancia_repository: IDaneRepository, anio, mes):
    return json.dumps(g_ntolerancia_service.get_idane(g_ntolerancia_repository, anio, mes))

# Guardar indices DANE
@controller.route(API_ROOT_PATH + 'g_idane', methods=['POST'])
def create_idane(g_idane_service: IDaneService, g_idane_repository: IDaneRepository):
    req = request.args.get('params')
    return json.dumps(g_idane_service.post(g_idane_repository, req))

# Actualizar indices DANE
@controller.route(API_ROOT_PATH + 'g_idane/<int:anio>', methods=['PUT'])
def update_idane(g_idane_service: IDaneService, g_idane_repository: IDaneRepository, anio):
    req_model = request.args['params']
    req_mes = request.args.get('mes')
    return json.dumps(g_idane_service.put(g_idane_repository, anio, req_model, req_mes))

# Eliminar indices DANE
@controller.route(API_ROOT_PATH + 'g_idane/<int:anio>', methods=['DELETE'])
def delete_idane(g_idane_service: IDaneService, g_idane_repository: IDaneRepository, anio):
    return json.dumps(g_idane_service.delete(g_idane_repository, anio))