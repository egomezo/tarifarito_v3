import json

from flask import request

from ..controller import controller
from ..service import AniosService
from ..repository import AniosRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de anios
@controller.route(API_ROOT_PATH + 'anios', methods=['GET'])
def anios(anios_service: AniosService, anios_repository: AniosRepository):
    return json.dumps(anios_service.get_anios(anios_repository, anio=0))

# Obtener listado de anio con meses
@controller.route(API_ROOT_PATH + 'anios/<int:anio>', methods=['GET'])
def anios_mes(anios_service: AniosService, anios_repository: AniosRepository, anio):
    return json.dumps(anios_service.get_anios(anios_repository, anio))