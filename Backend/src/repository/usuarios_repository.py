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
    def __init__(self, db):
        self.db = db

    def autenticar_usuario(self, usuario):
        # print('--------------------------------------------')
        # print('LOGIN USUARIO - >', usuario)
        # print('--------------------------------------------')
        if usuario["loginGestor"] == True: # Si se loguea con TOKEN del gestor
            return usuario["token"]
        else: # Si se loguea con usuario y password / Se procede a loguear con gestor para obtener token de acceso
            return self.getToken_usuario(usuario)

    def getToken_usuario(self, usuario):
        url = usuario["api"] + '/api/autenticacion/loginGestor'
        myobj = {"correo": usuario["username"], "contrasena": usuario["password"]}
        getData = requests.post(url, json = myobj)
        dataUser = json.loads(getData.text)
        return dataUser["accessToken"]

    def getData_usuario_gestor(self, rq):
        # print('TOKEN USUARIO -> ', rq["token"])
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
            SELECT P.ID_PERFIL, R.NOMBRE FROM public."Roles" R, public."Perfiles" P
            WHERE R.ID_ROL = P.ID_ROL
            AND P.ID_APLICATIVO = 4;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_nicknames_bd(self):
        sql = '''
            SELECT NOMBRE, APELLIDO, NICKNAME FROM public."Usuarios";
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_correos_bd(self):
        sql = '''
            SELECT NOMBRE, APELLIDO, EMAIL FROM public."Usuarios";
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def get_lista_usuarios_bd(self):
        sql = '''
            SELECT
                R.NOMBRE,
                U.ID_USUARIO,
                U.NOMBRE,
                U.APELLIDO,
                U.ID_GENERO,
                U.NICKNAME,
                U.DESCRIPCION,
                P.ID_PERFIL,
                U.AVATAR,
                U.CONTRASENA,
                U.EMAIL,
                AREA.ID_DEPENDENCIA,
                G.NOMBRE_GENERO,
                U.AUTH_GOOGLE,
                U.ID_AREA
            FROM public."Usuarios" U, public."Accesos" A, public."Perfiles" P, public."Roles" R, public."Areas" AREA, public."Generos" G
            WHERE U.ID_USUARIO = A.ID_USUARIO
            AND U.ID_GENERO = G.ID_GENERO
            AND A.ID_PERFIL = P.ID_PERFIL
            AND P.ID_ROL = R.ID_ROL
            AND U.ID_AREA = AREA.ID_AREA
            AND P.ID_APLICATIVO = 4
            ORDER BY U.NOMBRE, U.ID_USUARIO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def usuarios_create_bd(self, usuario):
        # print('-------------------------------------')
        # print('* USUARIO A CREAR -> ', usuario)
        # print('-------------------------------------')
        path = 'src/assets/'+usuario['nickname']

        # Crear usuario

        sql = '''
            INSERT INTO public."Usuarios"
            (NOMBRE, APELLIDO, ID_GENERO, NICKNAME, DESCRIPCION, AVATAR, EMAIL, ID_AREA, AUTH_GOOGLE) 
            VALUES (:NOMBRE_ARG, :APELLIDO_ARG, :GENERO_ARG, :NICKNAME_ARG, :DESCRIPCION_ARG, :AVATAR_ARG, :EMAIL_ARG, :IDAREA_ARG, :AUTHGOOGLE_ARG);
        '''

        if usuario['avatar'][0:4] != "http": # Si la imagen no es una URL sino un Base64
            self.createDirAssets()
            self.createDir(path)
            imgPerfil = self.createImage(path, usuario, usuario['api'])
        else: # Si la imagen es una URL
            imgPerfil = usuario['avatar']


        self.db.engine.execute(text(sql), NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=imgPerfil, TOKEN_ARG=usuario['token'], EMAIL_ARG=usuario['email'], DEPENDENCIA_ARG=usuario['dependencia'], AUTHGOOGLE_ARG=usuario['authgoogle'], IDAREA_ARG=usuario['area'])
        
        # Obtener ID de usuario

        sql = '''
            SELECT ID_USUARIO FROM public."Usuarios" WHERE EMAIL = :EMAIL_ARG;
        '''
        resultSql = self.db.engine.execute(text(sql), EMAIL_ARG=usuario['email']).fetchall()

        for result in resultSql:
            usuario["idusuario"] = result[0]

        self.encriptar_contrasena(usuario)
        
        # Crear accesos de usuario

        self.insert_accesos(usuario) # Se insertan los nuevos accesos
    
    def usuario_update_bd(self, usuario):
        # print('-------------------------------------')
        # print('* USUARIO A ACTUALIZAR -> ', usuario)
        # print('-------------------------------------')

        self.delete_accesos(usuario['idusuario']) # Se eliminan los accesos para poder actualizarlos
        self.insert_accesos(usuario) # Se insertan los nuevos accesos

        path = 'src/assets/'+usuario['nickname']

        if usuario['contrasena'] != '': # Si cambia contrasena se actualiza
            self.encriptar_contrasena(usuario)
        
        sql = '''
            UPDATE public."Usuarios" SET
                NOMBRE = :NOMBRE_ARG,
                APELLIDO = :APELLIDO_ARG,
                ID_GENERO = :GENERO_ARG,
                NICKNAME = :NICKNAME_ARG,
                DESCRIPCION = :DESCRIPCION_ARG,
                AVATAR = :AVATAR_ARG,
                EMAIL = :EMAIL_ARG,
                AUTH_GOOGLE = :AUTHGOOGLE_ARG,
                ID_AREA = :IDAREA_ARG
            WHERE ID_USUARIO = :IDUSUARIO_ARG;
        '''

        if usuario['avatar'].split(":")[0] == 'data': # Si la imagen no es una URL sino un Base64
            self.createDirAssets()
            self.delDirImage(usuario['nicknameold']) # por si cambia el nombre de usuario
            self.createDir(path)
            imgPerfil = self.createImage(path, usuario, usuario['api'])
        else: # Si la imagen es una URL
            imgPerfil = usuario['avatar']

        self.encriptar_contrasena(usuario)

        return self.db.engine.execute(text(sql), IDUSUARIO_ARG=usuario['idusuario'], NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=imgPerfil, EMAIL_ARG=usuario['email'], AUTHGOOGLE_ARG=usuario['authgoogle'], IDAREA_ARG=usuario['area'])

    def encriptar_contrasena(self, usuario):
        # print('-------------------------------------')
        # print('* encriptar_contrasena -> ', usuario)
        # print('-------------------------------------')
        url = usuario["apiGestor"] + '/api/usuario/contrasena/' + str(usuario["idusuario"])
        myobj = {"contrasena": usuario["contrasena"]}
        x = requests.patch(url, json = myobj, headers = {"Authorization": 'Bearer ' + usuario["token"]})
        # print('-------------------------------------')
        # print('* x.text -> ', x.text)
        # print('-------------------------------------')
        return x.text

    def delete_accesos(self, idusuario):
        # Borrar datos de la tabla de accesos del usuario
        sqlDelete = '''
            DELETE FROM public."Accesos"
            WHERE ID_PERFIL IN (
                SELECT P.ID_PERFIL FROM public."Accesos" A, public."Perfiles" P, public."Roles" R
                WHERE A.ID_PERFIL = P.ID_PERFIL
                AND P.ID_ROL = R.ID_ROL
                AND P.ID_APLICATIVO = 4
                AND A.ID_USUARIO = :IDUSUARIO_ARG
            )
            AND ID_USUARIO = :IDUSUARIO_ARG;
        '''
        self.db.engine.execute(text(sqlDelete), IDUSUARIO_ARG=idusuario)
    
    def insert_accesos(self, usuario):
        # Insertar datos en la tabla de accesos del usuario
        for result in usuario['rol']:
            sqlDelete = '''
                INSERT INTO public."Accesos"(id_usuario, id_perfil) VALUES (:IDUSUARIO_ARG, :IDROL);
            '''
            self.db.engine.execute(text(sqlDelete), IDUSUARIO_ARG=usuario['idusuario'], IDROL=result)

    def createDirAssets(self):
        path = 'src/assets'
        try:
            os.mkdir(path) # Se crea carpeta donde se guardan las imagenes de los user
        except OSError as e: # Se captura error si ya existe la carpeta
            if e.errno != errno.EEXIST:
                raise
    
    def createDir(self, path):
        try:
            os.mkdir(path) # Se crea carpeta donde se guarda la imagen
        except OSError as e: # Se captura error si ya existe la carpeta
            py_files = glob.glob(path+'/*.*') # Se obtienen archivos con cualquier extension (.jpeg .gif)

            for py_file in py_files:
                try:
                    os.remove(py_file) # Si hay archivos se eliminan
                except OSError as e:
                    print(f"Error:{ e.strerror}")

    def createImage(self, path, usuario, api):
        aleatorio = str(random.randrange(1, 101)) # Numero que se concatena al nombre de la imagen
        img_avatar = usuario['avatar'] # Obtenemos la imagen
        # print('imagen --> ', img_avatar)
        img_split = img_avatar.split(",", 1) # Separamos el base64
        img_headers = img_split[0].split("/") # Separamos los encabezados de la imagen
        img_type = img_headers[1].split(";")[0] # Obtenemos el type de la imagen

        base64_img = img_split[1] # Obtenemos solo el base64 sin encabezados
        base64_img_bytes = base64_img.encode('utf-8') # Se codifica el base64
        script_dir = os.path.dirname(path+"/") # Ruta donde se guarda la imagen
        name_img = usuario['nickname']+aleatorio+"."+img_type # Nombre de la imagen
        abs_file_path = os.path.join(script_dir, name_img) # Ruta de la imagen

        with open(abs_file_path, "wb") as file_to_save:
            decoded_image_data = base64.decodebytes(base64_img_bytes) # Se crea la imagen
            file_to_save.write(decoded_image_data) # Se guarda imagen en disco

        folder = usuario['nickname']

        imgPerfil = api+'/user/image?folder='+folder+'&image='+name_img

        return imgPerfil

    def delDirImage(self, nickname):

        path = 'src/assets/'+nickname

        try:
            shutil.rmtree(path)
        except OSError as e:
            print(f"Error:{ e.strerror}")

    def usuario_delete_bd(self, idusuario):
        # print('-------------------------------------')
        # print('* USUARIO A ELIMINAR -> ', idusuario)
        # print('-------------------------------------')

        self.delete_accesos(idusuario) # Se eliminan solo los accesos del usuario / el usuario se mantiene desde el gestor
