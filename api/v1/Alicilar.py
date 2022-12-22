from flask import Blueprint, request, jsonify

from db import db, Alici
from serialization import AliciSema
from utility import filtrele

alici_bp = Blueprint("alici_islemleri", __name__)

@alici_bp.route('/', methods=['GET'])
def tum_alicilar():
    alicilar = filtrele(Alici).all()
    sema = AliciSema()
    return sema.dump(alicilar, many=True)


@alici_bp.route('/sayfa/<int:kayit_sayisi>/<int:sayfa_no>')
def alici_sayfa(kayit_sayisi, sayfa_no):
    sayfa_no -= 1

    atlanacak_kayit_sayisi = sayfa_no * kayit_sayisi
    getirilecek_kayit_sayisi = kayit_sayisi

    alicilar = filtrele(Alici).limit(getirilecek_kayit_sayisi).offset(atlanacak_kayit_sayisi).all()

    sema = AliciSema()
    return sema.dump(alicilar, many=True)


@alici_bp.route('/sayfa/<int:kayit_sayisi>')
def alici_sayfa_sayisi(kayit_sayisi):
    alici_sayisi = filtrele(db.session.query(Alici), Alici).count()

    sayfa_sayisi = alici_sayisi // kayit_sayisi

    if alici_sayisi % kayit_sayisi > 0:
        sayfa_sayisi += 1
        return jsonify({
            'kayit_sayisi': alici_sayisi,
            'sayfa_sayisi': sayfa_sayisi
        })

@alici_bp.route('/<int:id>', methods=['GET'])
def alici_detay(id):
    alici = db.get_or_404(Alici, id)
    sema =AliciSema()
    return sema.dump(alici)

@alici_bp.route('/', methods=['POST'])
def alici_ekle():
    alici_bilgileri = request.json
    alici = Alici(**alici_bilgileri)
    db.session.add(alici)
    db.session.commit()
    sema = AliciSema()
    return sema.dump(alici)

@alici_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def alici_guncelle(id):
    alici = db.session.query(Alici).filter(Alici.id==id).one_or_none()
    yeni_alici_bilgileri = request.json
    sema = AliciSema
    yeni_alici = sema.load(yeni_alici_bilgileri, instance=alici, session=db.session)
    db.session.commit()
    return sema.dump(yeni_alici)

@alici_bp.route('/<int:id>', methods=['DELETE'])
def alici_sil(id):
    alici =db.get_or_404(Alici, id)
    db.session.delete(alici)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
#app.register_blueprint(alici_bp, url_prefix="/api/1/alicilar")

