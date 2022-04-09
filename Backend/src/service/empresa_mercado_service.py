from ..repository import EmpresaMercadoRepository


class EmpresaMercadoService:

    def get_empresa_mercado(self, empresa_mercado_repository: EmpresaMercadoRepository, empresa, mercado):
        data = empresa_mercado_repository.get_empresa_mercado_bd(empresa, mercado)
        empresa = []
        if empresa != 0:
            for result in data:
                # print("RESULT -> ", result[3])
                if result[3] != 0: # La empresa tiene un mercado definido
                    empresa.append(
                        {
                            'cod_empresa': result[0],
                            'nom_empresa': result[1],
                            'servicio': result[2],
                            'mercados': [{'cod_mercado': result[3], 'nom_mercado': result[4]}],
                        }
                    )
                else: # La empresa es un comercializador (Atiende en todos los mercados)
                    mercados = []
                    # print("TODOS LOS MERCADOS!")
                    dataMercados = self.__getDataMercado(empresa_mercado_repository.get_mercados_bd(mercado=0))
                    for mercado in dataMercados:
                        mercados.append(
                            {'cod_mercado': mercado['id_mercado'], 'nom_mercado': mercado['nom_mercado']}
                        )
                    empresa.append(
                        {
                            'cod_empresa': result[0],
                            'nom_empresa': result[1],
                            'servicio': result[2],
                            'mercados': mercados
                        }
                    )
        return empresa

    def __getDataMercado(self, data):
        mercados = []
        for result in data:
            mercados.append({
                'id_mercado': result[0],
                'nom_mercado': result[1],
                'estado': result[2]
            })
        return mercados