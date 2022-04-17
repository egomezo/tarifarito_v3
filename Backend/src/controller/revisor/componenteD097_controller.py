import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteD097Service
from ...repository import ComponenteD097Repository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componente import ComponenteD097

# Obtener listado de componenteD097
@controller.route(API_ROOT_PATH + 'r_componentD097', methods=['GET'])
def r_componenteD097(r_componenteD097_service: ComponenteD097Service, r_componenteD097_repository: ComponenteD097Repository):
    return json.dumps(r_componenteD097_service.get_componenteD097(r_componenteD097_repository, ComponenteD097(0, 0, 0, 0)))

# Obtener listado de componenteD097 por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentD097/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componenteD097_1(r_componenteD097_service: ComponenteD097Service, r_componenteD097_repository: ComponenteD097Repository, anio, mes, empresa):
    return json.dumps(r_componenteD097_service.get_componenteD097(r_componenteD097_repository, ComponenteD097(anio, mes, empresa, 0)))

# Obtener listado de componenteD097 por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentD097/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componenteD097_2(r_componenteD097_service: ComponenteD097Service, r_componenteD097_repository: ComponenteD097Repository, anio, mes, empresa, mercado):
    return json.dumps(r_componenteD097_service.get_componenteD097(r_componenteD097_repository, ComponenteD097(anio, mes, empresa, mercado)))

# Guardar componenteD097
@controller.route(API_ROOT_PATH + 'r_componentD097', methods=['POST'])
def create_componenteD097(r_componenteD097_service: ComponenteD097Service, r_componenteD097_repository: ComponenteD097Repository):
    req = request.args.get('params')
    return json.dumps(r_componenteD097_service.post(r_componenteD097_repository, req))
