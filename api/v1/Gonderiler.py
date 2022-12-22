from flask import Blueprint, request, jsonify

from db import Gonderiler, db
from serialization import GonderilerSema
from utility import filtrele

gonderi_bp = Blueprint("gonderi_islemleri", __name__)

@gonderi_bp.route('/', methods=['GET'])
def tum_gonderiler():
    gonderiler = filtrele(Gonderiler).all()
    sema = GonderilerSema()
    return sema.dump(gonderiler, many=True)


@gonderi_bp.route('/sayfa/<int:kayit_sayisi>/<int:sayfa_no>')
def gonderiler_sayfa(kayit_sayisi, sayfa_no):
    sayfa_no -= 1

    atlanacak_kayit_sayisi = sayfa_no * kayit_sayisi
    getirilecek_kayit_sayisi = kayit_sayisi

    gonderiler = filtrele(Gonderiler).limit(getirilecek_kayit_sayisi).offset(atlanacak_kayit_sayisi).all()

    sema = GonderilerSema()
    return sema.dump(gonderiler, many=True)


@gonderi_bp.route('/sayfa/<int:kayit_sayisi>')
def gonderi_sayfa_sayisi(kayit_sayisi):
    gonderi_sayisi = filtrele(db.session.query(Gonderiler), Gonderiler).count()

    sayfa_sayisi = gonderi_sayisi // kayit_sayisi

    if gonderi_sayisi % kayit_sayisi > 0:
        sayfa_sayisi += 1
        return jsonify({
            'kayit_sayisi': gonderi_sayisi,
            'sayfa_sayisi': sayfa_sayisi
        })


@gonderi_bp.route('/<int:id>', methods=['GET'])
def gonderi_detay(id):
    gonderi = db.get_or_404(Gonderiler, id)
    sema = GonderilerSema()
    return sema.dump(gonderi)


@gonderi_bp.route('/', methods=['POST'])
def gonderi_ekle():
    gonderi_bilgileri = request.json
    gonderi = Gonderiler(**gonderi_bilgileri)
    db.session.add(gonderi)
    db.session.commit()
    sema = GonderilerSema()
    return sema.dump(gonderi)

@gonderi_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def gonderi_guncelle(id):
    gonderi = db.session.query(Gonderiler).filter(Gonderiler.id==id).one_or_none()
    yeni_gonderi_bilgileri = request.json
    sema = GonderilerSema
    yeni_gonderi = sema.load(yeni_gonderi_bilgileri, instance=gonderi, session=db.session)
    db.session.commit()
    return sema.dump(yeni_gonderi)

@gonderi_bp.route('/<int:id>', methods=['DELETE'])
def gonderi_sil(id):
    gonderi =db.get_or_404(Gonderiler, id)
    db.session.delete(gonderi)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})

