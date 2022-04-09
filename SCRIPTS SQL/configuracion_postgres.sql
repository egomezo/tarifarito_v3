----------------------------
-- COMANDO PARA CREAR UNA BASE DE DATOS
----------------------------
1. sudo -i -u postgres -- Acceder al esquema por defecto 
2. postgres@1pc7-220-17741:~$ createdb procesos_dieg_pruebas -- Crear base de datos
3. postgres@1pc7-220-17741:~$ psql -d procesos_dieg_pruebas -- Acceder a la base de datos (utilizar BD)
4. procesos_dieg_pruebas=# \l -- Listar bases de datos
5. procesos_dieg_pruebas=# select * from rol; -- Hacer consulta a la BD 
6. procesos_dieg_pruebas=# \q -- Salir de la conexion de la BD

--------------------------------------
-- COMANDO PARA HACER BACKUP DE LA BD
--------------------------------------
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > 3_procesos14072021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/1_procesos14072021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/2_procesos25072021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/3_procesos25072021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/4_procesos09082021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/5_procesos12082021.sql
pg_dump -U procesos_dieg -W -h localhost procesos_dieg > backupbddieg/backups_bd/6_procesos21092021.sql

pg_dump -U procesos_dieg -W -h localhost procesos_dieg_pruebas > backupbd_procesosdieg/prueba_backup.sql

----------------------------
-- COMANDO PARA RESTAURAR BACKUP DE LA BASE DE DATOS
----------------------------
1. sudo -i -u postgres
2. postgres@vmunigrasas:~$ createdb juank
3. psql -U procesos_dieg -W -h localhost juank < 3_procesos13072021.sql (Ejecutarlo en la terminal de LINUX)
3.1 psql -U procesos_dieg -W -h localhost procesos_dieg < backupbddieg/backups_bd/3_procesos25072021.sql (Ejecutarlo en la terminal de LINUX)
3.1 psql -U procesos_dieg -W -h localhost procesos_dieg_pruebas < backupbddieg/backups_bd/3_procesos25072021.sql (Ejecutarlo en la terminal de LINUX)

psql -U procesos_dieg -W -h localhost procesos_dieg < backupbd_procesosdieg/2_diegpsql28022022.sql

----------------------------
-- COMANDO PARA ASIGNAR ROL DE SUPERUSUARIO
----------------------------
postgres# ALTER ROLE <user_name> SUPERUSER;

----------------------------
-- COMANDO PARA OBTENER LISTADO DE TABLAS Y SU RESPECTIVO TAMAÑO EN DISCO
----------------------------
\dt+

----------------------------
-- NOTA. CUANDO EL SISTEMA ARROJE ESTE ERROR 
-- "ERROR:  error de sintaxis en o cerca de «FUNCTION»
-- LÍNEA 1: ...TER INSERT ON public.proceso FOR EACH ROW EXECUTE FUNCTION p..."
-- ES DEBIDO A LA VERSION DEL POSTGRESQL QUE SE ESTA UTILIZANDO YA QUE ESY¿TA RESTAURANDO UN BACKUP DE VERSION 12 EN UNA VERSION INFERIOR
-- Y AL MOMENTO DE CREAR EL TRIGGER SE REVIENTA EL BACKUP, A CONTINUACION SE EVIDENCIA EL CAMBIO DE SINTAXIS ENTRE VERSIONES
-- CREATE TRIGGER tr_proceso AFTER INSERT ON public.proceso FOR EACH ROW EXECUTE PROCEDURE public.sp_proceso(); [VERSION 10]
-- CREATE TRIGGER tr_proceso AFTER INSERT ON public.proceso FOR EACH ROW EXECUTE FUNCTION public.sp_proceso(); [VERSION 12] [EL TERMINO PROCEDURE SE CAMBIO POR FUNCTION]
-- PARA SOLUCIONAR ESTO DEBEMOS CARGAR EL TRIGGER POR CONSOLA DE SQL
----------------------------


----------------------------
-- COMANDO PARA ELIMINAR UNA BASE DE DATOS
----------------------------
1. sudo -i -u postgres -- Acceder al esquema por defecto
2. postgres@1pc7-220-17741:~$ psql
3. Ejecutar script para matar conexiones a la BD:
    SELECT *, pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = 'juank';
4. postgres=# DROP DATABASE juank;

SELECT * FROM crosstab($$
SELECT EXPEDIENTE, CAUSAL.NOMBRECAUSAL, CAUSAL AS CAUSA
FROM HISTORICO_INFO_ESPECIFICA HIE, CAUSAL
WHERE HIE.CAUSAL = CAUSAL.IDCAUSAL
AND EXPEDIENTE = '2020240350600023E'
GROUP BY EXPEDIENTE, CAUSAL.NOMBRECAUSAL, CAUSAL
$$,
$$ select nombrecausal from causal $$)
AS t (
	"EXPEDIENTE" TEXT,
	"Falla en la prestación del servicio" TEXT,
	"Incumplimiento de aspectos técnicos" TEXT,
	"Incumplimiento de los indicadores de calidad" TEXT,
	"No atención a requerimientos" TEXT,
	"Retie" TEXT,
	"SUI" TEXT,
	"Violación régimen tarifario" TEXT,
	"Violación reglamentaria" TEXT,
	"RUPS" TEXT,
	"Incumplimientos relacionados con la facturación" TEXT
);
-- select count(*) from information_schema.routines where routine_name like 'crosstab%'; -- Si sale cero no se ha ejecutado la creacion de la extension

-- CREATE EXTENSION IF NOT EXISTS tablefunc; -- Ejecutar como superusuario (psql -d procesos_dieg_pruebas)

SELECT * FROM crosstab($$
SELECT EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL AS CAUSA
FROM HISTORICO_INFO_ESPECIFICA HIE, CAUSAL
WHERE HIE.CAUSAL = CAUSAL.IDCAUSAL
GROUP BY EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL
ORDER BY EXPEDIENTE
$$,
$$ select IDCAUSAL from causal $$)
AS t (
	"EXPEDIENTE" TEXT,
	"Falla en la prestación del servicio" TEXT,
	"Incumplimiento de aspectos técnicos" TEXT,
	"Incumplimiento de los indicadores de calidad" TEXT,
	"No atención a requerimientos" TEXT,
	"Retie" TEXT,
	"SUI" TEXT,
	"Violación régimen tarifario" TEXT,
	"Violación reglamentaria" TEXT,
	"RUPS" TEXT,
	"Incumplimientos relacionados con la facturación" TEXT
);

SELECT * FROM crosstab($$
SELECT EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL AS CAUSA
FROM HISTORICO_INFO_ESPECIFICA HIE, CAUSAL
WHERE HIE.CAUSAL = CAUSAL.IDCAUSAL
GROUP BY EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL
ORDER BY EXPEDIENTE
$$,
$$ select IDCAUSAL from causal $$)
AS t (
	"EXPEDIENTE" TEXT,
	"1" TEXT,
	"2" TEXT,
	"3" TEXT,
	"4" TEXT,
	"5" TEXT,
	"6" TEXT,
	"7" TEXT,
	"8" TEXT,
	"9" TEXT,
	"10" TEXT
);

SELECT * FROM crosstab($$
SELECT EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL AS CAUSA
FROM HISTORICO_INFO_ESPECIFICA HIE, CAUSAL
WHERE HIE.CAUSAL = CAUSAL.IDCAUSAL
GROUP BY EXPEDIENTE, CAUSAL, CAUSAL.NOMBRECAUSAL
ORDER BY EXPEDIENTE
$$,
$$ select IDCAUSAL from causal $$)
AS t (
	EXPEDIENTE TEXT,
	"1" TEXT,
	"2" TEXT,
	"3" TEXT,
	"4" TEXT,
	"5" TEXT,
	"6" TEXT,
	"7" TEXT,
	"8" TEXT,
	"9" TEXT,
	"10" TEXT
)
WHERE "6" = 'SUI';