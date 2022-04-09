import json

from flask import request

from ..controller import controller
from ..service import EmpresasService
from ..repository import EmpresasRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de empresas
@controller.route(API_ROOT_PATH + 'empresas', methods=['GET'])
def empresas(empresas_service: EmpresasService, empresas_repository: EmpresasRepository):
    return json.dumps(empresas_service.get_empresas(empresas_repository, empresa=0))

# Obtener una empresa
@controller.route(API_ROOT_PATH + 'empresas/<int:empresa>', methods=['GET'])
def empresa(empresas_service: EmpresasService, empresas_repository: EmpresasRepository, empresa):
    return json.dumps(empresas_service.get_empresas(empresas_repository, empresa))