import json

from ...business.componentes.componente import ComponenteD097

class ComponenteD097Repository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteD097_bd(self, componente: ComponenteD097):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteD097(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
