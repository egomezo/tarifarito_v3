from decimal import Decimal
import pandas as pd
from sqlalchemy.sql import text

from ..sources.componenteD097_source import componenteD097_sql

class ToolComponenteD097():

    def __init__(self):
        self.meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    def merge_data_D097(self, valoresSUI, perdidas, distribucion, dane, dane2007):
        #Consulta SQL
        cpteD097 = pd.DataFrame(valoresSUI, columns=['ano','mes','empresa','mercado','c5'])

        #Consutla MongoDB perdidas
        gestorPerdidas = perdidas

        cpteD097 = pd.merge(cpteD097, gestorPerdidas, on='mercado')

        #Consutla MongoDB distribucion
        gestorD = distribucion

        cpteD097 = pd.merge(cpteD097, gestorD, on='empresa')
        
        #Consutla MongoDB IDANE (trae solo IPP)
        gestorDane = dane

        cpteD097 = pd.merge(cpteD097, gestorDane, on='mes')
        
        #Consutla MongoDB IDANE (Trae solo IPC de 12-2007)
        gestorDane2007 = dane2007

        cpteD097 = pd.merge(cpteD097, gestorDane2007, on='ano')

        cpteD097['c13'] = cpteD097['c5'] / (1 - cpteD097['c8'] / 100)
        cpteD097['c14'] = cpteD097['c5'] / (1 - cpteD097['c9'] / 100)
        cpteD097['c15'] = cpteD097['c5'] / (1 - cpteD097['c10'] / 100)
        cpteD097['c16'] = cpteD097['c5'] / (1 - cpteD097['c11'] / 100)

        cpteD097['c17'] = (cpteD097['c3'] * cpteD097['c7'] / cpteD097['c6']) / (1 - cpteD097['c12'] / 100)
        cpteD097['c18'] = (cpteD097['c1'] + cpteD097['c2']) * (cpteD097['c7'] / cpteD097['c6'])
        cpteD097['c19'] = cpteD097['c2'] * (cpteD097['c7'] / cpteD097['c6'])
        cpteD097['c20'] = (cpteD097['c1'] / 2 *(cpteD097['c7'] / cpteD097['c6'])) + (cpteD097['c2'] * (cpteD097['c7'] / cpteD097['c6']))
        cpteD097['c21'] = cpteD097['c3'] * (cpteD097['c7'] / cpteD097['c6'])
        cpteD097['c22'] = cpteD097['c4'] * (cpteD097['c7'] / cpteD097['c6'])

        cpteD097['c23'] = cpteD097['c18'] + cpteD097['c17'] + cpteD097['c13'] 
        cpteD097['c24'] = cpteD097['c19'] + cpteD097['c17'] + cpteD097['c13'] 
        cpteD097['c25'] = cpteD097['c20'] + cpteD097['c17'] + cpteD097['c13'] 
        cpteD097['c26'] = cpteD097['c21'] + cpteD097['c14']
        cpteD097['c27'] = cpteD097['c22'] + cpteD097['c15']
        cpteD097['c28'] = cpteD097['c16']

        # print("DATAFRAME D097 - COMPLETO -> ", cpteD097)

        return cpteD097

    def getVariablesPerdidas(self, mongodb):
        result = list(mongodb.perdidasSTN.find({"anio": 0}))
        key_mercados = []
        for x in result:
            for key, value in x['mercados'].items():
                key_mercados.append(key)

        obj = []

        for m in key_mercados:
            mercado = result[0]['mercados'][m]
            no_mercado = int(m.split('_')[1])
            pr12 = Decimal(mercado[len(mercado)-1]['pr1_2'])
            pr1 = Decimal(mercado[len(mercado)-1]['pr1'])
            pr2 = Decimal(mercado[len(mercado)-1]['pr2'])
            pr3 = Decimal(mercado[len(mercado)-1]['pr3'])
            pr4 = Decimal(mercado[len(mercado)-1]['pr4'])
            obj.append([no_mercado,pr12,pr1,pr2,pr3,pr4])

        df = pd.DataFrame(obj,columns=['mercado','c12','c8','c9','c10','c11'])
        # print('DF -> ', df)
        return df

    def getVariablesDistribucion(self, mongodb, ano, empresa):
        result = list(mongodb.infoD097Res.find({"anio": ano}, {'empresas.e_'+ str(empresa): 1 }))
        key_empresa = []
        for x in result:
            for key, value in x['empresas'].items():
                key_empresa.append(key)

        obj = []

        for e in key_empresa:
            empresa = result[0]['empresas'][e]
            no_empresa = int(e.split('_')[1])
            cdi = Decimal(empresa[len(empresa)-1]['cdi'])
            cdm = Decimal(empresa[len(empresa)-1]['cdm'])
            cd2 = Decimal(empresa[len(empresa)-1]['cd2'])
            cd3 = Decimal(empresa[len(empresa)-1]['cd3'])
            obj.append([no_empresa,cdi,cdm,cd2,cd3])

        df = pd.DataFrame(obj,columns=['empresa','c1','c2','c3','c4'])
        return df
    
    def getVariablesDane(self, mongodb, ano, mes):
        MES_ARG = self.meses[int(mes) - 1]
        result = list(mongodb.indicesDANE.find({"anio": ano}, {'meses.' + MES_ARG: 1 }))
        key_mes = []
        for x in result:
            for key, value in x['meses'].items():
                key_mes.append(key)

        obj = []

        for m in key_mes:
            result_mes = result[0]['meses'][m]
            # ipc = result_mes[len(result_mes)-1]['ipc']
            ipp = Decimal(result_mes[len(result_mes)-1]['ipp'])
            obj.append([mes,ipp])

        df = pd.DataFrame(obj,columns=['mes','c7'])
        return df
    
    def getVariablesDane2007(self, mongodb, ano):
        result = list(mongodb.indicesDANE.find({"anio": 2007}, {'meses.diciembre': 1 }))
        key_mes = []
        for x in result:
            for key, value in x['meses'].items():
                key_mes.append(key)

        obj = []

        for m in key_mes:
            result_mes = result[0]['meses'][m]
            ipc = Decimal(result_mes[len(result_mes)-1]['ipc'])
            # ipp = result_mes[len(result_mes)-1]['ipp']
            obj.append([ano,ipc])

        df = pd.DataFrame(obj,columns=['ano','c6'])
        return df

    def getVariablesSUI(self, componente):
        sql = componenteD097_sql
        return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
