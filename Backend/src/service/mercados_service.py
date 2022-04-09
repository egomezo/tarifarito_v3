from ..repository import MercadosRepository


class MercadosService:

    def get_mercados(self, mercados_repository: MercadosRepository, mercado):
        mercados = []
        data = mercados_repository.get_mercados_bd(mercado)
        for result in data:
            mercados.append({
                'id_mercado': result[0],
                'nom_mercado': result[1],
                'estado': result[2]
            })
        return mercados
