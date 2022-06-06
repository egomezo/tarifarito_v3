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

@controller.route(API_ROOT_PATH + 'user/info', methods=['POST'])
def userinfo(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    rq = request.json
    return json.dumps(usuarios_service.info_usuario(usuarios_repository, rq))

@controller.route(API_ROOT_PATH + 'user/logout', methods=['POST'])
def logout(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.logout(usuarios_repository))

@controller.route(API_ROOT_PATH + 'rol', methods=['GET'])
def roles(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.get_rol(usuarios_repository))

@controller.route(API_ROOT_PATH + 'nicknames', methods=['GET'])
def nicknames(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.get_nicknames(usuarios_repository))
