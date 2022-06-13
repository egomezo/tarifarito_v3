from sqlalchemy.sql import text


class DependenciaRepository:
    def __init__(self, db):
        self.db = db

    def get_dependencia_bd(self, iddependencia):
        sql = '''
            SELECT * FROM public."Dependencias"
            WHERE ID_DEPENDENCIA = :IDDEPENDENCIA_ARG OR 0 = :IDDEPENDENCIA_ARG;
        '''
        return self.db.engine.execute(text(sql), IDDEPENDENCIA_ARG=iddependencia).fetchall()
    
    def get_area_bd(self, iddependencia):
        sql = '''
            SELECT ID_AREA, NOMBRE_AREA FROM public."Areas"
            WHERE ID_DEPENDENCIA = :IDDEPENDENCIA_ARG OR 0 = :IDDEPENDENCIA_ARG;
        '''
        return self.db.engine.execute(text(sql), IDDEPENDENCIA_ARG=iddependencia).fetchall()