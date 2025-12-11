# import hashlib, json
# from app.models.model import *
# from app._init_ import create_app,db
#
# def create_receptionForm(carnumber, appointment_date, description, veType_id,customer_id,staff_id,**kwargs):
#     receptionForm = ReceptionForm(carnumber = carnumber,
#                                   appointment_date = appointment_date,
#                                   description = description,
#                                   veType_id = veType_id,
#                                   customer_id = customer_id,
#                                   staff_id = staff_id,)
#     db.session.add(receptionForm)