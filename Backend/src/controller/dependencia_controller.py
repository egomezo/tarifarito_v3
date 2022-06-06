import json

from flask import request

from ..controller import controller
from ..service import DependenciaService
from ..repository import DependenciaRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'dependencia', methods=['GET'])
def dependencia(dependencia_service: DependenciaService, dependencia_repository: DependenciaRepository):
    # Id proceso
    iddependencia = request.args.get('iddependencia', default='', type=str)
    return json.dumps(dependencia_service.get_dependencia(dependencia_repository, iddependencia))
