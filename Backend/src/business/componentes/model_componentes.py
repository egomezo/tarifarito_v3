from .tools.componenteG_tool import ToolComponenteG
from .tools.componenteT_tool import ToolComponenteT
from .tools.componenteP097_tool import ToolComponenteP097
from .tools.componenteP015_tool import ToolComponenteP015
from .tools.componenteDtun_tool import ToolComponenteDtun
from .tools.componenteD097_tool import ToolComponenteD097
from .tools.componenteD015_tool import ToolComponenteD015
from .tools.componenteC_tool import ToolComponenteC
from .tools.componenteR_tool import ToolComponenteR
from .tools.costoUnitario_tool import ToolCostoUnitario


class ModelComponent:
    def __init__(self):
        self.operacion = None

    def getValoresComponenteSui():
        pass

    def getValoresGestor():
        pass

    def mergeDataframe():
        pass


class Util(ModelComponent):
    def __init__(self):
        Util.__init__(self)


class ModelComponenteG(Util):
    def __init__(self):
        self.operacion = ToolComponenteG()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)


class ModelComponenteT(Util):
    def __init__(self):
        self.operacion = ToolComponenteT()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)


class ModelComponenteP097(Util):
    def __init__(self):
        self.operacion = ToolComponenteP097()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)

    def getValoresGestor(self, mongodb):
        return self.operacion.getVariablesPerdidas(mongodb)

    def mergeDataframe(self, valoresSUI, valoresGestor):
        return self.operacion.merge_perdidas_P097(valoresSUI, valoresGestor)


class ModelComponenteP015(Util):
    def __init__(self):
        self.operacion = ToolComponenteP015()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)


class ModelComponenteDtun(Util):
    def __init__(self):
        self.operacion = ToolComponenteDtun()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)

    def getValoresGestor(self, mongodb, mercado):
        return self.operacion.getValoresADD(mongodb, mercado)

    def mergeDataframe(self, valoresSUI, valoresGestor):
        return self.operacion.merge_perdidas_Dtun(valoresSUI, valoresGestor)


class ModelComponenteD097(Util):
    def __init__(self):
        self.operacion = ToolComponenteD097()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)

    def getValoresGestor(self, mongodb, ano, periodo, empresa):
        perdidas = self.operacion.getVariablesPerdidas(mongodb)
        distribucion = self.operacion.getVariablesDistribucion(mongodb, ano, empresa)
        dane = self.operacion.getVariablesDane(mongodb, ano, periodo)
        dane2007 = self.operacion.getVariablesDane2007(mongodb, ano)
        return perdidas, distribucion, dane, dane2007

    def mergeDataframe(self, valoresSUI, perdidas, distribucion, dane, dane2007):
        return self.operacion.merge_data_D097(valoresSUI, perdidas, distribucion, dane, dane2007)


class ModelComponenteD015(Util):
    def __init__(self):
        self.operacion = ToolComponenteD015()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)


class ModelComponenteC(Util):
    def __init__(self):
        self.operacion = ToolComponenteC()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)

    def getValoresGestor(self, mongodb, ano, periodo, empresa):
        dane2013 = self.operacion.getVariablesDane2013(mongodb, ano)
        dane = self.operacion.getVariablesDane(mongodb, ano, periodo)
        comercializacion = self.operacion.getVariablesComercializacion(mongodb, ano, empresa)
        return dane2013, dane, comercializacion

    def mergeDataframe(self, valoresSUI, dane2013, dane, comercializacion, mercado):
        return self.operacion.merge_comercializacion(valoresSUI, dane2013, dane, comercializacion, mercado)


class ModelComponenteR(Util):
    def __init__(self):
        self.operacion = ToolComponenteR()

    def getValoresComponenteSui(self, componente):
        return self.operacion.getVariablesSUI(componente)


class ModelCostoUnitario(Util):
    def __init__(self):
        self.operacion = ToolCostoUnitario()

    def getValoresComponenteSui(self, valoresCU):
        return self.operacion.getVariablesSUI(valoresCU)

    def getValoresComponentes(self, valoresCU):
        return self.operacion.crearComponentes(valoresCU)
