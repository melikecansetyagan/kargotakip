from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .db import db
from .AliciModel import Alici
from .GondericiModel import Gonderici

class Gonderiler(db.Model):
    __tablename__ = 'gonderiler'

    Gonderiid = Column(Integer, primary_key=True)
    Aliciid = Column(Integer, ForeignKey('alici.Aliciid'))
    Gondericiid = Column(Integer, ForeignKey('gonderici.Gondericiid'))
    TahminiTeslimZamani = Column(String)
    GonderiOdemeSekli = Column(String)

    alici = relationship("alici", back_populates="Gonderiler")
    gonderici = relationship("gonderici", back_populates="Gonderiler")

    def __repr__(self):
        return "gonderiler  Aliciid={} ,Gondericiid={},TahminiTeslimZamani={}, GonderiOdemeSekli={}".format(self.Aliciid, self.Gondericiid, self.TahminiTeslimZamani, self.GonderiOdemeSekli)


Alici.gonderiler = relationship("Gonderiler", order_by=Gonderiler.Gonderiid, back_populates="alici")
Gonderici.gonderiler = relationship("Gonderiler", order_by=Gonderiler.Gonderiid, back_populates="gonderici")
