from flask import Blueprint

from .Alicilar import alici_bp
from .Gonderici import gonderici_bp
from .Gonderiler import gonderi_bp

apiv1_bp = Blueprint("apiv1", __name__)

apiv1_bp.register_blueprint(alici_bp, url_prefix="/alicilar")

apiv1_bp.register_blueprint(gonderici_bp, url_prefix="/gondericiler")

apiv1_bp.register_blueprint(gonderi_bp, url_prefix="/gonderiler")




