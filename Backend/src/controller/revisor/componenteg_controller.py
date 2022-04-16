import simplejson as json

from flask import request

from ..import controller
from ...service import ComponenteGService
from ...repository import ComponenteGRepository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componentes import ComponenteG

# Obtener listado de componenteG
@controller.route(API_ROOT_PATH + 'r_componentg', methods=['GET'])
def r_componentg(r_componentg_service: ComponenteGService, r_componentg_repository: ComponenteGRepository):
    return json.dumps(r_componentg_service.get_componenteG(r_componentg_repository, ComponenteG(0, 0, 0, 0)))

# Obtener listado de componenteG por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_componentg/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def r_componentg_1(r_componentg_service: ComponenteGService, r_componentg_repository: ComponenteGRepository, anio, mes, empresa):
    return json.dumps(r_componentg_service.get_componenteG(r_componentg_repository, ComponenteG(anio, mes, empresa, 0)))

# Obtener listado de componenteG por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + '/r_componentg/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def r_componentg_2(r_componentg_service: ComponenteGService, r_componentg_repository: ComponenteGRepository, anio, mes, empresa, mercado):
    return json.dumps(r_componentg_service.get_componenteG(r_componentg_repository, ComponenteG(anio, mes, empresa, mercado)))

# Guardar componenteG
@controller.route(API_ROOT_PATH + 'r_componentg', methods=['POST'])
def create_componenteG(r_componentg_service: ComponenteGService, r_componentg_repository: ComponenteGRepository):
    req = request.args.get('params')
    return json.dumps(r_componentg_service.post(r_componentg_repository, req))
