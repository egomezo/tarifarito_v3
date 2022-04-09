from flask import Blueprint

controller = Blueprint('controller', __name__, url_prefix='/')

from . import \
front_controller, \
anios_controller, \
empresas_controller, \
mercados_controller, \
empresa_mercado_controller \

from .gestor import \
ntolerancia_controller