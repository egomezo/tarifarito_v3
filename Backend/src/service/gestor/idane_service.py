from ...repository import IDaneRepository

class IDaneService:

    def __init__(self):
        self.meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    def get_idane(self, g_idane_repository: IDaneRepository, anio, mes):
        mydoc = []
        if anio == 0 and mes == "TODOS":
            # Consultar todos los registros
            query = g_idane_repository.get_idane_bd()
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and mes == "TODOS":
            # Consultar un registro especifico por anio
            query = g_idane_repository.get_idane_anio_bd(anio)
            for result in query:
                # print(result)
                result['_id'] = str(result['_id'])
                mydoc.append(result)
        elif anio != 0 and mes != "TODOS":
            mes = self.meses[int(mes) - 1]
            # Consultar un registro especifico por anio y mes
            objeto = {}
            lista = list(g_idane_repository.get_idane_anio_mes_bd(anio, mes))
            sizeArray = len(lista[0]['meses'][mes])
            # print("*SIZEARRAY -> ",  sizeArray)
            for key, value in lista[0]['meses'][mes][sizeArray-1].items():
                objeto[key] = value
            mydoc.append(objeto)
        return mydoc

    def post(self, g_idane_repository: IDaneRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_idane_repository.post_idane(req)
        return result

    def put(self, g_idane_repository: IDaneRepository, anio, req_model, req_mes):
        anio = anio if anio != 0 else 0
        print("_________ PUT MODEL _____________")
        print(req_model)
        print("_________________________________")
        # Modificar datos
        result = g_idane_repository.put_idane(anio, req_model, req_mes)
        return result

    def delete(self, g_idane_repository: IDaneRepository, anio):
        print("_________ DELETE ANIO ___________")
        print(anio)
        print("_________________________________")
        # Borrar documento
        result = g_idane_repository.delete_idane(anio)
        return result
