import json

class IComercialRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_icomercial_bd(self):
        query = self.mongodb.infoComercial.find()
        return query

    def get_icomercial_anio_bd(self, anio):
        query = self.mongodb.infoComercial.find({"anio": anio})
        return query

    def get_icomercial_anio_empresa_bd(self, anio, empresa):
        query = self.mongodb.infoComercial.find({'anio': anio}, {'empresas.'+ empresa +'': 1})
        return query

    def post_icomercial(self, req):
        self.mongodb.infoComercial.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_icomercial(self, anio, req_model, req_empresa):
        self.mongodb.infoComercial.update_one(
            {"anio": anio},
            {"$push": {"empresas."+req_empresa: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_icomercial(self, anio):
        self.mongodb.infoComercial.delete_one({"anio": anio})
        return 'Datos eliminados!'