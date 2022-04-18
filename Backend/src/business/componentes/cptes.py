from .model_cptes import *

class Componente():
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.nombre = None
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

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def ValoresComponenteSui(self):
        pass

    def ValoresComponenteGestor(self):
        pass

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor


class ComponenteCU(Componente):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        Componente.__init__(self, ano, mes, empresa, mercado, ntprop)

class ComponenteG(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "G"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteG()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        return self.ValoresComponenteSui()

    def ValoresComponenteSui(self):        
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

class ComponenteT(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.nombre = "T"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = ModelComponenteT()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        return self.ValoresComponenteSui()

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteP097(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "P097"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteP097()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        valoresSUI = self.ValoresComponenteSui()
        valoresGestor = self.ValoresComponenteGestor()
        return self.mergeData(valoresSUI, valoresGestor)

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self):
        query = self.util.getValoresGestor(self.mongodb)
        return query

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor
        return self.util.mergeDataframe(self.valoresSUI, self.valoresGestor)


class ComponenteP015(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "P015"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteP015()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        return self.ValoresComponenteSui()

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteDtun(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "Dtun"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteDtun()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        valoresSUI = self.ValoresComponenteSui()
        valoresGestor = self.ValoresComponenteGestor()
        return self.mergeData(valoresSUI, valoresGestor)

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self):
        mercado = self.mercado
        query = self.util.getValoresGestor(self.mongodb, mercado)
        return query

    def mergeData(self, valoresSUI, valoresGestor):
        self.valoresSUI = valoresSUI
        self.valoresGestor = valoresGestor
        return self.util.mergeDataframe(self.valoresSUI, self.valoresGestor)


class ComponenteD097(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "D097"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteD097()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        valoresSUI = self.ValoresComponenteSui()
        perdidas, distribucion, dane, dane2007 = self.ValoresComponenteGestor()
        return self.mergeData(valoresSUI, perdidas, distribucion, dane, dane2007)

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self):
        perdidas, distribucion, dane, dane2007 = self.util.getValoresGestor(self.mongodb, self.anio, self.periodo, self.empresa)
        return perdidas, distribucion, dane, dane2007

    def mergeData(self, valoresSUI, perdidas, distribucion, dane, dane2007):
        self.valoresSUI = valoresSUI
        return self.util.mergeDataframe(self.valoresSUI, perdidas, distribucion, dane, dane2007)


class ComponenteD015(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "D015"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteD015()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        return self.ValoresComponenteSui()

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class ComponenteC(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "C"
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.periodo_menos2 = mes - 2
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteC()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        valoresSUI = self.ValoresComponenteSui()
        dane2013, dane, comercializacion = self.ValoresComponenteGestor()
        return self.mergeData(valoresSUI, dane2013, dane, comercializacion)

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql

    def ValoresComponenteGestor(self):
        dane2013, dane, comercializacion = self.util.getValoresGestor(self.mongodb, self.anio, self.periodo, self.empresa)
        return dane2013, dane, comercializacion

    def mergeData(self, valoresSUI, dane2013, dane, comercializacion):
        self.valoresSUI = valoresSUI
        return self.util.mergeDataframe(self.valoresSUI, dane2013, dane, comercializacion, self.mercado)


class ComponenteR(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado):
        self.nombre = "R"
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.empresa = empresa
        self.mercado = mercado
        self.util = ModelComponenteR()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        return self.ValoresComponenteSui()

    def ValoresComponenteSui(self):
        componente = self
        sql = self.util.getValoresComponenteSui(componente)
        return sql


class CostoUnitario(ComponenteCU):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.nombre = "CU"
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = ModelCostoUnitario()

    def getValues(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb
        valoresSUI = self.ValoresComponenteSui()
        # self.crearComponentesCU()
        return self.crearComponentesCU()

    def ValoresComponenteSui(self):
        valoresCU = self
        sql = self.util.getValoresComponenteSui(valoresCU)
        return sql

    def crearComponentesCU(self):
        valoresCU = self
        return self.util.getValoresComponentes(valoresCU)