from ...repository import InfoAddRepository

class InfoAddService:

    def get_infoAdd(self, g_infoAdd_repository: InfoAddRepository, mercado):
        print("GET MERCADO ---> ", mercado)
        if mercado == 0:
            # Consultar todos los registros
            result = []
            query = g_infoAdd_repository.get_infoADD_bd()
            for item in query:
                # print(result)
                item['_id'] = str(item['_id'])
                result.append(item)
            return result
        else:
            # Consultar un registro especifico
            result = []
            objeto = {}
            mercado = 'm_' + str(mercado)
            query = g_infoAdd_repository.get_infoADD_mercado_bd(mercado)
            lista = list(query)
            if len(lista) > 0:
                # print('lista > ', lista)
                if lista[0]['mercados']:
                    sizeArray = len(lista[0]['mercados'][mercado])
                    print("___________ SIZEARRAY _____________")
                    print(sizeArray)
                    objeto['mercado'] = mercado
                    for key, value in lista[0]['mercados'][mercado][sizeArray-1].items():
                        objeto[key] = value
                    result.append(objeto)
                    return result

    def post(self, g_infoAdd_repository: InfoAddRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_infoAdd_repository.post_infoADD(req)
        return result

    def put(self, g_infoAdd_repository: InfoAddRepository, mercado, req_model):
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_infoAdd_repository.put_infoADD(mercado, req_model)
        return result

    def delete(self, g_infoAdd_repository: InfoAddRepository):
        # Borrar documento
        result = g_infoAdd_repository.delete_infoADD()
        return result
