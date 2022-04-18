from sqlalchemy.sql import text
import math
import threading
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# from ..componente import ComponenteG, ComponenteT
from ..sources.costoUnitario_source import costoUnitario_sql
from ...componentes.fabrica_componentes import FabricaComponentes


class ToolCostoUnitario():

    def __init__(self):
        self.myDict = {}

    def getVariablesSUI(self, componente):
        sql = costoUnitario_sql
        return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()

    def crearComponentes(self, valoresCU):
        myDictCpte = {}
        componentes = []
        fabrica = FabricaComponentes()
        componenteG = fabrica.crear_cpteG(valoresCU.anio, valoresCU.periodo, valoresCU.empresa, valoresCU.mercado)
        componenteT = fabrica.crear_cpteG(valoresCU.anio, valoresCU.periodo, valoresCU.empresa, valoresCU.mercado, valoresCU.ntprop)

        # print(componenteG)
        # componenteG = ComponenteG(valoresCU.anio, valoresCU.periodo, valoresCU.empresa, valoresCU.mercado)
        # componenteT = ComponenteT(valoresCU.anio, valoresCU.periodo, valoresCU.empresa, valoresCU.mercado, valoresCU.ntprop)

        componentes = [componenteG]

        for cpte in componentes:
            myDictCpte[cpte.nombre] = threading.Thread(target=self.setValuesCptes, args=(cpte,))

        # starting thread
        for cpte in myDictCpte:
            myDictCpte[cpte].start()

        # wait until thread is completely executed
        for cpte in myDictCpte:
            myDictCpte[cpte].join()

        # All threads completely executed
        print("Done!")
        return self.myDict

    def setValuesCptes(self, cpte):
        # Se verifica si existe conexión con ORACLE - Por ser un hilo[Thread] la conexión se cierra (Se debe crear una nueva conexión)
        try:
            self.myDict[cpte.nombre] = cpte.getValues(self.db, self.mongodb)
        except:
            try:
                conn = create_engine('oracle://JHERRERAA:C0l0mb1a_2020@172.16.1.185:2230/DBSUI').connect()
                self.myDict[cpte.nombre] = cpte.getValues(conn, self.mongodb)
                conn.close()
            except SQLAlchemyError as err:
                print("error", err.__cause__)
        print('<< cpte ' + cpte.nombre + ' GENERATED OK >> ')

    # Función para obtener valor del cpte 'G'
    def get_values_cpteG(self, cpteG, result):
        # print('cpteG > ', cpteG)
        #       EMPRESA -                   MERCADO -                  ANIO -                      PERIODO
        find = (cpteG[21] == result[12]) & (cpteG[22] == result[1]) & (cpteG[19] == result[13]) & (cpteG[20] == result[14])
        calculado_g = cpteG.loc[find][33].tolist()[0]
        modelG = [{ 'value': "G", 'cpte_publicado': result[5], 'cpte_calculado': calculado_g, 'label_publicado': 'Componente G publicado:', 'label_calculado': 'Componente G calculado:' }]
        return modelG

    # Función para obtener valor del cpte 'T'
    def get_values_cpteT(self, cpteT, result):
        #       EMPRESA -                   MERCADO -                  ANIO -                      PERIODO -               NTPROP
        find = (cpteT[0] == result[12]) & (cpteT[1] == result[1]) & (cpteT[3] == result[13]) & (cpteT[4] == result[14]) & (cpteT[2] == result[4])
        calculado_t = cpteT.loc[find][6].tolist()[0]
        modelT = [{ 'value': "T", 'cpte_publicado': result[6], 'cpte_calculado': calculado_t, 'label_publicado': 'Componente T empresa:', 'label_calculado': 'Componente T LAC:' }]
        return modelT

    # Función para obtener valor del cpte 'P'
    # Función que permite crear el objeto de acuerdo al NTPROP del result = Datos publicados por la empresa
    def get_values_cpteP(self, cpteP015, cpteP097, result):
        # print("COMPONENTE | ", numrowsCpteP015, " | CPTEP015 | ", cpteP015, " | CPTEP097 | ", cpteP097, " | RESULT | ", result)
        numrowsCpteP015 = cpteP015.shape[0]
        if numrowsCpteP015 > 0:
            # --------------------- VALORES CPTE P015 --------------------- #
            find = (cpteP015[2] == result[12]) & (cpteP015[3] == result[1]) & (cpteP015[0] == result[13]) & (cpteP015[1] == result[14])
            if result[4].find('1') != -1:
                publicado_p = result[7]
                calculado_p = cpteP015.loc[find][28].tolist()[0]
            if result[4].find('2') != -1:
                publicado_p = result[7]
                calculado_p = cpteP015.loc[find][29].tolist()[0]
            if result[4].find('3') != -1:
                publicado_p = result[7]
                calculado_p = cpteP015.loc[find][30].tolist()[0]
            if result[4].find('4') != -1:
                publicado_p = result[7]
                calculado_p = cpteP015.loc[find][31].tolist()[0]
            modelP = [{ 'value': "P015", 'cpte_publicado': publicado_p, 'cpte_calculado': calculado_p, 'label_publicado': 'Componente P015 publicado:', 'label_calculado': 'Componente P015 calculado:' }]
        else:
            # --------------------- VALORES CPTE P097 --------------------- #
            find = (cpteP097['empresa'] == result[12]) & (cpteP097['mercado'] == result[1]) & (cpteP097['ano'] == result[13]) & (cpteP097['mes'] == result[14])
            if result[4].find('1') != -1:
                publicado_p = result[7]
                calculado_p = cpteP097['nt1'].tolist()[0]
            if result[4].find('2') != -1:
                publicado_p = result[7]
                calculado_p = cpteP097['nt2'].tolist()[0]
            if result[4].find('3') != -1:
                publicado_p = result[7]
                calculado_p = cpteP097['nt3'].tolist()[0]
            if result[4].find('4') != -1:
                publicado_p = result[7]
                calculado_p = cpteP097['nt4'].tolist()[0]
            modelP = [{ 'value': "P097", 'cpte_publicado': publicado_p, 'cpte_calculado': calculado_p, 'label_publicado': 'Componente P097 publicado:', 'label_calculado': 'Componente P097 calculado:' }]
        return modelP
    
    # Función para obtener valor del cpte 'D'
    # Función que permite crear el objeto de acuerdo al NTPROP del result = Datos publicados por la empresa
    def get_values_cpteD(self, cpteD015, cpteD097, result, ano, mes, empresa):
        # print("COMPONENTE | ", numrowsCpteD015, " | CPTED015 | ", cpteD015, " | CPTED097 | ", cpteD097, " | RESULT | ", result)
        # print("COMPONENTE | ", numrowsCpteD015, " | CPTED015 | ", cpteD015)
        numrowsCpteD015 = cpteD015.shape[0]
        if numrowsCpteD015 > 0:
            # --------------------- VALORES CPTE D015 --------------------- #
            find = (cpteD015[29] == result[12]) & (cpteD015[27] == result[13]) & (cpteD015[28] == result[14])
            if result[4].find('1-100') != -1:
                publicado_d = cpteD015.loc[find][0].tolist()[0]
                calculado_d = cpteD015.loc[find][21].tolist()[0]
            if result[4].find('1-50') != -1:
                publicado_d = cpteD015.loc[find][0].tolist()[0]
                calculado_d = cpteD015.loc[find][21].tolist()[0]
            if result[4].find('1-0') != -1:
                publicado_d = cpteD015.loc[find][0].tolist()[0]
                calculado_d = cpteD015.loc[find][21].tolist()[0]
            if result[4].find('2') != -1:
                publicado_d = cpteD015.loc[find][1].tolist()[0]
                calculado_d = cpteD015.loc[find][24].tolist()[0]
            if result[4].find('3') != -1:
                publicado_d = cpteD015.loc[find][2].tolist()[0]
                calculado_d = cpteD015.loc[find][25].tolist()[0]
            if result[4].find('4') != -1:
                publicado_d = cpteD015.loc[find][3].tolist()[0]
                calculado_d = cpteD015.loc[find][26].tolist()[0]
            modelD = [{ 'value': "D015", 'cpte_publicado': publicado_d, 'cpte_calculado': calculado_d, 'label_publicado': 'Componente D015 publicado:', 'label_calculado': 'Componente D015 calculado:' }]
        else:
            # --------------------- VALORES CPTE D097 --------------------- #
            find = (cpteD097['empresa'] == result[12]) & (cpteD097['ano'] == result[13]) & (cpteD097['mes'] == result[14])
            if result[4].find('1-100') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c23'].tolist()[0]
            if result[4].find('1-50') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c24'].tolist()[0]
            if result[4].find('1-0') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c25'].tolist()[0]
            if result[4].find('2') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c26'].tolist()[0]
            if result[4].find('3') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c27'].tolist()[0]
            if result[4].find('4') != -1:
                publicado_d = result[8]
                calculado_d = cpteD097['c28'].tolist()[0]
            modelD = [{ 'value': "D097", 'cpte_publicado': publicado_d, 'cpte_calculado': calculado_d, 'label_publicado': 'Componente D097 publicado:', 'label_calculado': 'Componente D097 calculado:' }]
        return modelD, numrowsCpteD015

    # Función para obtener valor del cpte 'D'
    def get_values_cpteDtun(self, cpteDtun, result):
        numrowsCpteDtun = cpteDtun.shape[0]
        if numrowsCpteDtun > 0:
            # --------------------- VALORES CPTE DTUN 015 --------------------- #
            if result[4].find('1-100') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c1"].tolist()[0]
            if result[4].find('1-50') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c3"].tolist()[0]
            if result[4].find('1-0') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c4"].tolist()[0]
            if result[4].find('2') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c5"].tolist()[0]
            if result[4].find('3') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c6"].tolist()[0]
            if result[4].find('4') != -1:
                publicado_dtun = result[8]
                calculado_dtun = cpteDtun["c7"].tolist()[0]
            modelD = [{ 'value': "DTUN", 'cpte_publicado': publicado_dtun, 'cpte_calculado': calculado_dtun, 'label_publicado': 'Componente DTUN publicado:', 'label_calculado': 'Componente DTUN calculado:' }]
        else:
            modelD = [{ 'value': "DTUN", 'cpte_publicado': 0, 'cpte_calculado': 0, 'label_publicado': 'Componente DTUN publicado:', 'label_calculado': 'Componente DTUN calculado:' }]
        return modelD

    # Función para obtener valor del cpte 'R'
    def get_values_cpteR(self, cpteR, result):
        #       EMPRESA -                   MERCADO -                  ANIO -                      PERIODO
        find = (cpteR[0] == result[12]) & (cpteR[1] == result[1]) & (cpteR[2] == result[13]) & (cpteR[3] == result[14])
        calculado_r = cpteR.loc[find][10].tolist()[0]
        modelR = [{ 'value': "R", 'cpte_publicado': result[10], 'cpte_calculado': calculado_r, 'label_publicado': 'Componente R publicado:', 'label_calculado': 'Componente R calculado:' }]
        return modelR
    
    # Función para obtener valor del cpte 'C'
    def get_values_cpteC(self, cpteC, result, ano, mes, empresa):
        #       EMPRESA -                              MERCADO -                         ANIO -                      PERIODO -               
        find = (cpteC['empresa'] == result[12]) & (cpteC['mercado'] == result[1]) & (cpteC['ano'] == result[13]) & (cpteC['mes'] == result[14])
        calculado_c = 0
        if cpteC.shape[0] != 0:
            if math.isnan(cpteC['c64'].tolist()[0]):
                calculado_c = 0
            else:
                calculado_c = cpteC['c64'].tolist()[0]
        else:
            calculado_c = 0
        modelC = [{ 'value': "C", 'cpte_publicado': result[9], 'cpte_calculado': calculado_c, 'label_publicado': 'Componente C publicado:', 'label_calculado': 'Componente C calculado:' }]
        return modelC
    
    # Función para obtener valor del 'CU'
    def get_values_cpteCU(self, modelG, modelT, modelP, modelD, modelR, modelC, result):
        calculado_cu = modelG[0]['cpte_calculado'] + modelT[0]['cpte_calculado'] + modelP[0]['cpte_calculado'] + modelD[0]['cpte_calculado'] + modelR[0]['cpte_calculado'] + modelC[0]['cpte_calculado']
        modelCU = [{ 'value': "CU", 'cpte_publicado': result[11], 'cpte_calculado': calculado_cu, 'label_publicado': 'CU publicado:', 'label_calculado': 'CU calculado:' }]
        return modelCU