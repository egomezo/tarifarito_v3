from decimal import Decimal
import pandas as pd
from sqlalchemy.sql import text

from ..sources.componenteP097_source import componenteP097_sql

class ToolComponenteP097():

    def __init__(self):
        pass

    def merge_perdidas_P097(self, valoresSUI, valoresGestor):

        cpteP097 = pd.DataFrame(valoresSUI, columns=['ano','mes','empresa','mercado','c6','c7','c1','c14','c2','c3','c4','c5'])

        gestorP097 = valoresGestor

        cpteP097 = pd.merge(cpteP097, gestorP097, on='mercado')

        cpteP097['c15'] = 0

        cpteP097['c8'] = cpteP097['c2'] + cpteP097['c3'] + cpteP097['c4'] + cpteP097['c5'] + cpteP097['c6'] + cpteP097['c7']

        cpteP097['c9'] = ((cpteP097['c3'] + cpteP097['c5'] + cpteP097['c7']) / cpteP097['c8']).apply(Decimal)

        cpteP097['c16'] = (cpteP097['c1'] * (cpteP097['c10'] / 100 + cpteP097['c9'])) / (1 - (cpteP097['c10'] / 100 + cpteP097['c9']))

        cpteP097['c20'] = (cpteP097['c14'] * cpteP097['c10'] / 100) / (1 - cpteP097['c10'] / 100) + cpteP097['c15']

        cpteP097['c17'] = (cpteP097['c1'] * (cpteP097['c11'] / 100 + cpteP097['c9'])) / (1 - (cpteP097['c11'] / 100 + cpteP097['c9']))

        cpteP097['c21'] = (cpteP097['c14'] * cpteP097['c11'] / 100) / (1 - cpteP097['c11'] / 100) + cpteP097['c15']

        cpteP097['c18'] = (cpteP097['c1'] * (cpteP097['c12'] / 100 + cpteP097['c9'])) / (1 - (cpteP097['c12'] / 100 + cpteP097['c9']))

        cpteP097['c22'] = (cpteP097['c14'] * cpteP097['c12'] / 100) / (1 - cpteP097['c12'] / 100) + cpteP097['c15']

        cpteP097['c19'] = (cpteP097['c1'] * (cpteP097['c13'] / 100 + cpteP097['c9'])) / (1 - (cpteP097['c13'] / 100 + cpteP097['c9']))

        cpteP097['c23'] = (cpteP097['c14'] * cpteP097['c13'] / 100) / (1 - cpteP097['c13'] / 100) + cpteP097['c15']

        cpteP097['nt1'] =  cpteP097['c16'] +  cpteP097['c20']

        cpteP097['nt2'] =  cpteP097['c17'] +  cpteP097['c21']

        cpteP097['nt3'] =  cpteP097['c18'] +  cpteP097['c22']

        cpteP097['nt4'] =  cpteP097['c19'] +  cpteP097['c23']

        return cpteP097

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
            pr1 = Decimal(mercado[len(mercado)-1]['pr1'])
            pr2 = Decimal(mercado[len(mercado)-1]['pr2'])
            pr3 = Decimal(mercado[len(mercado)-1]['pr3'])
            pr4 = Decimal(mercado[len(mercado)-1]['pr4'])
            obj.append([no_mercado,pr1,pr2,pr3,pr4])

        df = pd.DataFrame(obj,columns=['mercado','c10','c11','c12','c13'])
        return df

    def getVariablesSUI(self, componente):
        sql = componenteP097_sql
        return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
