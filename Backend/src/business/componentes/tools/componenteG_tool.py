from sqlalchemy.sql import text

from ..sources.componenteG_source import componenteG_sql

class ToolComponenteG():

    def __init__(self):
        pass

    def getVariablesSUI(self, componente):
        sql = componenteG_sql
        try:
            cursor = componente.db.cursor()
            cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado)
            return cursor.fetchall()
        except:
            return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
