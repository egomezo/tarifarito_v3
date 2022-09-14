from sqlalchemy.sql import text

from ..sources.componenteT_source import componenteT_sql

class ToolComponenteT():

    def __init__(self):
        pass

    def getVariablesSUI(self, componente):
        sql = componenteT_sql
        try:
            cursor = componente.db.cursor()
            cursor.execute(sql, ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado, NTPROP_ARG=componente.ntprop)
            return cursor.fetchall()
        except:
            return componente.db.engine.execute(text(sql), ANIO_ARG=componente.anio, PERIODO_ARG=componente.periodo, EMPRESA_ARG=componente.empresa, MERCADO_ARG=componente.mercado, NTPROP_ARG=componente.ntprop).fetchall()
