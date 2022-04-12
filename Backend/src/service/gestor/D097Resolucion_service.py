from ...repository import D097ResolucionRepository

class D097ResolucionService:
    
    def get_resolucion(self, g_resolucion_repository: D097ResolucionRepository, anio, empresa):
        mydoc = []
        if anio == 0 and empresa == "TODOS":
            # Consultar todos los registros
            query = g_resolucion_repository.get_resolucion_bd()
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and empresa == "TODOS":
            # Consultar un registro especifico por anio
            query = g_resolucion_repository.get_resolucion_anio_bd(anio)
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and empresa != "TODOS":
            # Consultar un registro especifico por anio y empresa
            objeto = {}
            lista = list(g_resolucion_repository.get_resolucion_anio_empresa_bd(anio, empresa))
            sizeArray = len(lista[0]['empresas'][empresa])
            # print("*SIZEARRAY -> ",  sizeArray)
            for key, value in lista[0]['empresas'][empresa][sizeArray-1].items():
                objeto[key] = value
            mydoc.append(objeto)
        return mydoc

    def post(self, g_resolucion_repository: D097ResolucionRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_resolucion_repository.post_resolucion(req)
        return result

    def put(self, g_resolucion_repository: D097ResolucionRepository, anio, req_model, req_empresa):
        anio = anio if anio != 0 else 0
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_resolucion_repository.put_resolucion(anio, req_model, req_empresa)
        return result

    def delete(self, g_resolucion_repository: D097ResolucionRepository, anio):
        print("_________ DELETE ANIO ___________")
        print(anio)
        print("_________________________________")
        # Borrar documento
        result = g_resolucion_repository.delete_resolucion(anio)
        return result
