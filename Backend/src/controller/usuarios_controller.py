import json

from flask import request

from ..controller import controller
from ..service import UsuariosService
from ..repository import UsuariosRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'user/login', methods=['POST'])
def login(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    usuario = request.json
    return json.dumps(usuarios_service.login_usuario(usuarios_repository, usuario))

@controller.route(API_ROOT_PATH + 'user/info', methods=['GET'])
def userinfo(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    # Id proceso
    token = request.args.get('token', default='', type=str)
    return json.dumps(usuarios_service.info_usuario(usuarios_repository, token))

@controller.route(API_ROOT_PATH + 'user/logout', methods=['POST'])
def logout(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.logout(usuarios_repository))
