from .tools.tarifas_tool import ToolTarifas


class ModelRegimenTarifario:
    def __init__(self):
        self.operacion = None

    def getValoresSui():
        pass

    def getValoresGestor():
        pass

    def mergeDataframe():
        pass


class Util(ModelRegimenTarifario):
    def __init__(self):
        Util.__init__(self)


class ModelTarifas(Util):
    def __init__(self):
        self.operacion = ToolTarifas()

    def getValoresSui(self, tarifa):
        return self.operacion.getVariablesSUI(tarifa)

    def getValoresGestor(self, mongodb, tarifa):
        ipcMesAnterior = self.operacion.getIPC(mongodb, tarifa.anio, tarifa.periodo, 2)
        ipcMesConsulta = self.operacion.getIPC(mongodb, tarifa.anio, tarifa.periodo, 1)
        return ipcMesAnterior, ipcMesConsulta

    def mergeDataframe(self, valoresSui, ipcMesAnterior, ipcMesConsulta):
        result = self.operacion.calcular_tarifas(valoresSui, ipcMesAnterior, ipcMesConsulta)
        return result
