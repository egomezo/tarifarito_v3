import json

from ...business.componentes.componentes import ComponenteD097

class ComponenteD097Repository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteD097_bd(self, componente: ComponenteD097):
        valoresSUI = componente.ValoresComponenteSui(self.db)
        perdidas, distribucion, dane, dane2007 = componente.ValoresComponenteGestor(self.mongodb)
        return componente.mergeData(valoresSUI, perdidas, distribucion, dane, dane2007)

    def post_componenteD097(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
