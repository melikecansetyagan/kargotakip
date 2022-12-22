from sqlalchemy import Column, Integer, String

from .db import db

class Alici(db.Model):
    __tablename__ = 'alici'

    Aliciid = Column(Integer, primary_key=True)
    AliciAd = Column(String)
    AliciSoyad = Column(String)
    AliciAdres = Column(String)
    AliciTelefon = Column(String)

    def __repr__(self):
        return "Alici  Ad={}, Soyad={}, Adres={}, Telefon={}".format(self.AliciAd, self.AliciSoyad, self.AliciAdres, self.AliciTelefon)
