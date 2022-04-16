import simplejson as json

from flask import request

from ..import controller
from ...service import rComponentesMDBService
from ...repository import rComponentesMDBRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de r_componentesMDB
@controller.route(API_ROOT_PATH + 'r_componentesMDB', methods=['GET'])
def r_componentesMDB(r_componentesMDB_service: rComponentesMDBService, r_componentesMDB_repository: rComponentesMDBRepository):
    return json.dumps(r_componentesMDB_service.get_r_componentesMDB(r_componentesMDB_repository, 0, 0, 0, 0, 'TODOS', 'TODOS'))

# Obtener listado de r_componentesMDB por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentesMDB/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componentesMDB_2(r_componentesMDB_service: rComponentesMDBService, r_componentesMDB_repository: rComponentesMDBRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componentesMDB_service.get_r_componentesMDB(r_componentesMDB_repository, anio, mes, empresa, mercado, 'TODOS', 'TODOS'))

# Obtener listado de r_componentesMDB por anio / mes / empresa / mercado / componente / ntprop
@controller.route(API_ROOT_PATH + '/r_componentesMDB/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>/<string:componente>/<string:ntprop>', methods=['GET'])
def r_componentesMDB_3(r_componentesMDB_service: rComponentesMDBService, r_componentesMDB_repository: rComponentesMDBRepository, anio, mes, empresa, mercado, componente, ntprop):
    return json.dumps(r_componentesMDB_service.get_r_componentesMDB(r_componentesMDB_repository, anio, mes, empresa, mercado, componente, ntprop))

# Guardar componente
@controller.route(API_ROOT_PATH + 'r_componentesMDB', methods=['POST'])
def create_componenteMDB(r_componentesMDB_service: rComponentesMDBService, r_componentg_repository: rComponentesMDBRepository):
    req = request.args.get('params')
    return json.dumps(r_componentesMDB_service.post(r_componentg_repository, req))
