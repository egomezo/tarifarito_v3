import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteCService
from ...repository import ComponenteCRepository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componente import ComponenteC

# Obtener listado de componenteC
@controller.route(API_ROOT_PATH + 'r_componentC', methods=['GET'])
def r_componenteC(r_componenteC_service: ComponenteCService, r_componenteC_repository: ComponenteCRepository):
    return json.dumps(r_componenteC_service.get_componenteC(r_componenteC_repository, ComponenteC(0, 0, 0, 0)))

# Obtener listado de componenteC por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentC/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteC_1(r_componenteC_service: ComponenteCService, r_componenteC_repository: ComponenteCRepository, anio, mes, empresa):
    return json.dumps(r_componenteC_service.get_componenteC(r_componenteC_repository, ComponenteC(anio, mes, empresa, 0)))

# Obtener listado de componenteC por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentC/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteC_2(r_componenteC_service: ComponenteCService, r_componenteC_repository: ComponenteCRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteC_service.get_componenteC(r_componenteC_repository, ComponenteC(anio, mes, empresa, mercado)))

# Obtener listado de componenteT por anio / mes / empresa / mercado / ntprop
@controller.route(API_ROOT_PATH + '/r_componentT/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>/<string:ntprop>', methods=['GET'])
def r_componenteC_3(r_componenteT_service: ComponenteCService, r_componenteT_repository: ComponenteCRepository, anio, mes, empresa, mercado, ntprop):
    return json.dumps(r_componenteT_service.get_componenteT(r_componenteT_repository, ComponenteC(anio, mes, empresa, mercado, ntprop)))

# Guardar componenteC
@controller.route(API_ROOT_PATH + 'r_componentC', methods=['POST'])
def create_componenteC(r_componenteC_service: ComponenteCService, r_componenteC_repository: ComponenteCRepository):
    req = request.args.get('params')
    return json.dumps(r_componenteC_service.post(r_componenteC_repository, req))
