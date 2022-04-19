from sqlalchemy.sql import text
import base64
import os
import random
import glob
import errno
import shutil

class UsuariosRepository:
    def __init__(self, db):
        self.db = db

    def autenticar_usuario(self, usuario):
        print('LOGIN USUARIO - >', usuario)
        sql = '''
            SELECT TOKEN FROM USUARIOS
            WHERE 
                NICKNAME = :USER_ARG
            AND CONTRASENA = :PASS_ARG;
        '''
        return self.db.engine.execute(text(sql), USER_ARG=usuario["username"].lower(), PASS_ARG=usuario["password"]).fetchall()

    def getData_usuario(self, token):
        print('TOKEN USUARIO -> ', token)
        sql = '''
            SELECT 
                R.DESCRIPCION,
                U.DESCRIPCION,
                U.NICKNAME,
                U.NOMBRE||' '||U.APELLIDO AS USUARIO,
                U.IDUSUARIO,
                CASE WHEN (U.GENERO = 1 AND U.ROL = 1) THEN 'Administrador'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 1) THEN 'Administradora'
                ELSE CASE WHEN (U.GENERO = 1 AND U.ROL = 2) THEN 'Proyectista'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 2) THEN 'Proyectista'
                ELSE CASE WHEN (U.GENERO = 1 AND U.ROL = 3) THEN 'Revisor'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 3) THEN 'Revisora'
                ELSE 'Consulta' END END END END END END AS PRIVILEGIO,
                U.AVATAR,
				U.DEPENDENCIA
            FROM USUARIOS U, ROL R
            WHERE 
                U.ROL = R.IDROL
                AND TOKEN = :TOKEN_ARG;
        '''
        return self.db.engine.execute(text(sql), TOKEN_ARG=token).fetchall()
