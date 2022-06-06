from flask import abort
from ..repository import DependenciaRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class DependenciaService:

    def get_dependencia(self, dependencia_repository: DependenciaRepository, iddependencia):
        dependencia = []
        data = dependencia_repository.get_dependencia_bd(iddependencia)
        for result in data:
            dependencia.append(
                {
                    'iddependencia': result[0],
                    'nombre': result[1],
                    'descripcion': result[2],
                }
            )
        return dependencia