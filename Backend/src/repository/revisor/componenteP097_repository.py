import json

from ...componentes.componentes import ComponenteP097

class ComponenteP097Repository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteP097_bd(self, componente: ComponenteP097):
        valoresSUI = componente.ValoresComponenteSui(self.db)
        valoresGestor = componente.ValoresComponenteGestor(self.mongodb)
        return componente.mergeData(valoresSUI, valoresGestor)

    def post_componenteP097(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
