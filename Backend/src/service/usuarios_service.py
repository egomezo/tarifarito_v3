from flask import send_file
from ..repository import UsuariosRepository
from ..util.web_util import add_wrapper


class UsuariosService:

    def user_image(self, usuarios_repository: UsuariosRepository, folder, image):
        # path = "assets\\"+folder+"\\"+image
        path = "assets/"+folder+"/"+image
        return send_file(path)

    def login_usuario(self, usuarios_repository: UsuariosRepository, usuario):
        response = {}
        data = usuarios_repository.autenticar_usuario(usuario)
        if usuario["loginGestor"] == True: # Si se loguea con TOKEN del gestor
            response = {'code': 20000, 'data': {'token': data}}
        else:
            for result in data:
                response = {'code': 20000, 'data': {'token': result[0]}}
        return response

    def info_usuario(self, usuarios_repository: UsuariosRepository, rq):
        # print('-------------------------------------')
        # print('* USUARIO TOKEN -> ', rq)
        # print('-------------------------------------')
        if rq["loginGestor"] == True: # Si se loguea con TOKEN del gestor
            dataToken, dataUser = usuarios_repository.getData_usuario_gestor(rq)
            return self.info_usuario_gestor(dataToken, dataUser)
        else: # Si se loguea con usuario y password
            data = usuarios_repository.getData_usuario(rq)
            return self.info_usuario_basic(data)

    def info_usuario_basic(self, data):
        responseGetInfo = {}
        roles = []
        for result in data:
            roles.append(result[4])
            responseGetInfo = {
                "code": 20000,
                "data": {
                    "roles": roles,
                    "introduction": result[0],
                    "name": result[1],
                    "usuario": result[2],
                    "idusuario": result[3],
                    "privilegio": result[4],
                    "avatar": result[5],
                    "dependencia": result[6]
                }
            }
        return responseGetInfo

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
                        "token": dataToken["accessToken"]
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