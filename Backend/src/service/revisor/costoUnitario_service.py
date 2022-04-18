from ...repository import CostoUnitarioRepository
import time
from datetime import datetime

class CostoUnitarioService:

    def get_costoUnitario(self, r_costoUnitario_repository: CostoUnitarioRepository, costoUnitario):
        timeStart = datetime.today()
        print(f"started at {timeStart.strftime('%X')}")
        data = r_costoUnitario_repository.get_costoUnitario_bd(costoUnitario)
        timeEnd = datetime.today()
        print(f"finished at {timeEnd.strftime('%X')}")
        timeTotal = timeEnd - timeStart
        print(f"Time Total = {timeTotal}")
        return data