import json

from ...business.componentes.componente import ComponenteG

class ComponenteGRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteG_bd(self, componente: ComponenteG):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteG(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!!!'