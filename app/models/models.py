import json
from datetime import datetime
from app._init_ import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from enum import Enum as RoleEnum

class UserRole(RoleEnum):
    CUSTOMER = 1
    STAFF = 2
    ACCOUNTANT = 3
    TECHNICK = 4
    ADMIN = 5

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
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
        backref='technick',
        lazy=True
    )
    receipts = relationship(
        'Receipt',
        backref='customer',
        lazy=True
    )

class Vehicletype(Base):
    components = relationship('Component', backref="vehicletype", lazy=True)
    reception_forms = relationship('ReceptionForm', backref="vehicletype", lazy=True)

class Component(Base):
    price = Column(Float, default=0.0)
    image = Column(String(300),default="https://res.cloudinary.com/dy1unykph/image/upload/v1741254148/aa0aawermmvttshzvjhc.png")
    description = Column(Text)
    veType_id = Column(Integer, ForeignKey(Vehicletype.id), nullable=False)

class Form_status(RoleEnum):
    WAIT_APPROVAL = 1
    REFUSE = 2
    WAIT_REPAIR = 3
    UNDER_REPAIR = 4
    SUCCESS = 5

class ReceptionForm(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    carnumber = Column(String(150), nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    description = Column(Text)
    status = Column(Enum(Form_status), default=Form_status.WAIT_APPROVAL)
    veType_id = Column(Integer, ForeignKey(Vehicletype.id), nullable=False)
    customer_id = Column(Integer, ForeignKey(User.id), nullable=False)
    staff_id = Column(Integer, ForeignKey(User.id), nullable=True)

class SystemParameters(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    VAT = Column(Float, default=0.0)
    limitcar=Column(Integer, default=30)

class Receipt(Base):
    created_date = Column(DateTime, default=datetime.now)
    customer_id = Column(Integer, ForeignKey(User.id), nullable=False)
    sys_id = Column(Integer, ForeignKey(SystemParameters.id), nullable=False)
    repair_forms = relationship('RepairForm', backref='receipt', lazy=True)

class RepairForm(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(Text)
    cost = Column(Float, default=0.0)
    technick_id = Column(Integer, ForeignKey(User.id), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    components = relationship(
        'Component',
        secondary='repair_forms_components',
        backref='repair_forms',
        lazy=True
    )

class RepairForms_Components(db.Model):
    id_repair_form = Column(Integer, ForeignKey(RepairForm.id), nullable=False,primary_key=True)
    id_component = Column(Integer, ForeignKey(Component.id), nullable=False,primary_key=True)
    quantity = Column(Integer, default=1)

if __name__=="__main__":
    with app.app_context():
        db.create_all()


