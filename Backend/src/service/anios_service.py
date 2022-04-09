from ..repository import AniosRepository


class AniosService:

    def get_anios(self, anios_repository: AniosRepository, anio):
        anios = []
        if anio != 0:  # se ejecuta cuando se envia el año
            print("________Se recibe año________________")
            print(anio)
            print("____________________________")
            data = anios_repository.get_anios_bd(anio)
            for pqr in data:
                anios.append(
                    {
                        'anio': pqr[0],
                        'mes': pqr[1]
                    }
                )
            return anios
        else:  # se ejecuta cuando se quieren obtener todos los años
            print("________No se recibe año________________")
            print(anio)
            print("____________________________")
            data = anios_repository.get_anios_bd(anio)
            anio = 0
            for pqr in data:
                if anio != pqr[0]:
                    anios.append(
                        {
                            'anio': pqr[0]
                        }
                    )
                anio = pqr[0]
            return anios
