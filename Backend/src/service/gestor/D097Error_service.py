from ...repository import D097ErrorRepository

class D097ErrorService:
    
    def get_error(self, g_error_repository: D097ErrorRepository, f_inicial, f_final):
        mydoc = []
        print("___________ GET FINICIAL_____________")
        print(f_inicial)
        print("_________________________________")
        if f_inicial == '':
            # Consultar todos los registros
            data = g_error_repository.get_error_bd()
        elif f_inicial != '' and f_final == '':
            # Consultar un registro especifico por fecha inicial
            data = g_error_repository.get_error_f_inicial_bd(f_inicial)
        else:
            # Consultar un registro especifico por ambas fechas
            data = g_error_repository.get_error_f_inicial_f_final_bd(f_inicial, f_final)
        
        for result in data:
            # print(result)
            result['_id'] = str(result['_id'])
            mydoc.append(result)
        return mydoc

    def post(self, g_error_repository: D097ErrorRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_error_repository.post_error(req)
        return result

    def put(self, g_error_repository: D097ErrorRepository, f_inicial, f_final, req_model, req_empresa):
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_error_repository.put_error(f_inicial, f_final, req_model, req_empresa)
        return result

    def delete(self, g_error_repository: D097ErrorRepository, f_inicial):
        print("_________ DELETE ANIO ___________")
        print(f_inicial)
        print("_________________________________")
        # Borrar documento
        result = g_error_repository.delete_error(f_inicial)
        return result
