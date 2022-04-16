import json

class rComponentesMDBRepository:
    def __init__(self, mongodb):
        self.mongodb = mongodb

    def get_aggregate(self, anio, mes, empresa, mercado):
        query = self.mongodb.componentes.aggregate( [
                { "$match" : {'ano':anio, 'mes':mes, 'cod_empresa': empresa, 'cod_mercado': mercado} },
                { "$group" : {
                    "_id": {"nt_prop": "$nt_prop", "componente": "$componente"},
                    "usuario": { "$last": "$usuario" },
                    "ano": { "$last": "$ano" },
                    "mes": { "$last": "$mes" },
                    "cod_empresa": { "$last": "$cod_empresa" },
                    "nom_empresa": { "$last": "$nom_empresa" },
                    "cod_mercado": { "$last": "$cod_mercado" },
                    "nom_mercado": { "$last": "$nom_mercado" },
                    "componente": { "$last": "$componente" },
                    "nt_prop": { "$last": "$nt_prop" },
                    "novedad": { "$last": "$novedad" },
                    "fecha_modif": { "$last": "$fecha_modif" },
                    "estado": { "$last": "$estado" },
                    "componentes": { "$last": "$componentes" },
                    "values": { "$last": "$values" } } }
                ])
        return query
    
    def get_findAll(self, anio, mes, empresa, mercado, componente, ntprop):
        query = self.mongodb.componentes.find({'ano':anio, 'mes':mes, 'cod_empresa':empresa, 'cod_mercado':mercado, 'componente':componente, 'nt_prop':ntprop}).sort([("fecha_modif", -1)])
        return query

    def post(self, params):
        self.mongodb.componentes.insert_one(
            json.loads(params)
        )
        return 'Datos guardados!'
