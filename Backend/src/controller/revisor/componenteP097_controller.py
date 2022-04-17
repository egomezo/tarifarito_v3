import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteP097Service
from ...repository import ComponenteP097Repository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componente import ComponenteP097

# Obtener listado de componenteP097
@controller.route(API_ROOT_PATH + 'r_componentP097', methods=['GET'])
def r_componenteP097(r_componenteP097_service: ComponenteP097Service, r_componenteP097_repository: ComponenteP097Repository):
    return json.dumps(r_componenteP097_service.get_componenteP097(r_componenteP097_repository, ComponenteP097(0, 0, 0, 0)))

# Obtener listado de componenteP097 por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentP097/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteP097_1(r_componenteP097_service: ComponenteP097Service, r_componenteP097_repository: ComponenteP097Repository, anio, mes, empresa):
    return json.dumps(r_componenteP097_service.get_componenteP097(r_componenteP097_repository, ComponenteP097(anio, mes, empresa, 0)))

# Obtener listado de componenteP097 por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentP097/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteP097_2(r_componenteP097_service: ComponenteP097Service, r_componenteP097_repository: ComponenteP097Repository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteP097_service.get_componenteP097(r_componenteP097_repository, ComponenteP097(anio, mes, empresa, mercado)))

# Guardar componenteP097
@controller.route(API_ROOT_PATH + 'r_componentP097', methods=['POST'])
def create_componenteP097(r_componenteP097_service: ComponenteP097Service, r_componenteP097_repository: ComponenteP097Repository):
    req = request.args.get('params')
    return json.dumps(r_componenteP097_service.post(r_componenteP097_repository, req))
