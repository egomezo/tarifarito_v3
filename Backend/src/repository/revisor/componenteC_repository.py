import json

from ...business.componentes.componente import ComponenteC

class ComponenteCRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteC_bd(self, componente: ComponenteC):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteC(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
