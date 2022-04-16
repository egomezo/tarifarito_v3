from ...business.tarifas.tarifa import Tarifas


class TarifasRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_tarifas_bd(self, tarifas: Tarifas):
        valoresSUI = tarifas.ValoresSui(self.db)
        ipcMesAnterior, ipcMesConsulta = tarifas.ValoresGestor(self.mongodb)
        return tarifas.mergeData(valoresSUI, ipcMesAnterior, ipcMesConsulta)
