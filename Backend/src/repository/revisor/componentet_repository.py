from sqlalchemy.sql import text
import json

from ...componentes.componentes import ComponenteT

class ComponenteTRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteT_bd(self, componente: ComponenteT):
        return componente.ValoresComponente(self.db)

    def post_componenteT(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'