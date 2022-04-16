from .model_tarifas import ModelTarifas


class RegimenTarifario():
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.anio = ano
        self.periodo = mes
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = None

    def ValoresSui(self, db):
        self.db = db

    def ValoresGestor(self, mongodb):
        self.mongodb = mongodb

    def mergeData(self):
        pass


class Tarifa(RegimenTarifario):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        RegimenTarifario.__init__(self, ano, mes, empresa, mercado, ntprop)


class Tarifas(Tarifa):
    def __init__(self, ano, mes, empresa, mercado, ntprop):
        self.anio = ano
        self.periodo = mes
        self.periodo_menos1 = mes - 1
        self.empresa = empresa
        self.mercado = mercado
        self.ntprop = ntprop
        self.util = ModelTarifas()

    def ValoresSui(self, db):
        self.db = db
        tarifa = self
        sql = self.util.getValoresSui(tarifa)
        return sql

    def ValoresGestor(self, mongodb):
        self.mongodb = mongodb
        tarifa = self
        ipcMesAnterior, ipcMesConsulta = self.util.getValoresGestor(self.mongodb, tarifa)
        return ipcMesAnterior, ipcMesConsulta

    def mergeData(self, valoresSui, ipcMesAnterior, ipcMesConsulta):
        return self.util.mergeDataframe(valoresSui, ipcMesAnterior, ipcMesConsulta)
