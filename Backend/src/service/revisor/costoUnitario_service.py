from ...repository import CostoUnitarioRepository
import time

class CostoUnitarioService:

    def get_costoUnitario(self, r_costoUnitario_repository: CostoUnitarioRepository, costoUnitario):
        print(f"started at {time.strftime('%X')}")
        data = r_costoUnitario_repository.get_costoUnitario_bd(costoUnitario)
        # print('-----------------------------')
        # print('-- COSTO UNITARIO >> ', data)
        # print('-----------------------------')
        # cpte = []
        # for result in data:
        #     cpte.append(
        #         {
        #             'ano': result[3],
        #             'mes': result[4],
        #             'empresa': result[0],
        #             'mercado': result[1],
        #             'ntprop': result[2],
        #         }
        #     )
        # print(f"finished at {time.strftime('%X')}")
        # return cpte