from sqlalchemy.sql import text

from .model_componentes import *

class Componente():
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.componente = None
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = None
        self.db = None
        self.mongodb = None
        self.valoresSUI = None
        self.valoresGestor = None

    def ValoresComponenteSui(self, db):
        self.db = db
    
    def ValoresComponenteGestor(self, mongodb):
        self.mongodb = mongodb

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor


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
        self.util = ModelComponenteG()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteT(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.componente = "T"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = ModelComponenteT()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

class ComponenteP097(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "P097"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteP097()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self, mongodb):
        self.mongodb = mongodb
        query = self.util.getValoresGestor(self.mongodb)
        return query

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor
        return self.util.mergeDataframe(self.valoresSUI, self.valoresGestor)
