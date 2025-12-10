from flask import Flask, render_template
from app.middleware import authenticate
from app.middleware.authenticate import role_required
from app.models.model import UserRole


class AppointmentController:

    # [GET] /components
    # Chỉ CUSTOMER (role = 2)(CUSTOMER) mới được đặt lịch
    @role_required(UserRole.CUSTOMER,UserRole.STAFF)
    def index(self):
        return render_template("appointment.html", page="Đặt lịch sửa xe")
