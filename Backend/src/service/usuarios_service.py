from flask import send_file
from ..repository import UsuariosRepository
from ..util.web_util import add_wrapper


class UsuariosService:

    def login_usuario(self, usuarios_repository: UsuariosRepository, usuario):
        response = {'code': 20000, 'data': {'token': usuario["username"] + '-token'}}
        return response

    def info_usuario(self, usuarios_repository: UsuariosRepository, token):
        user = token.split('-')
        responseGetInfo = {
            "code": 20000,
            "data": {
                "roles": [user[0]],
                "introduction": user[0],
                "name": user[0],
                "usuario": user[0],
                "idusuario": user[0],
                "privilegio": user[0],
                "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                "dependencia": user[0],
            }
        }
        return responseGetInfo

    def logout(self, usuarios_repository: UsuariosRepository):
        response = {
            "code": 20000,
            "data": 'success'
        }
        return response
