from sqlalchemy.sql import text
import json

from ...componentes.componentes import ComponenteG

class ComponenteGRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_componenteG_bd(self, componente: ComponenteG):
        return componente.ValoresComponente(self.db)

    def post_componenteG(self, req):
        self.mongodb.componentes.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'