import json

from ...componentes.componentes import ComponenteDtun

class ComponenteDtunRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteDtun_bd(self, componente: ComponenteDtun):
        valoresSUI = componente.ValoresComponenteSui(self.db)
        valoresGestor = componente.ValoresComponenteGestor(self.mongodb)
        return componente.mergeData(valoresSUI, valoresGestor)

    def post_componenteDtun(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
