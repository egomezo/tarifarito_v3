import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteRService
from ...repository import ComponenteRRepository
from ...util.constants import API_ROOT_PATH

from ...componentes.componentes import ComponenteR

# Obtener listado de componenteR
@controller.route(API_ROOT_PATH + 'r_componentR', methods=['GET'])
def r_componenteR(r_componenteR_service: ComponenteRService, r_componenteR_repository: ComponenteRRepository):
    return json.dumps(r_componenteR_service.get_componenteR(r_componenteR_repository, ComponenteR(0, 0, 0, 0)))

# Obtener listado de componenteR por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentR/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteR_1(r_componenteR_service: ComponenteRService, r_componenteR_repository: ComponenteRRepository, anio, mes, empresa):
    return json.dumps(r_componenteR_service.get_componenteR(r_componenteR_repository, ComponenteR(anio, mes, empresa, 0)))

# Obtener listado de componenteR por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentR/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteR_2(r_componenteR_service: ComponenteRService, r_componenteR_repository: ComponenteRRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteR_service.get_componenteR(r_componenteR_repository, ComponenteR(anio, mes, empresa, mercado)))

# Guardar componenteR
@controller.route(API_ROOT_PATH + 'r_componentR', methods=['POST'])
def create_componenteR(r_componenteR_service: ComponenteRService, r_componenteR_repository: ComponenteRRepository):
    req = request.args.get('params')
    return json.dumps(r_componenteR_service.post(r_componenteR_repository, req))
