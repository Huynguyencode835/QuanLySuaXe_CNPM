import hashlib, json

from flask_login import current_user

from app.models.model import *
from app._init_ import create_app,db
from datetime import datetime, date

def countLimitVehicle():
    return ReceptionForm.query.filter(ReceptionForm.status == 3).count()

def limitVehicle():
    return db.session.query(SystemParameters).first().limitcar


def create_receptionForm(
        name,
        phonenumber,
        carnumber,
        appointment_date,
        description,
        veType_id,
        customer_id=None,
        staff_id=None
):
    receptionForm = ReceptionForm(
        name=name,
        phonenumber=phonenumber,
        carnumber=carnumber,
        appointment_date=appointment_date,
        description=description,
        veType_id=veType_id,
        customer_id=customer_id,
        staff_id=staff_id
    )

    if (current_user.is_authenticated and current_user.role.name == 'CUSTOMER'):
        receptionForm.customer_id = current_user.id

    if(current_user.is_authenticated and current_user.role.name == 'STAFF'):
        receptionForm.staff_id = current_user.id
        receptionForm.status = Form_status.WAIT_REPAIR

    db.session.add(receptionForm)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(countLimitVehicle())