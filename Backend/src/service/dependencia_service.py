from ..repository import DependenciaRepository

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
    
    def get_area(self, dependencia_repository: DependenciaRepository, iddependencia):
        area = []
        data = dependencia_repository.get_area_bd(iddependencia)
        for result in data:
            area.append(
                {
                    'idarea': result[0],
                    'nombre': result[1]
                }
            )
        return area