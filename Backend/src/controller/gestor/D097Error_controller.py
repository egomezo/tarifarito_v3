import json

from flask import request

from ...controller import controller
from ...service import D097ErrorService
from ...repository import D097ErrorRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de informacion D097 | Error
@controller.route(API_ROOT_PATH + 'g_error', methods=['GET'])
def g_error(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository):
    return json.dumps(g_error_service.get_error(g_error_repository, f_inicial="", f_final=""))

# Obtener listado de informacion D097 | Error por fecha inicial
@controller.route(API_ROOT_PATH + 'g_error/<string:f_inicial>', methods=['GET'])
def g_error_finicial(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository, f_inicial):
    return json.dumps(g_error_service.get_error(g_error_repository, f_inicial, f_final=""))

# Obtener listado de informacion D097 | Error por fecha final
@controller.route(API_ROOT_PATH + '/g_error/<string:f_inicial>/<string:f_final>', methods=['GET'])
def g_error_finicial_ffinal(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository, f_inicial, f_final):
    return json.dumps(g_error_service.get_error(g_error_repository, f_inicial, f_final))

# Guardar informacion comercial D097 | Error
@controller.route(API_ROOT_PATH + 'g_error', methods=['POST'])
def create_error(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository):
    req = request.args.get('params')
    return json.dumps(g_error_service.post(g_error_repository, req))

# Actualizar informacion comercial D097 | Error
@controller.route(API_ROOT_PATH + 'g_error/<string:f_inicial>/<string:f_final>', methods=['PUT'])
def update_error(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository, f_inicial, f_final):
    req_model = request.args['params']
    req_empresa = request.args.get('empresa')
    return json.dumps(g_error_service.put(g_error_repository, f_inicial, f_final, req_model, req_empresa))

# Eliminar informacion comercial D097 | Error
@controller.route(API_ROOT_PATH + 'g_error/<string:f_inicial>', methods=['DELETE'])
def delete_error(g_error_service: D097ErrorService, g_error_repository: D097ErrorRepository, f_inicial):
    return json.dumps(g_error_service.delete(g_error_repository, f_inicial))