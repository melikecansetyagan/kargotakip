from .ma import ma
from db import Alici
from .AliciSema import AliciSema

class AlicilarveGonderilerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alici

    gonderiler = ma.Nested(AliciSema, many=True)
