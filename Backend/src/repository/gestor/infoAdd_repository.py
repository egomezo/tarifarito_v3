import json

class InfoAddRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_infoADD_bd(self):
        query = self.mongodb.infoADD.find()
        return query

    def get_infoADD_mercado_bd(self, mercado):
        query = self.mongodb.infoADD.find({'key':0}, {'mercados.' + mercado: 1})
        return query

    def post_infoADD(self, req):
        self.mongodb.infoADD.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_infoADD(self, req_model, req_mercado):
        self.mongodb.infoADD.update_one(
            {"key": 0},
            {"$push": {"mercados."+req_mercado: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_infoADD(self):
        self.mongodb.infoADD.delete_one({"key": 0})
        return 'Datos eliminados!'