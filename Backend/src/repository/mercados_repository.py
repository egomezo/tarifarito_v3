from sqlalchemy.sql import text


class MercadosRepository:
    def __init__(self, db):
        self.db = db

    def get_mercados_bd(self, mercado):
        sql = '''
            SELECT 
                DISTINCT ID_MERCADO,
                NOM_MERCADO,
                ESTADO 
            FROM 
                CARG_COMERCIAL_E.MERCADO_EMPRESA 
            WHERE 
                ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG 
                AND ESTADO = 'A'
                AND NOM_MERCADO NOT LIKE '%Mercado Prueba%' 
                AND NOM_MERCADO NOT LIKE '%Mercado de Prueba%' 
            ORDER BY 
                NOM_MERCADO
        '''
        return self.db.engine.execute(text(sql), MERCADO_ARG=mercado).fetchall()
