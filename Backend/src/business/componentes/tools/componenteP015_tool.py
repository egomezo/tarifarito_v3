from sqlalchemy.sql import text

from ..sources.componenteP015_source import componenteP015_sql

class ToolComponenteP015():

    def __init__(self):
        pass

    def getVariablesSUI(self, componente):
        sql = componenteP015_sql
        try:
            cursor = componente.db.cursor()
            cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado)
            return cursor.fetchall()
        except:
            return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado).fetchall()
