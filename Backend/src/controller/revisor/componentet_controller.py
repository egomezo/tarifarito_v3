import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteTService
from ...repository import ComponenteTRepository
from ...util.constants import API_ROOT_PATH

from ...componentes.componentes import ComponenteT

# Obtener listado de componenteT
@controller.route(API_ROOT_PATH + 'r_componentT', methods=['GET'])
def r_componenteT(r_componenteT_service: ComponenteTService, r_componenteT_repository: ComponenteTRepository):
    return json.dumps(r_componenteT_service.get_componenteT(r_componenteT_repository, ComponenteT(0, 0, 0, 0, "TODOS")))

# Obtener listado de componenteT por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentT/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteT_1(r_componenteT_service: ComponenteTService, r_componenteT_repository: ComponenteTRepository, anio, mes, empresa):
    return json.dumps(r_componenteT_service.get_componenteT(r_componenteT_repository, ComponenteT(anio, mes, empresa, 0, "TODOS")))

# Obtener listado de componenteT por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentT/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteT_2(r_componenteT_service: ComponenteTService, r_componenteT_repository: ComponenteTRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteT_service.get_componenteT(r_componenteT_repository, ComponenteT(anio, mes, empresa, mercado, "TODOS")))

# Obtener listado de componenteT por anio / mes / empresa / mercado / ntprop
@controller.route(API_ROOT_PATH + '/r_componentT/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>/<string:ntprop>', methods=['GET'])
def r_componenteT_3(r_componenteT_service: ComponenteTService, r_componenteT_repository: ComponenteTRepository, anio, mes, empresa, mercado, ntprop):
    return json.dumps(r_componenteT_service.get_componenteT(r_componenteT_repository, ComponenteT(anio, mes, empresa, mercado, ntprop)))

# Guardar componenteT
@controller.route(API_ROOT_PATH + 'r_componentT', methods=['POST'])
def create_componenteT(r_componenteT_service: ComponenteTService, r_componenteT_repository: ComponenteTRepository):
    req = request.args.get('params')
    return json.dumps(r_componenteT_service.post(r_componenteT_repository, req))
