from ...business.componentes.componente import CostoUnitario
import time

class CostoUnitarioRepository:
    def __init__(self, db, mongodb):
        self.db = db
        self.mongodb = mongodb

    def get_costoUnitario_bd(self, costoUnitario: CostoUnitario):
        result = costoUnitario.getValues(self.db, self.mongodb)
        # print('-----------------------------')
        # print('-- COSTO UNITARIO >> ', result)
        # print('-----------------------------')
        return result
