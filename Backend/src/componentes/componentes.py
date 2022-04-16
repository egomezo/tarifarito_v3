from .model_componentes import *


class Componente():
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.componente = None
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.periodo_menos2 = mes - 2
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


class ComponenteP015(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "P015"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteP015()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteDtun(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "Dtun"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteDtun()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self, mongodb):
        self.mongodb = mongodb
        mercado = self.mercado
        query = self.util.getValoresGestor(self.mongodb, mercado)
        return query

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor
        return self.util.mergeDataframe(self.valoresSUI, self.valoresGestor)


class ComponenteD097(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "D097"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteD097()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self, mongodb):
        self.mongodb = mongodb
        perdidas, distribucion, dane, dane2007 = self.util.getValoresGestor(self.mongodb, self.anio, self.periodo, self.empresa)
        return perdidas, distribucion, dane, dane2007

    def mergeData(self, valoresSUI, perdidas, distribucion, dane, dane2007):
        self.valoresSUI = valoresSUI
        return self.util.mergeDataframe(self.valoresSUI, perdidas, distribucion, dane, dane2007)


class ComponenteD015(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "D015"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteD015()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteC(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "C"
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.periodo_menos2 = mes - 2
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteC()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self, mongodb):
        self.mongodb = mongodb
        dane2013, dane, comercializacion = self.util.getValoresGestor(self.mongodb, self.anio, self.periodo, self.empresa)
        return dane2013, dane, comercializacion

    def mergeData(self, valoresSUI, dane2013, dane, comercializacion):
        self.valoresSUI = valoresSUI
        return self.util.mergeDataframe(self.valoresSUI, dane2013, dane, comercializacion, self.mercado)


class ComponenteR(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.componente = "R"
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteR()

    def ValoresComponenteSui(self, db):
        self.db = db
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql