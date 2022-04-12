import json

class D097ResolucionRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_resolucion_bd(self):
        query = self.mongodb.infoD097Res.find()
        return query

    def get_resolucion_anio_bd(self, anio):
        query = self.mongodb.infoD097Res.find({"anio": anio})
        return query

    def get_resolucion_anio_empresa_bd(self, anio, empresa):
        query = self.mongodb.infoD097Res.find({'anio': anio}, {'empresas.'+ empresa +'': 1})
        return query

    def post_resolucion(self, req):
        self.mongodb.infoD097Res.insert_one(
            json.loads(req)
        )
        return 'Datos guardados!'
    
    def put_resolucion(self, anio, req_model, req_empresa):
        self.mongodb.infoD097Res.update_one(
            {"anio": anio},
            {"$push": {"empresas."+req_empresa: {"$each": [json.loads(req_model)]}}}
        )
        return 'Datos actualizados!'
    
    def delete_resolucion(self, anio):
        self.mongodb.infoD097Res.delete_one({"anio": anio})
        return 'Datos eliminados!'