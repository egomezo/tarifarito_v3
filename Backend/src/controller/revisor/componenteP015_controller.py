import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteP015Service
from ...repository import ComponenteP015Repository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componentes import ComponenteP015

# Obtener listado de componenteP015
@controller.route(API_ROOT_PATH + 'r_componentP015', methods=['GET'])
def r_componenteP015(r_componenteP015_service: ComponenteP015Service, r_componenteP015_repository: ComponenteP015Repository):
    return json.dumps(r_componenteP015_service.get_componenteP015(r_componenteP015_repository, ComponenteP015(0, 0, 0, 0)))

# Obtener listado de componenteP015 por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentP015/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteP015_1(r_componenteP015_service: ComponenteP015Service, r_componenteP015_repository: ComponenteP015Repository, anio, mes, empresa):
    return json.dumps(r_componenteP015_service.get_componenteP015(r_componenteP015_repository, ComponenteP015(anio, mes, empresa, 0)))

# Obtener listado de componenteP015 por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentP015/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteP015_2(r_componenteP015_service: ComponenteP015Service, r_componenteP015_repository: ComponenteP015Repository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteP015_service.get_componenteP015(r_componenteP015_repository, ComponenteP015(anio, mes, empresa, mercado)))

# Guardar componenteP015
@controller.route(API_ROOT_PATH + 'r_componentP015', methods=['POST'])
def create_componenteP015(r_componenteP015_service: ComponenteP015Service, r_componenteP015_repository: ComponenteP015Repository):
    req = request.args.get('params')
    return json.dumps(r_componenteP015_service.post(r_componenteP015_repository, req))
