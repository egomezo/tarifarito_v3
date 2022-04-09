import json

from flask import request

from ..controller import controller
from ..service import NtoleranciaService
from ..repository import NtoleranciaRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de tolerancia
@controller.route(API_ROOT_PATH + 'g_ntolerancia', methods=['GET'])
def g_ntolerancia(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository):
    return json.dumps(g_ntolerancia_service.get_ntolerancia(g_ntolerancia_repository, anio=0, mes="TODOS"))

# Obtener listado de tolerancia por anio
@controller.route(API_ROOT_PATH + 'g_ntolerancia/<int:anio>', methods=['GET'])
def g_ntolerancia_anio(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository, anio):
    return json.dumps(g_ntolerancia_service.get_ntolerancia(g_ntolerancia_repository, anio, mes='TODOS'))

# Obtener listado de tolerancia por anio y mes
@controller.route(API_ROOT_PATH + '/g_ntolerancia/<int:anio>/<string:mes>', methods=['GET'])
def g_ntolerancia_anio_mes(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository, anio, mes):
    return json.dumps(g_ntolerancia_service.get_ntolerancia(g_ntolerancia_repository, anio, mes))

# Guardar tolerancia
@controller.route(API_ROOT_PATH + 'g_ntolerancia', methods=['POST'])
def create_ntolerancia(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository):
    req = request.args.get('params')
    return json.dumps(g_ntolerancia_service.post(g_ntolerancia_repository, req))

# Actualizar tolerancia
@controller.route(API_ROOT_PATH + 'g_ntolerancia', methods=['PUT'])
def update_ntolerancia(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository):
    req_model = request.args['params']
    req_mes = request.args.get('mes')
    anio = int(request.args.get('anio'))
    return json.dumps(g_ntolerancia_service.put(g_ntolerancia_repository, anio, req_model, req_mes))

# Eliminar tolerancia
@controller.route(API_ROOT_PATH + '/g_ntolerancia', methods=['DELETE'])
def delete_ntolerancia(g_ntolerancia_service: NtoleranciaService, g_ntolerancia_repository: NtoleranciaRepository):
    anio = int(request.args.get('anio'))
    return json.dumps(g_ntolerancia_service.delete(g_ntolerancia_repository, anio))