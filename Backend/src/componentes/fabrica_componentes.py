from componentes import *

# ---------------------------
# -- Fabrica
# ---------------------------

class Fabrica:
    def crear_cpteg(self):
        pass

    def crear_cptet(self):
        pass

class FabricaComponentes(Fabrica):
    def crear_cpteg(self):
        return ComponenteG()

    def crear_cptet(self):
        return ComponenteT()