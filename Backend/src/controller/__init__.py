from flask import Blueprint

controller = Blueprint('controller', __name__, url_prefix='/')

from . import \
front_controller, \
anios_controller, \
empresas_controller, \
mercados_controller, \
empresa_mercado_controller \

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
componenteP097_controller
