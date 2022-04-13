from ...repository import ComponenteTRepository

class ComponenteTService:

    def get_componenteT(self, g_componenteT_repository: ComponenteTRepository, componenteT):
        cpte = []
        data = g_componenteT_repository.get_componenteT_bd(componenteT)
        for result in data:
            cpte.append(
                {
                    'ano': result[3],
                    'mes': result[4],
                    'empresa': result[0],
                    'mercado': result[1],
                    'ntprop': result[2],
                    'values': {
                        'DATAPUBLICADA': [
                            result[5], #C3 - STNAGENTE
                            result[6]  #C4 - STNLAC
                        ],
                        'CALCULOSSPD': [
                            0, #C - TLAC
                            0, #C - DTLAC
                            0  #C - CPT
                        ],
                        'DIFERENCIA': [
                            0, #C - CPTAGENTE
                            0  #C - CPTLAC
                        ]
                    },
                }
            )
        return cpte

    def post(self, g_componenteT_repository: ComponenteTRepository, req):
        print("_________ POST MODEL _____________")
        print(req)
        print("_________________________________")
        # Insertar datos
        result = g_componenteT_repository.post_componenteT(req)
        return result
