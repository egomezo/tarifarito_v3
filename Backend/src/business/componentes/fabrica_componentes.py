from .componente import *

# ---------------------------
# -- FABRICA COMPONENTES
# ---------------------------

class Fabrica:
    def crear_cpteG(self):
        pass

    def crear_cpteT(self):
        pass


class FabricaCU(Fabrica):
    def __init__(self):
        Fabrica.__init__(self)


class FabricaComponentes(FabricaCU):
    def crear_cpteG(self, ano, mes, empresa, mercado):
        cpte = ComponenteG(ano, mes, empresa, mercado)
        return cpte

    # def crear_cpteT(self, ano, mes, empresa, mercado, ntprop):
    #     return ComponenteT(ano, mes, empresa, mercado, ntprop)