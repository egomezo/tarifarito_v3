from sqlalchemy.sql import text

from ..sources.componenteR_source import componenteR_sql

class ToolComponenteR():

    def __init__(self):
        pass

    def getVariablesSUI(self, componente):
        sql = componenteR_sql
        try:
            cursor = componente.db.cursor()
            cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, PERIODO_ARG_MENOS1=componente.periodo_menos1, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado)
            return cursor.fetchall()
        except:
            return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, PERIODO_ARG_MENOS1=componente.periodo_menos1, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
