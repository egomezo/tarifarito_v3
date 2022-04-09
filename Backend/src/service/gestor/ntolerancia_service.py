from ...repository import NtoleranciaRepository

class NtoleranciaService:

    def __init__(self):
        self.meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    def get_ntolerancia(self, g_ntolerancia_repository: NtoleranciaRepository, anio, mes):
        mydoc = []
        if anio == 0 and mes == "TODOS":
            # Consultar todos los registros
            query = g_ntolerancia_repository.get_ntolerancia_bd()
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and mes == "TODOS":
            # Consultar un registro especifico por anio
            query = g_ntolerancia_repository.get_ntolerancia_anio_bd(anio)
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and mes != "TODOS":
            mes = self.meses[int(mes) - 1]
            # Consultar un registro especifico por anio y mes
            objeto = {}
            lista = list(g_ntolerancia_repository.get_ntolerancia_anio_mes_bd(anio, mes))
            sizeArray = len(lista[0]['meses'][mes])
            # print("*SIZEARRAY -> ",  sizeArray)
            for key, value in lista[0]['meses'][mes][sizeArray-1].items():
                objeto[key] = value
            mydoc.append(objeto)
        return mydoc

    def post(self, g_ntolerancia_repository: NtoleranciaRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_ntolerancia_repository.post_ntolerancia(req)
        return result

    def put(self, g_ntolerancia_repository: NtoleranciaRepository, anio, req_model, req_mes):
        anio = anio if anio != 0 else 0
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_ntolerancia_repository.put_ntolerancia(anio, req_model, req_mes)
        return result

    def delete(self, g_ntolerancia_repository: NtoleranciaRepository, anio):
        print("_________ DELETE ANIO ___________")
        print(anio)
        print("_________________________________")
        # Borrar documento
        result = g_ntolerancia_repository.delete_ntolerancia(anio)
        return result
