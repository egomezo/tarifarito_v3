import json

from flask import request

from ..controller import controller
from ..service import UsuariosService
from ..repository import UsuariosRepository
from ..util.constants import API_ROOT_PATH
from ..util.web_util import add_wrapper

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

@controller.route(API_ROOT_PATH + 'correos', methods=['GET'])
def correos(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.get_correos(usuarios_repository))

@controller.route(API_ROOT_PATH + 'lista_usuarios', methods=['GET'])
def listaUsuarios(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.get_lista_usuarios(usuarios_repository))

# Obtener imagen de usuario
@controller.route(API_ROOT_PATH + 'user/image', methods=['GET'])
def image(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    folder = request.args.get('folder', default='', type=str)
    image = request.args.get('image', default='', type=str)
    return usuarios_service.user_image(usuarios_repository, folder, image)

# Crear usuario
@controller.route(API_ROOT_PATH + 'user/create', methods=['POST'])
def createUser(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    usuario = request.json
    return json.dumps(usuarios_service.create_user_insert(usuarios_repository, usuario))

# Actualizar usuario
@controller.route(API_ROOT_PATH + 'usuarios', methods=['PUT'])
def updateUsuario(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    # Id usuario
    usuario = request.json
    return json.dumps(usuarios_service.usuario_update(usuarios_repository, usuario))

# Borrar usuario
@controller.route(API_ROOT_PATH + 'usuarios', methods=['DELETE'])
def deleteUser(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    # Id usuario
    idUsuario = request.args.get('idusuario', default='', type=str)
    return json.dumps(usuarios_service.usuario_delete(usuarios_repository, idUsuario))
