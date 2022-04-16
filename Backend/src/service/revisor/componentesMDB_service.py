from ...repository import rComponentesMDBRepository

class rComponentesMDBService:

    def get_r_componentesMDB(self, r_componentesMDB_repository: rComponentesMDBRepository, anio, mes, empresa, mercado, componente, ntprop):
        if componente == "TODOS" and ntprop == "TODOS":
            mydoc = r_componentesMDB_repository.get_aggregate(anio, mes, empresa, mercado)
            mydoc = list(mydoc)
        else:
            # TRAEMOS TODO EL HISTORICO DEL COMPONENTE GURADADO
            mydoc = []
            result = r_componentesMDB_repository.get_findAll(anio, mes, empresa, mercado, componente, ntprop)
            for item in result:
                mydoc.append(
                    {
                        'usuario': item['usuario'],
                        "ano": item['ano'],
                        "mes": item['mes'],
                        "cod_empresa": item['cod_empresa'],
                        "nom_empresa": item['nom_empresa'],
                        "cod_mercado": item['cod_mercado'],
                        "nom_mercado": item['nom_mercado'],
                        "componente": item['componente'],
                        "nt_prop": item['nt_prop'],
                        "novedad": item['novedad'],
                        "fecha_modif": item['fecha_modif'],
                        "estado": item['estado'],
                        "componentes": item['componentes'],
                        "values": item['values']
                    }
                )
        return mydoc

    def post(self, r_componentesMDB_repository: rComponentesMDBRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = r_componentesMDB_repository.post(req)
        return result