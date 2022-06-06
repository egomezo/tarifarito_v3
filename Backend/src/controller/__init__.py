from flask import Blueprint

controller = Blueprint('controller', __name__, url_prefix='/')

from . import \
front_controller, \
anios_controller, \
empresas_controller, \
mercados_controller, \
empresa_mercado_controller, \
dependencia_controller, \
usuarios_controller

from .gestor import \
ntolerancia_controller, \
idane_controller, \
icomercial_controller, \
D097Resolucion_controller, \
D097Error_controller, \
perdidas_controller, \
infoAdd_controller

from .revisor import \
componenteG_controller, \
componenteT_controller, \
componenteP097_controller, \
componenteP015_controller,\
componenteDtun_controller, \
componenteD097_controller, \
componenteD015_controller, \
componenteC_controller, \
componenteR_controller, \
componentesMDB_controller, \
tarifas_controller, \
costoUnitario_controller
