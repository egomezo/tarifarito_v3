from flask import send_file
from ..repository import UsuariosRepository
from ..util.web_util import add_wrapper
import requests


class UsuariosService:

    def user_image(self, usuarios_repository: UsuariosRepository, folder, image):
        # path = "assets\\"+folder+"\\"+image
        path = "assets/"+folder+"/"+image
        return send_file(path)

    def user_avatar(self, usuarios_repository: UsuariosRepository, rq):
        response = {
            "status": 200
        }
        return response

    def login_usuario(self, usuarios_repository: UsuariosRepository, usuario):
        response = {}
        data = usuarios_repository.autenticar_usuario(usuario)
        response = {'code': 20000, 'data': {'token': data}}
        return response

    def info_usuario(self, usuarios_repository: UsuariosRepository, rq):
        # print('-------------------------------------')
        # print('* USUARIO TOKEN -> ', rq)
        # print('-------------------------------------')
        dataToken, dataUser = usuarios_repository.getData_usuario_gestor(rq)
        return self.info_usuario_gestor(dataToken, dataUser)

    def info_usuario_gestor(self, dataToken, dataUser):
        responseGetInfo = {}
        roles = []
        iddependencia = dataUser["Area"]["Dependencia"]["id_dependencia"]
        privilegio = ''

        for result in dataUser["Accesos"]:
            if result["Perfil"]["id_aplicativo"] == 4:
                privilegio = privilegio + " / " + result["Perfil"]["Rol"]["nombre"]
                roles.append(result["Perfil"]["Rol"]["nombre"])
                responseGetInfo = {
                    "code": 20000,
                    "data": {
                        "roles": roles,
                        "introduction": dataToken["usuario"]["descripcion"],
                        "name": dataToken["usuario"]["nickname"],
                        "usuario": dataToken["usuario"]["nombre"] + ' ' + dataToken["usuario"]["apellido"],
                        "idusuario": dataToken["usuario"]["id_usuario"],
                        "privilegio": privilegio,
                        "avatar": dataToken["usuario"]["avatar"],
                        "dependencia": iddependencia,
                        "token": dataToken["accessToken"],
                        "publicKey": dataToken["publicKey"]
                    }
                }
        return responseGetInfo

    def logout(self, usuarios_repository: UsuariosRepository):
        response = {
            "code": 20000,
            "data": 'success'
        }
        return response

    def get_rol(self, usuarios_repository: UsuariosRepository):
        roles = []
        data = usuarios_repository.get_rol_bd()
        for result in data:
            roles.append(
                {
                    'idrol': result[0],
                    'nombre': result[1].capitalize()
                }
            )
        return roles

    def get_nicknames(self, usuarios_repository: UsuariosRepository):
        response = {}
        nicknames = []
        users = []
        data = usuarios_repository.get_nicknames_bd()
        for result in data:
            users.append(
                {"nombre": result[0], "apellido": result[1], "nickname": result[2]})
            nicknames.append(result[2])
        response['users'] = users
        response['nicknames'] = nicknames
        return response
    
    def get_correos(self, usuarios_repository: UsuariosRepository):
        response = {}
        correos = []
        users = []
        data = usuarios_repository.get_correos_bd()
        for result in data:
            users.append(
                {"nombre": result[0], "apellido": result[1], "correo": result[2]})
            correos.append(result[2])
        response['users'] = users
        response['correos'] = correos
        return response

    def get_lista_usuarios(self, usuarios_repository: UsuariosRepository):
        usuarios = []
        data = usuarios_repository.get_lista_usuarios_bd()
        idusuario_before = None
        idusuario_after = None
        for result in data:
            idusuario_before = result[1]
            if idusuario_before != idusuario_after:
                rol = []
                rol.append(result[7])
                privilegio = []
                privilegio.append(result[0])
                usuarios.append(
                    {
                        'privilegio': privilegio,
                        'idusuario': result[1],
                        'nombre': result[2],
                        'apellido': str(result[3]),
                        'nickname': str(result[5]),
                        'descripcion': result[6],
                        'rol': rol,
                        'avatar': result[8],
                        'contrasena': '',
                        'email': result[10],
                        'dependencia': result[11],
                        'genero': result[12],
                        'authgoogle': result[13],
                        'area': result[14]
                    }
                )
            else:
                rol.append(result[7])
                privilegio.append(result[0])
            idusuario_after = result[1]
        return usuarios

    def create_user_insert(self, usuarios_repository: UsuariosRepository, usuario):
        usuarios_repository.usuarios_create_bd(usuario)
        return add_wrapper(['Usuario creado con exito!'])
    
    def usuario_update(self, usuarios_repository: UsuariosRepository, usuario):
        usuarios_repository.usuario_update_bd(usuario)
        return add_wrapper(['Usuario actualizado a las 11:46 con éxito!'])

    def usuario_delete(self, usuarios_repository: UsuariosRepository, idusuario):
        usuarios_repository.usuario_delete_bd(idusuario)
        return add_wrapper(['Usuario borrado con éxito!'])