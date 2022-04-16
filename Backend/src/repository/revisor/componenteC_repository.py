import json

from ...business.componentes.componentes import ComponenteC

class ComponenteCRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteC_bd(self, componente: ComponenteC):
        valoresSUI = componente.ValoresComponenteSui(self.db)
        dane2013, dane, comercializacion = componente.ValoresComponenteGestor(self.mongodb)
        return componente.mergeData(valoresSUI, dane2013, dane, comercializacion)

    def post_componenteC(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
