import hashlib, json
from app.models.model import Vehicletype, BrandVehicle, User, Component, UserRole, RepairForm, ReceptionForm
from app._init_ import create_app,db
from sqlalchemy import or_

def load_vehicletype():
    # with open("data/category.json", 'r', encoding='utf-8') as f:
    #     return json.load(f)
    return Vehicletype.query.all()

def load_brandveghicle():
    return BrandVehicle.query.all()

def load_component(q=None, vehicle_id=None, brand_id=None):
    # with open("data/component.json", 'r', encoding='utf-8') as f:
    #     component = json.load(f)
    #     if q:
    #         component = [c for c in component if c["name"].find(q)>=0]
    #     if vehicle_id:
    #         component = [c for c in component if c["cate_id"].__eq__(int(vehicle_id))]
    #     if brand_id:
    #         component = [c for c in component if c["brand_id"].__eq__(int(brand_id))]
    #     return component
    query = Component.query
    if q:
        query = query.filter(Component.name.contains(q))

    if vehicle_id:
        query = query.filter(Component.vehicle_id.__eq__(int(vehicle_id)))

    if brand_id:
        query = query.filter(Component.brand_id.__eq__(int(brand_id)))

    return query.all()

def add_user(name, phonenumber,username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(),
                phonenumber=phonenumber.strip(),
                username=username.strip(),
                password=password,
                avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

# lấy phiếu sửa chữa
def get_repair_form():
    return RepairForm.query.all()

# Lấy phiếu tiếp nhận
def get_reception_form():
    return ReceptionForm.query.all()


def load_repairform_receptionform(q=None):
    query = RepairForm.query.join(ReceptionForm)
    if q:
        query = query.filter(or_(ReceptionForm.name.contains(q),
                                 ReceptionForm.phonenumber.contains(q),
                                 ReceptionForm.carnumber.contains(q)))
    return query.all()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(get_repair_form())
        print(get_reception_form())

