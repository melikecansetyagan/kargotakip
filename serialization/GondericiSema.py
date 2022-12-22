from .ma import ma
from db import Gonderici


class GondericiSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Gonderici
        load_instance = True