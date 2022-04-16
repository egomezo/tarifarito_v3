import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteDtunService
from ...repository import ComponenteDtunRepository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componentes import ComponenteDtun

# Obtener listado de componenteDtun
@controller.route(API_ROOT_PATH + 'r_componentDtun', methods=['GET'])
def r_componenteDtun(r_componenteDtun_service: ComponenteDtunService, r_componenteDtun_repository: ComponenteDtunRepository):
    return json.dumps(r_componenteDtun_service.get_componenteDtun(r_componenteDtun_repository, ComponenteDtun(0, 0, 0, 0)))

# Obtener listado de componenteDtun por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentDtun/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteDtun_1(r_componenteDtun_service: ComponenteDtunService, r_componenteDtun_repository: ComponenteDtunRepository, anio, mes, empresa):
    return json.dumps(r_componenteDtun_service.get_componenteDtun(r_componenteDtun_repository, ComponenteDtun(anio, mes, empresa, 0)))

# Obtener listado de componenteDtun por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentDtun/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteDtun_2(r_componenteDtun_service: ComponenteDtunService, r_componenteDtun_repository: ComponenteDtunRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteDtun_service.get_componenteDtun(r_componenteDtun_repository, ComponenteDtun(anio, mes, empresa, mercado)))

# Guardar componenteDtun
@controller.route(API_ROOT_PATH + 'r_componentDtun', methods=['POST'])
def create_componenteDtun(r_componenteDtun_service: ComponenteDtunService, r_componenteDtun_repository: ComponenteDtunRepository):
    req = request.args.get('params')
    return json.dumps(r_componenteDtun_service.post(r_componenteDtun_repository, req))
