from flask import Blueprint, jsonify, request

from db import Gonderici, db
from serialization import GondericiSema
from utility import filtrele

gonderici_bp = Blueprint("gonderici_islemleri", __name__)

@gonderici_bp.route('/', methods=['GET'])
def tum_gondericiler():
    gondericiler = filtrele(Gonderici).all()
    sema = GondericiSema()
    return sema.dump(gondericiler, many=True)


@gonderici_bp.route('/sayfa/<int:kayit_sayisi>/<int:sayfa_no>')
def gonderici_sayfa(kayit_sayisi, sayfa_no):
    sayfa_no -= 1

    atlanacak_kayit_sayisi = sayfa_no * kayit_sayisi
    getirilecek_kayit_sayisi = kayit_sayisi

    gondericiler = filtrele(Gonderici).limit(getirilecek_kayit_sayisi).offset(atlanacak_kayit_sayisi).all()

    sema = GondericiSema()
    return sema.dump(gondericiler, many=True)


@gonderici_bp.route('/sayfa/<int:kayit_sayisi>')
def gonderici_sayfa_sayisi(kayit_sayisi):
    gonderici_sayisi = filtrele(db.session.query(Gonderici), Gonderici).count()

    sayfa_sayisi = gonderici_sayisi // kayit_sayisi

    if gonderici_sayisi % kayit_sayisi > 0:
        sayfa_sayisi += 1
        return jsonify({
            'kayit_sayisi': gonderici_sayisi,
            'sayfa_sayisi': sayfa_sayisi
        })


@gonderici_bp.route('/<int:id>', methods=['GET'])
def gonderici_detay(id):
    gonderici = db.get_or_404(Gonderici, id)
    sema =GondericiSema()
    return sema.dump(gonderici)

@gonderici_bp.route('/', methods=['POST'])
def gonderici_ekle():
    gonderici_bilgileri = request.json
    gonderici = Gonderici(**gonderici_bilgileri)
    db.session.add(gonderici)
    db.session.commit()
    sema = GondericiSema()
    return sema.dump(gonderici)

@gonderici_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def gonderici_guncelle(id):
    gonderici = db.session.query(Gonderici).filter(Gonderici.id==id).one_or_none()
    yeni_gonderici_bilgileri = request.json
    sema = GondericiSema
    yeni_gonderici = sema.load(yeni_gonderici_bilgileri, instance=gonderici, session=db.session)
    db.session.commit()
    return sema.dump(yeni_gonderici)

@gonderici_bp.route('/<int:id>', methods=['DELETE'])
def gonderici_sil(id):
    gonderici =db.get_or_404(Gonderici, id)
    db.session.delete(gonderici)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
