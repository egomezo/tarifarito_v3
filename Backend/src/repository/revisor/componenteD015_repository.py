import json

from ...componentes.componentes import ComponenteD015

class ComponenteD015Repository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteD015_bd(self, componente: ComponenteD015):
        return componente.ValoresComponenteSui(self.db)

    def post_componenteD015(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
