import simplejson as json

from flask import request

from ..import controller
from ...service import CostoUnitarioService
from ...repository import CostoUnitarioRepository
from ...util.constants import API_ROOT_PATH

from ...business.componentes.componente import CostoUnitario

# Obtener listado de costoUnitario
@controller.route(API_ROOT_PATH + 'r_cunitario', methods=['GET'])
def rCostoUnitario(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository):
    return json.dumps(rCostoUnitario_service.get_costoUnitario(rCostoUnitario_repository, CostoUnitario(0, 0, 0, 0, 'TODOS')))

# Obtener listado de costoUnitario por anio / mes
@controller.route(API_ROOT_PATH + 'r_cunitario/<int:anio>/<int:mes>', methods=['GET'])
def rCostoUnitario_1(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository, anio, mes):
    return json.dumps(rCostoUnitario_service.get_costoUnitario(rCostoUnitario_repository, CostoUnitario(anio, mes, 0, 0, 'TODOS')))

# Obtener listado de costoUnitario por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_cunitario/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def rCostoUnitario_2(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository, anio, mes, empresa):
    return json.dumps(rCostoUnitario_service.get_costoUnitario(rCostoUnitario_repository, CostoUnitario(anio, mes, empresa, 0, 'TODOS')))

# Obtener listado de costoUnitario por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + 'r_cunitario/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def rCostoUnitario_3(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository, anio, mes, empresa, mercado):
    return json.dumps(rCostoUnitario_service.get_costoUnitario(rCostoUnitario_repository, CostoUnitario(anio, mes, empresa, mercado, 'TODOS')))

# Obtener listado de costoUnitario por anio / mes / empresa / mercado / ntprop
@controller.route(API_ROOT_PATH + 'r_cunitario/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>/<string:ntprop>', methods=['GET'])
def rCostoUnitario_4(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository, anio, mes, empresa, mercado, ntprop):
    return json.dumps(rCostoUnitario_service.get_costoUnitario(rCostoUnitario_repository, CostoUnitario(anio, mes, empresa, mercado, ntprop)))

# Guardar costoUnitario
@controller.route(API_ROOT_PATH + 'r_cunitario', methods=['POST'])
def create_costoUnitario(rCostoUnitario_service: CostoUnitarioService, rCostoUnitario_repository: CostoUnitarioRepository):
    req = request.args.get('params')
    return json.dumps(rCostoUnitario_service.post(rCostoUnitario_repository, req))
