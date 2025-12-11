import hashlib, json
from app.models.model import *
from app._init_ import create_app,db
from datetime import datetime, date

def countLimitVehicle():
    return ReceptionForm.query.filter(ReceptionForm.status == 3).count()

def limitVehicle():
    return db.session.query(SystemParameters).first().limitcar

def create_receptionForm(carnumber, appointment_date, description, veType_id,customer_id,staff_id,**kwargs):
    receptionForm = ReceptionForm(carnumber = carnumber,
                                  appointment_date = appointment_date,
                                  description = description,
                                  veType_id = veType_id,
                                  customer_id = customer_id,
                                  staff_id = staff_id,)
    db.session.add(receptionForm)

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(countLimitVehicle())