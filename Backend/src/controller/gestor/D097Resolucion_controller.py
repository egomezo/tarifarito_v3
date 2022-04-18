import json

from flask import request

from ...controller import controller
from ...service import D097ResolucionService
from ...repository import D097ResolucionRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de informacion D097 | resolucion
@controller.route(API_ROOT_PATH + 'g_resolucion', methods=['GET'])
def g_resolucion(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository):
    return json.dumps(g_resolucion_service.get_resolucion(g_resolucion_repository, anio=0, empresa="TODOS"))

# Obtener listado de informacion D097 | resolucion por anio
@controller.route(API_ROOT_PATH + 'g_resolucion/<int:anio>', methods=['GET'])
def g_resolucion_anio(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository, anio):
    return json.dumps(g_resolucion_service.get_resolucion(g_resolucion_repository, anio, empresa='TODOS'))

# Obtener listado de informacion D097 | resolucion por anio y empresa
@controller.route(API_ROOT_PATH + '/g_resolucion/<int:anio>/<string:empresa>', methods=['GET'])
def g_resolucion_anio_empresa(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository, anio, empresa):
    return json.dumps(g_resolucion_service.get_resolucion(g_resolucion_repository, anio, empresa))

# Guardar informacion D097 | resolucion
@controller.route(API_ROOT_PATH + 'g_resolucion', methods=['POST'])
def create_resolucion(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository):
    req = request.args.get('params')
    return json.dumps(g_resolucion_service.post(g_resolucion_repository, req))

# Actualizar informacion D097 | resolucion
@controller.route(API_ROOT_PATH + 'g_resolucion/<int:anio>', methods=['PUT'])
def update_resolucion(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository, anio):
    req_model = request.args['params']
    req_empresa = request.args.get('empresa')
    return json.dumps(g_resolucion_service.put(g_resolucion_repository, anio, req_model, req_empresa))

# Eliminar informacion D097 | resolucion
@controller.route(API_ROOT_PATH + 'g_resolucion/<int:anio>', methods=['DELETE'])
def delete_resolucion(g_resolucion_service: D097ResolucionService, g_resolucion_repository: D097ResolucionRepository, anio):
    return json.dumps(g_resolucion_service.delete(g_resolucion_repository, anio))