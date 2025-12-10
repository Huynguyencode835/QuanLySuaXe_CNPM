import hashlib, json
from app.models.model import Vehicletype,BrandVehicle,User,Component,UserRole
from app._init_ import create_app,db

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

def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def check_login(username, password,role=UserRole.CUSTOMER):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password.strip())).first()


def count_cart(cart):
    total_quantity, total_amount = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(load_component())
