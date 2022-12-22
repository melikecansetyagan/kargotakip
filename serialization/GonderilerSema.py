from .ma import ma
from db import Gonderiler


class GonderilerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Gonderiler