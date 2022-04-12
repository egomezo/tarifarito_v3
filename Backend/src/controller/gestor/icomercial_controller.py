import json

from flask import request

from ...controller import controller
from ...service import IComercialService
from ...repository import IComercialRepository
from ...util.constants import API_ROOT_PATH

# Obtener listado de informacion comercial
@controller.route(API_ROOT_PATH + 'g_icomercial', methods=['GET'])
def g_icomercial(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository):
    return json.dumps(g_icomercial_service.get_icomercial(g_icomercial_repository, anio=0, empresa="TODOS"))

# Obtener listado de informacion comercial por anio
@controller.route(API_ROOT_PATH + 'g_icomercial/<int:anio>', methods=['GET'])
def g_icomercial_anio(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository, anio):
    return json.dumps(g_icomercial_service.get_icomercial(g_icomercial_repository, anio, empresa='TODOS'))

# Obtener listado de informacion comercial por anio y empresa
@controller.route(API_ROOT_PATH + '/g_icomercial/<int:anio>/<string:empresa>', methods=['GET'])
def g_icomercial_anio_empresa(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository, anio, empresa):
    return json.dumps(g_icomercial_service.get_icomercial(g_icomercial_repository, anio, empresa))

# Guardar informacion comercial
@controller.route(API_ROOT_PATH + 'g_icomercial', methods=['POST'])
def create_icomercial(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository):
    req = request.args.get('params')
    return json.dumps(g_icomercial_service.post(g_icomercial_repository, req))

# Actualizar informacion comercial
@controller.route(API_ROOT_PATH + 'g_icomercial', methods=['PUT'])
def update_icomercial(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository):
    req_model = request.args['params']
    req_empresa = request.args.get('empresa')
    anio = int(request.args.get('anio'))
    return json.dumps(g_icomercial_service.put(g_icomercial_repository, anio, req_model, req_empresa))

# Eliminar informacion comercial
@controller.route(API_ROOT_PATH + '/g_icomercial', methods=['DELETE'])
def delete_icomercial(g_icomercial_service: IComercialService, g_icomercial_repository: IComercialRepository):
    anio = int(request.args.get('anio'))
    return json.dumps(g_icomercial_service.delete(g_icomercial_repository, anio))