from .tools.componenteP097_tool import ToolComponenteP097
from .tools.componenteG_tool import ToolComponenteG
from .tools.componenteT_tool import ToolComponenteT


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
