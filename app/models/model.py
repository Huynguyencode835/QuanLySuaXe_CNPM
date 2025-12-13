import json,hashlib
from datetime import datetime
from app._init_ import db,create_app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum, Text, false
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from enum import Enum as RoleEnum

class UserRole(RoleEnum):
    CUSTOMER = 2
    STAFF = 3
    ACCOUNTANT = 4
    TECHNICK = 5
    ADMIN = 1

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)

    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    phonenumber = Column(String(150), nullable=True)
    avatar = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
    joined = Column(DateTime, default=datetime.now)
    active = Column(Boolean, default=True)
    reception_forms_as_customer = relationship(
        'ReceptionForm',
        foreign_keys='ReceptionForm.customer_id',
        backref='customer',
        lazy=True
    )
    reception_forms_as_staff = relationship(
        'ReceptionForm',
        foreign_keys='ReceptionForm.staff_id',
        backref='staff',
        lazy=True
    )
    repair_form= relationship(
        'RepairForm',
        foreign_keys='[RepairForm.technick_id]',
        backref='technick',
        lazy=True
    )
    receipts_as_customer = relationship(
        'Receipt',
        foreign_keys='[Receipt.customer_id]',
        backref='customer',
        lazy=True
    )
    receipts_as_accountant = relationship(
        'Receipt',
        foreign_keys='[Receipt.accountant_id]',
        backref='accountant',
        lazy=True
    )

class Vehicletype(Base):
    __tablename__ = "Vehicletype"
    components = relationship('Component', backref="vehicletype", lazy=True)
    reception_forms = relationship('ReceptionForm', backref="vehicletype", lazy=True)

class BrandVehicle(Base):
    __tablename__ = "BrandVehicle"
    reception_forms = relationship('Component', backref="brandvehicle", lazy=True)

class Component(Base):
    __tablename__ = "Component"
    name = Column(String(150), nullable=False)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="")
    vehicle_id = Column(Integer, ForeignKey(Vehicletype.id), nullable=False)
    brand_id = Column(Integer, ForeignKey(BrandVehicle.id), nullable=False)


class Form_status(RoleEnum):
    WAIT_APPROVAL = 1
    REFUSE = 2
    WAIT_REPAIR = 3
    UNDER_REPAIR = 4
    SUCCESS = 5

class ReceptionForm(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    phonenumber = Column(String(150), nullable=False)
    carnumber = Column(String(150), nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    appointment_date = Column(DateTime, default=datetime.now)
    description = Column(Text)
    status = Column(Enum(Form_status), default=Form_status.WAIT_APPROVAL)
    veType_id = Column(Integer, ForeignKey(Vehicletype.id), nullable=False)
    customer_id = Column(Integer, ForeignKey(User.id), nullable=True)
    staff_id = Column(Integer, ForeignKey(User.id), nullable=True)
    repair_forms = relationship('RepairForm', backref='reception_form', lazy=True)

class SystemParameters(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    VAT = Column(Float, default=0.0)
    limitcar=Column(Integer, default=30)

class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now)
    customer_id = Column(Integer, ForeignKey(User.id), nullable=False)
    accountant_id = Column(Integer, ForeignKey(User.id), nullable=False)
    repair_forms = relationship('RepairForm', backref='receipt', lazy=True)

class RepairForm(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(Text)
    technick_id = Column(Integer, ForeignKey(User.id), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    reception_form_id = Column(Integer, ForeignKey(ReceptionForm.id), nullable=False)
    components = relationship(
        'Component',
        secondary='repair_forms_components',
        backref='repair_forms',
        lazy=True
    )

class RepairForms_Components(db.Model):
    __tablename__ = "repair_forms_components"
    id_repair_form = Column(Integer, ForeignKey(RepairForm.id), nullable=False,primary_key=True)
    id_component = Column(Integer, ForeignKey(Component.id), nullable=False,primary_key=True)
    quantity = Column(Integer, default=1)
    cost = Column(Float, default=0.0)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        c1 = Vehicletype(name="Moto")
        c2 = Vehicletype(name="Oto")
        db.session.add_all([c1, c2])

        b1 = BrandVehicle(name="Honda")
        b2 = BrandVehicle(name="Yamaha")
        b3 = BrandVehicle(name="Toyota")
        b4 = BrandVehicle(name="Mercedes")
        db.session.add_all([b1, b2,b3,b4])

        with open("../data/component.json", encoding="utf-8") as f:
            components = json.load(f)

            for c in components:
                comp = Component(**c)
                db.session.add(comp)

        admin_pass = str(hashlib.md5(("admin").encode('utf-8')).hexdigest())
        new_admin = User(
            name="Quản trị viên",
            username="admin",
            password=admin_pass,
            avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfjno7hGrNNuPZwaFZ8U8Mhr_Yq39rzd_p0YN_HVYk6KFmMETjtgd9bwl0UhU6g4xDDGg&usqp=CAU",
            role=UserRole.ADMIN

        )

        new_customer = User(
            name="Customer",
            username="customer",
            password=str(hashlib.md5(("customer").encode('utf-8')).hexdigest()),
            avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfjno7hGrNNuPZwaFZ8U8Mhr_Yq39rzd_p0YN_HVYk6KFmMETjtgd9bwl0UhU6g4xDDGg&usqp=CAU",
            role=UserRole.CUSTOMER
        )

        new_staff = User(
            name="Staff",
            username="staff",
            password=str(hashlib.md5(("staff").encode('utf-8')).hexdigest()),
            avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfjno7hGrNNuPZwaFZ8U8Mhr_Yq39rzd_p0YN_HVYk6KFmMETjtgd9bwl0UhU6g4xDDGg&usqp=CAU",
            role=UserRole.STAFF
        )

        new_accountant = User(
            name="Accountant",
            username="accountant",
            password=str(hashlib.md5(("1").encode('utf-8')).hexdigest()),
            avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfjno7hGrNNuPZwaFZ8U8Mhr_Yq39rzd_p0YN_HVYk6KFmMETjtgd9bwl0UhU6g4xDDGg&usqp=CAU",
            role=UserRole.ACCOUNTANT
        )
        db.session.add_all([new_admin,new_customer, new_staff,new_accountant])
        db.session.add(SystemParameters(VAT=20, limitcar=30))
        db.session.commit()
