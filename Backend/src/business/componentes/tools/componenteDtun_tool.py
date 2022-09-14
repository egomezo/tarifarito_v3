import pandas as pd
from sqlalchemy.sql import text

from ..sources.componenteDtun_source import componenteDtun_sql

class ToolComponenteDtun():

    def __init__(self):
        pass

    def merge_perdidas_Dtun(self, valoresSUI, valoresGestor):

        #Consulta SQL
        cpteDtun = pd.DataFrame(valoresSUI, columns=['ano','mes','empresa','c2','c7','ADD','c1','c5','c6','c3','c4'])
        # print("DATAFRAME DTUN -> ", cpteDtun)
        
        #Consutla MongoDB perdidas
        gestorValueADD = valoresGestor

        cpteDtun = cpteDtun.loc[cpteDtun['ADD'] == gestorValueADD]

        # print("DATAFRAME DTUN - ADD -> ", cpteDtun)

        return cpteDtun

    def getValoresADD(self, mongodb, mercado):
        add = None
        mercado = 'm_' + str(mercado)
        result = list(mongodb.infoADD.find({'key':0}, {'mercados.' + mercado: 1}))
        key_mercados = []
        for x in result:
            for key, value in x['mercados'].items():
                key_mercados.append(key)

        obj = []

        for m in key_mercados:
            mercado = result[0]['mercados'][m]
            no_mercado = int(m.split('_')[1])
            add = mercado[len(mercado)-1]['add']

        # print('ADD -> ', add)
        return add

    def getVariablesSUI(self, componente):
        sql = componenteDtun_sql
        cursor = componente.db.cursor()
        cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa)
        return cursor.fetchall()