from .cptes import ComponenteG

class FabricaComponentes():
    def crear_cpteG(self, ano, mes, empresa, mercado):
        cpte = ComponenteG(ano, mes, empresa, mercado)
        return cpte