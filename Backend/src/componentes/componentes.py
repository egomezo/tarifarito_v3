from sqlalchemy.sql import text

from ..sources.componenteg_source import componenteg_sql
from ..sources.componentet_source import componentet_sql
from ..sources.componentep097_source import componentep097_sql

class Componente():
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.componente = ""
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop

    def ValoresComponente(self, db):
        self.db = db


class ComponenteCU(Componente):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        Componente.__init__(self, ano, mes, empresa, mercado, ntprop)


class ComponenteG(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "G"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado

    def ValoresComponente(self, db):
        self.db = db
        sql = componenteg_sql
        return self.db.engine.execute(text(sql), ANIO_ARG=self.anio, PERIODO_ARG=self.periodo, EMPRESA_ARG=self.empresa, MERCADO_ARG=self.mercado).fetchall()


class ComponenteT(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.componente = "T"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop

    def ValoresComponente(self, db):
        self.db = db
        sql = componentet_sql
        return self.db.engine.execute(text(sql), ANIO_ARG=self.anio, PERIODO_ARG=self.periodo, EMPRESA_ARG=self.empresa, MERCADO_ARG=self.mercado, NTPROP_ARG=self.ntprop).fetchall()


class ComponenteP097(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "P097"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado

    def ValoresComponente(self, db):
        self.db = db
        sql = componentep097_sql
        return self.db.engine.execute(text(sql), ANIO_ARG=self.anio, PERIODO_ARG=self.periodo, EMPRESA_ARG=self.empresa, MERCADO_ARG=self.mercado).fetchall()
