import json

from ...business.componentes.componente import ComponenteDtun

class ComponenteDtunRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteDtun_bd(self, componente: ComponenteDtun):
        return componente.getValues(self.db, self.mongodb)

    def post_componenteDtun(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
