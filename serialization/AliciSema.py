from .ma import ma
from db import Alici

class AliciSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alici
        load_instance = True