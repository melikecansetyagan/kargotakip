from sqlalchemy import Column, Integer, String

from .db import db

class Gonderici(db.Model):
    __tablename__ = 'gonderici'

    Gondericiid = Column(Integer, primary_key=True)
    GondericiAd = Column(String)
    GondericiSoyad = Column(String)
    GondericiAdres = Column(String)
    GondericiTelefon = Column(String)

    def __repr__(self):
        return "Gonderici  Ad={}, Soyad={}, Adres={}, Telefon={}".format( self.GondericiAd, self.GondericiSoyad, self.GondericiAdres, self.GondericiTelefon)
