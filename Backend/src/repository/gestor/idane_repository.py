import json

class IDaneRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_idane_bd(self):
        # Consultar todos los registros
        query = self.mongodb.indicesDANE.find()
        return query

    def get_idane_anio_bd(self, anio):
        query = self.mongodb.indicesDANE.find({"anio": anio})
        return query

    def get_idane_anio_mes_bd(self, anio, mes):
        query = self.mongodb.indicesDANE.find({'anio': anio}, {'meses.'+ mes +'': 1})
        return query

    def post_idane(self, req):
        self.mongodb.indicesDANE.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_idane(self, anio, req_model, req_mes):
        self.mongodb.indicesDANE.update_one(
            {"anio": anio},
            {"$push": {"meses."+req_mes: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_idane(self, anio):
        self.mongodb.indicesDANE.delete_one({"anio": anio})
        return 'Datos eliminados!'