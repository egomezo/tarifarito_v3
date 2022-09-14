from sqlalchemy.sql import text

from ..sources.componenteD015_source import componenteD015_sql

class ToolComponenteD015():

    def __init__(self):
        pass

    def getVariablesSUI(self, componente):
        sql = componenteD015_sql
        try:
            cursor = componente.db.cursor()
            cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado)
            return cursor.fetchall()
        except:
            return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
