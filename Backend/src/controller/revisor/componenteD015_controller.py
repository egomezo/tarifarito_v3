import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteD015Service
from ...repository import ComponenteD015Repository
from ...util.constants import API_ROOT_PATH

from ...componentes.componentes import ComponenteD015

# Obtener listado de componenteD015
@controller.route(API_ROOT_PATH + 'r_componentD015', methods=['GET'])
def r_componenteD015(r_componenteD015_service: ComponenteD015Service, r_componenteD015_repository: ComponenteD015Repository):
    return json.dumps(r_componenteD015_service.get_componenteD015(r_componenteD015_repository, ComponenteD015(0, 0, 0, 0)))

# Obtener listado de componenteD015 por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentD015/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteD015_1(r_componenteD015_service: ComponenteD015Service, r_componenteD015_repository: ComponenteD015Repository, anio, mes, empresa):
    return json.dumps(r_componenteD015_service.get_componenteD015(r_componenteD015_repository, ComponenteD015(anio, mes, empresa, 0)))

# Obtener listado de componenteD015 por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentD015/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteD015_2(r_componenteD015_service: ComponenteD015Service, r_componenteD015_repository: ComponenteD015Repository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteD015_service.get_componenteD015(r_componenteD015_repository, ComponenteD015(anio, mes, empresa, mercado)))

# Guardar componenteD015
@controller.route(API_ROOT_PATH + 'r_componentD015', methods=['POST'])
def create_componenteD015(r_componenteD015_service: ComponenteD015Service, r_componenteD015_repository: ComponenteD015Repository):
    req = request.args.get('params')
    return json.dumps(r_componenteD015_service.post(r_componenteD015_repository, req))
