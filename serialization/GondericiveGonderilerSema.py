from .ma import ma
from db import Gonderici
from .GondericiSema import GondericiSema


class GondericilerveGonderilerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Gonderici

    gonderiler = ma.Nested(GondericiSema, many=True)
