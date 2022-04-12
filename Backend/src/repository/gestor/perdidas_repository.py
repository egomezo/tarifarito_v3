import json

class PerdidasRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_perdidas_bd(self):
        query = self.mongodb.perdidasSTN.find()
        return query

    def get_perdidas_mercado_bd(self, mercado):
        query = self.mongodb.perdidasSTN.find({'anio':0}, {'mercados.m_'+mercado:1})
        return query

    def post_perdidas(self, req):
        self.mongodb.perdidasSTN.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_perdidas(self, anio, req_model, req_mercado):
        self.mongodb.perdidasSTN.update_one(
            {"anio": anio},
            {"$push": {"mercados."+req_mercado: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_perdidas(self, anio):
        self.mongodb.perdidasSTN.delete_one({"anio": anio})
        return 'Datos eliminados!'