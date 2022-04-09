import json

class NtoleranciaRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_ntolerancia_bd(self):
        query = self.mongodb.nivelTolerancia.find()
        return query

    def get_ntolerancia_anio_bd(self, anio):
        query = self.mongodb.nivelTolerancia.find({"anio": anio})
        return query

    def get_ntolerancia_anio_mes_bd(self, anio, mes):
        query = self.mongodb.nivelTolerancia.find({'anio': anio}, {'meses.'+ mes +'': 1})
        return query

    def post_ntolerancia(self, req):
        self.mongodb.nivelTolerancia.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_ntolerancia(self, anio, req_model, req_mes):
        self.mongodb.nivelTolerancia.update_one(
            {"anio": anio},
            {"$push": {"meses."+req_mes: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_ntolerancia(self, anio):
        self.mongodb.nivelTolerancia.delete_one({"anio": anio})
        return 'Datos eliminados!'