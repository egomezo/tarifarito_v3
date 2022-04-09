from ..repository import EmpresasRepository


class EmpresasService:

    def get_empresas(self, empresas_repository: EmpresasRepository, empresa):
        empresas = []
        data = empresas_repository.get_empresas_bd(empresa)
        for result in data:
            if result[0] == 20217:
                lst = list(result)
                lst[1] = "UNIDAD DE SERVICIOS PUBLICOS - VAUPES"
                result = tuple(lst)
            elif result[0] == 497:
                lst = list(result)
                lst[1] = "PROMOTORA DE ENERGIA ELECTRICA DE CARTAGENA"
                result = tuple(lst)
            elif result[0] == 2452:
                lst = list(result)
                lst[1] = "COMERCIALIZADORA ANDINA DE ENERGIA"
                result = tuple(lst)
            elif result[0] == 1900:
                lst = list(result)
                lst[1] = "E.A.T. DE PRESTACION DE SERVCIOS PUBLICOS MOSQUERA"
                result = tuple(lst)
            elif result[0] == 3111:
                lst = list(result)
                lst[1] = "ENERGETICOS S.A.S. DISTRIBUIDORA"
                result = tuple(lst)
            elif result[0] == 1720:
                lst = list(result)
                lst[1] = "SOCIEDAD PRODUCTORA DE ENERGÍA DE SAN ANDRES Y PROV"
                result = tuple(lst)
            elif result[0] == 2261:
                lst = list(result)
                lst[1] = "TERMOCANDELARIA SOCIEDAD EN COMANDITA POR ACCIONES"
                result = tuple(lst)
            empresas.append(
                {
                    'cod_empresa': result[0],
                    'nombre': result[1],
                    'servicio': result[2],
                    'sigla': result[3],
                    'NIT': result[4]
                }
            )
        return empresas
