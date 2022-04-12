import json

class D097ErrorRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_error_bd(self):
        query = self.mongodb.infoD097Error.find()
        return query

    def get_error_f_inicial_bd(self, f_inicial):
        query = self.mongodb.infoD097Error.find({"f_inicial": f_inicial})
        return query

    def get_error_f_inicial_f_final_bd(self, f_inicial, f_final):
        query = self.mongodb.infoD097Error.find({"f_inicial": f_inicial, "f_final": f_final})
        return query

    def post_error(self, req):
        self.mongodb.infoD097Error.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_error(self, f_inicial, f_final, req_model, req_empresa):
        self.mongodb.infoD097Error.update_one(
            {"f_inicial": f_inicial, "f_final": f_final},
            {"$push": {"empresas."+req_empresa: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_error(self, f_inicial):
        self.mongodb.infoD097Error.delete_one({"f_inicial": f_inicial})
        return 'Datos eliminados!'