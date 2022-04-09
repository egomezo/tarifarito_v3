from sqlalchemy.sql import text


class EmpresaMercadoRepository:
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

    def get_empresa_mercado_bd(self, empresa, mercado):
        sql = '''
            SELECT IDEMPRESA,
            ARE_ESP_NOMBRE,
            'ENERGIA' SERVICIO,
            CASE WHEN ID_MERCADO IS NOT NULL THEN ID_MERCADO ELSE 0 END,
            CASE WHEN NOM_MERCADO IS NOT NULL THEN NOM_MERCADO ELSE '0' END 
            FROM
            (
            (
            SELECT EMPRESAS.IDEMPRESA,
                    EMPRESAS.ARE_ESP_NOMBRE,
                    MERCADOS.ID_MERCADO,
                    MERCADOS.NOM_MERCADO 
            FROM 
            (
                SELECT DISTINCT
                    IDENTIFICADOR_EMPRESA IDEMPRESA,
                    TRIM(NOMBRE_DE_LA_EMPRESA) ARE_ESP_NOMBRE
                FROM RENASER.BODEGA_EMPRESAS_ORFEO
                WHERE
                    ENERGIA = 1
            ) EMPRESAS,
            (
                SELECT 
                    DISTINCT ID_MERCADO,
                    ARE_ESP_SECUE,
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
            ) MERCADOS 
            WHERE 
                EMPRESAS.IDEMPRESA = MERCADOS.ARE_ESP_SECUE
                AND (EMPRESAS.IDEMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
            )
            UNION 
            (
            SELECT EMPRESAS.IDEMPRESA,
                    EMPRESAS.ARE_ESP_NOMBRE,
                    MERCADOS.ID_MERCADO,
                    MERCADOS.NOM_MERCADO 
            FROM 
            (
                SELECT DISTINCT
                    IDENTIFICADOR_EMPRESA IDEMPRESA,
                    TRIM(NOMBRE_DE_LA_EMPRESA) ARE_ESP_NOMBRE
                FROM RENASER.BODEGA_EMPRESAS_ORFEO
                WHERE
                    ENERGIA = 1
            ) EMPRESAS 
            LEFT JOIN 
            (
                SELECT 
                    DISTINCT ID_MERCADO,
                    ARE_ESP_SECUE,
                    NOM_MERCADO,
                    ESTADO 
                FROM 
                    CARG_COMERCIAL_E.MERCADO_EMPRESA 
                WHERE 
                    ESTADO = 'A'
                    AND NOM_MERCADO NOT LIKE '%Mercado Prueba%' 
                    AND NOM_MERCADO NOT LIKE '%Mercado de Prueba%' 
                ORDER BY 
                    NOM_MERCADO
            ) MERCADOS 
            ON 
                EMPRESAS.IDEMPRESA = MERCADOS.ARE_ESP_SECUE 
            WHERE 
                MERCADOS.ARE_ESP_SECUE IS NULL
            )
            )
            WHERE IDEMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG
        '''
        return self.db.engine.execute(text(sql), EMPRESA_ARG=empresa, MERCADO_ARG=mercado).fetchall()
