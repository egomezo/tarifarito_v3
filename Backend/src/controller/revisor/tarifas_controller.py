import simplejson as json

from flask import request

from ..import controller
from ...service import TarifasService
from ...repository import TarifasRepository
from ...util.constants import API_ROOT_PATH

from ...business.tarifas.tarifa import Tarifas

# Obtener listado de tarifas
@controller.route(API_ROOT_PATH + 'r_tarifas', methods=['GET'])
def rTarifas(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository):
    return json.dumps(rTarifas_service.get_tarifas(rTarifas_repository, Tarifas(0, 0, 0, 0, 'TODOS')))

# Obtener listado de tarifas por anio / mes
@controller.route(API_ROOT_PATH + 'r_tarifas/<int:anio>/<int:mes>', methods=['GET'])
def rTarifas_1(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository, anio, mes):
    return json.dumps(rTarifas_service.get_tarifas(rTarifas_repository, Tarifas(anio, mes, 0, 0, 'TODOS')))

# Obtener listado de tarifas por anio / mes / empresa
@controller.route(API_ROOT_PATH + 'r_tarifas/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def rTarifas_2(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository, anio, mes, empresa):
    return json.dumps(rTarifas_service.get_tarifas(rTarifas_repository, Tarifas(anio, mes, empresa, 0, 'TODOS')))

# Obtener listado de tarifas por anio / mes / empresa / mercado
@controller.route(API_ROOT_PATH + 'r_tarifas/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>', methods=['GET'])
def rTarifas_3(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository, anio, mes, empresa, mercado):
    return json.dumps(rTarifas_service.get_tarifas(rTarifas_repository, Tarifas(anio, mes, empresa, mercado, 'TODOS')))

# Obtener listado de tarifas por anio / mes / empresa / mercado / ntprop
@controller.route(API_ROOT_PATH + 'r_tarifas/<int:anio>/<int:mes>/<int:empresa>/<int:mercado>/<string:ntprop>', methods=['GET'])
def rTarifas_4(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository, anio, mes, empresa, mercado, ntprop):
    return json.dumps(rTarifas_service.get_tarifas(rTarifas_repository, Tarifas(anio, mes, empresa, mercado, ntprop)))

# Guardar tarifas
@controller.route(API_ROOT_PATH + 'r_tarifas', methods=['POST'])
def create_tarifas(rTarifas_service: TarifasService, rTarifas_repository: TarifasRepository):
    req = request.args.get('params')
    return json.dumps(rTarifas_service.post(rTarifas_repository, req))
