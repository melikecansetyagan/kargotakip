import inspect
import json

from flask import request
from sqlalchemy import func

from db import db



def filtrele(vt_sinifi):
    sorgu = db.session.query(vt_sinifi)
    if 'sorgu' in request.args:
        talep = request.args['sorgu']
        talep_obj = json.loads(talep)

        alicinin_icinde_var_olanlar = dict(inspect.getmembers(vt_sinifi))

        for alan in talep_obj:
            if alan == "sirala":
                alanlar = talep_obj[alan].split(",")
        for s_alan in alanlar:
            if s_alan.startswith('-'):
                sorgu = sorgu.order_by(alicinin_icinde_var_olanlar[s_alan[1:]].desc())
            elif s_alan.startswith('+'):
                sorgu = sorgu.order_by(alicinin_icinde_var_olanlar[s_alan[1:]])
            else:
                sorgu = sorgu.order_by(alicinin_icinde_var_olanlar[s_alan])
        else:
            vt_alani = alicinin_icinde_var_olanlar[alan]
            deger = talep_obj[alan]
            if deger.startswith('>='):
                sorgu = sorgu.filter(vt_alani >= deger[2:])
            elif deger.startswith('>'):
                sorgu = sorgu.filter(vt_alani>deger[1:])
            else:
                sorgu = sorgu.filter(func.lower(vt_alani) == talep_obj[alan].lower())

    return sorgu


def filtrele(vt_sinifi):
    sorgu = db.session.query(vt_sinifi)
    if 'sorgu' in request.args:
        talep = request.args['sorgu']
        talep_obj = json.loads(talep)

        gondericinin_icinde_var_olanlar = dict(inspect.getmembers(vt_sinifi))

        for alan in talep_obj:
            if alan == "sirala":
                alanlar = talep_obj[alan].split(",")
        for s_alan in alanlar:
            if s_alan.startswith('-'):
                sorgu = sorgu.order_by(gondericinin_icinde_var_olanlar[s_alan[1:]].desc())
            elif s_alan.startswith('+'):
                sorgu = sorgu.order_by(gondericinin_icinde_var_olanlar[s_alan[1:]])
            else:
                sorgu = sorgu.order_by(gondericinin_icinde_var_olanlar[s_alan])
        else:
            vt_alani = gondericinin_icinde_var_olanlar[alan]
            deger = talep_obj[alan]
            if deger.startswith('>='):
                sorgu = sorgu.filter(vt_alani >= deger[2:])
            elif deger.startswith('>'):
                sorgu = sorgu.filter(vt_alani>deger[1:])
            else:
                sorgu = sorgu.filter(func.lower(vt_alani) == talep_obj[alan].lower())

    return sorgu


def filtrele(vt_sinifi):
    sorgu = db.session.query(vt_sinifi)
    if 'sorgu' in request.args:
        talep = request.args['sorgu']
        talep_obj = json.loads(talep)

        gonderinin_icinde_var_olanlar = dict(inspect.getmembers(vt_sinifi))

        for alan in talep_obj:
            if alan == "sirala":
                alanlar = talep_obj[alan].split(",")
        for s_alan in alanlar:
            if s_alan.startswith('-'):
                sorgu = sorgu.order_by(gonderinin_icinde_var_olanlar[s_alan[1:]].desc())
            elif s_alan.startswith('+'):
                sorgu = sorgu.order_by(gonderinin_icinde_var_olanlar[s_alan[1:]])
            else:
                sorgu = sorgu.order_by(gonderinin_icinde_var_olanlar[s_alan])
        else:
            vt_alani = gonderinin_icinde_var_olanlar[alan]
            deger = talep_obj[alan]
            if deger.startswith('>='):
                sorgu = sorgu.filter(vt_alani >= deger[2:])
            elif deger.startswith('>'):
                sorgu = sorgu.filter(vt_alani>deger[1:])
            else:
                sorgu = sorgu.filter(func.lower(vt_alani) == talep_obj[alan].lower())

    return sorgu