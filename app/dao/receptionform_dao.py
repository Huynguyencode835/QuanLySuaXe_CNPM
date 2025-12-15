from flask import request
from flask_login import current_user
from flask_sqlalchemy import query

from app.models.model import *
from app._init_ import create_app,db
from datetime import datetime, date

def receptionFormCustomer(id, status=None):
    return (ReceptionForm.query.filter(ReceptionForm.customer_id == id, ReceptionForm.status == status).all()
            if status
            else ReceptionForm.query.filter(ReceptionForm.customer_id == id).all())


def receptionFormUserState(Form_status):
    return ReceptionForm.query.filter(ReceptionForm.status.__eq__(Form_status)).all()

def load_receptionForm():
    return ReceptionForm.query.all()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(receptionFormCustomer(2))