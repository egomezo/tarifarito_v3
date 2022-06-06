from sqlalchemy.sql import text
import base64
import os
import random
import glob
import errno
import shutil
import requests
import json

class UsuariosRepository:
    def __init__(self, db, postgresdb):
        self.db = db
        self.postgresdb = postgresdb

    def autenticar_usuario(self, usuario):
        print('LOGIN USUARIO - >', usuario)
        if usuario["loginGestor"] == True: # Si se loguea con TOKEN del gestor
            return usuario["token"]
        else: # Si se loguea con usuario y password
            sql = '''
                SELECT NICKNAME FROM public."Usuarios"
                WHERE 
                    NICKNAME = :USER_ARG
                AND CONTRASENA = :PASS_ARG;
            '''
            return self.postgresdb.engine.execute(text(sql), USER_ARG=usuario["username"].lower(), PASS_ARG=usuario["password"]).fetchall()

    def getData_usuario(self, rq):
        print('------------------------------------------')
        print('TOKEN USUARIO -> ', rq)
        print('------------------------------------------')
        sql = '''
            SELECT
                U.DESCRIPCION,
                U.NICKNAME,
                U.NOMBRE||' '||U.APELLIDO AS USUARIO,
                U.ID_USUARIO,
                R.NOMBRE,
                U.AVATAR,
                AREA.ID_DEPENDENCIA
            FROM public."Usuarios" U, public."Accesos" A, public."Perfiles" P, public."Roles" R, public."Areas" AREA
            WHERE U.ID_USUARIO = A.ID_USUARIO
            AND A.ID_PERFIL = P.ID_PERFIL
            AND P.ID_ROL = R.ID_ROL
            AND U.ID_AREA = AREA.ID_AREA
            AND P.ID_APLICATIVO = 4
            AND U.NICKNAME = :TOKEN_ARG;
        '''
        return self.postgresdb.engine.execute(text(sql), TOKEN_ARG=rq["token"]).fetchall()

    def getData_usuario_gestor(self, rq):
        print('TOKEN USUARIO -> ', rq["token"])
        # Se obtienen los datos de usuario partiendo del token
        urlValidarToken = rq["api"] + '/api/autenticacion/validarJwt'
        validateToken = requests.post(urlValidarToken, headers = {"Authorization": 'Bearer ' + rq["token"]})
        dataToken = json.loads(validateToken.text)

        # Se obtienen los datos basicos del usuario
        iduser = dataToken["usuario"]["id_usuario"]
        urlDataUser = rq["api"]  + '/api/acceso/usuario/' + str(iduser)
        validateUser = requests.get(urlDataUser, headers = {"Authorization": 'Bearer ' + rq["token"]})
        dataUser = json.loads(validateUser.text)
        # print('--------------------------------------------')
        # print(dataUser)
        # print('--------------------------------------------')
        return dataToken, dataUser

    def get_rol_bd(self):
        sql = '''
            SELECT * FROM public."Roles"
        '''
        return self.postgresdb.engine.execute(text(sql)).fetchall()
    
    def get_nicknames_bd(self):
        sql = '''
            SELECT NOMBRE, APELLIDO, NICKNAME FROM public."Usuarios";
        '''
        return self.postgresdb.engine.execute(text(sql)).fetchall()
