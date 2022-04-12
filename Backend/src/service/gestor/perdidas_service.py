from ...repository import PerdidasRepository

class PerdidasService:

    def get_perdidas(self, g_perdidas_repository: PerdidasRepository, anio, mercado):
        print("___________ GET ANIO_____________")
        print(anio)
        print("_________________________________")
        if anio == 0 and mercado == 0:
            # Consultar todos los registros
            result = []
            query = g_perdidas_repository.get_perdidas_bd()
            for item in query:
                # print(result)
                item['_id'] = str(item['_id'])
                result.append(item)
            return result
        elif anio == 0 and mercado != 0:
            print("___________ MERCADO _____________")
            print(mercado)
            # Consultar un registro especifico
            result = []
            objeto = {}
            lista = list(g_perdidas_repository.get_perdidas_mercado_bd(mercado))
            sizeArray = len(lista[0]['mercados']['m_'+mercado])
            print("___________ SIZEARRAY _____________")
            print(sizeArray)
            objeto['mercado'] = mercado
            for key, value in lista[0]['mercados']['m_'+mercado][sizeArray-1].items():
                objeto[key] = value
            result.append(objeto)
            return result

    def post(self, g_perdidas_repository: PerdidasRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_perdidas_repository.post_perdidas(req)
        return result

    def put(self, g_perdidas_repository: PerdidasRepository, anio, req_model, req_mes):
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_perdidas_repository.put_perdidas(anio, req_model, req_mes)
        return result

    def delete(self, g_perdidas_repository: PerdidasRepository, anio):
        print("_________ DELETE ANIO ___________")
        print(anio)
        print("_________________________________")
        # Borrar documento
        result = g_perdidas_repository.delete_perdidas(anio)
        return result
