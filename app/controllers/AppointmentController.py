from flask import Flask, render_template, request, jsonify
from app.middleware import authenticate
from app.middleware.authenticate import role_required
from app.models.model import UserRole
from app.dao import appointment_dao

class AppointmentController:
    # [GET] /components
    # @role_required(UserRole.CUSTOMER,UserRole.STAFF)
    def createFormAsCustomer(self):
        appointment_dao.create_receptionForm()

    def createFormAsStaff(self, name, phoneNumber):
        return 0

    def limitVehicle(self):
        count = appointment_dao.countLimitVehicle()
        limit = appointment_dao.limitVehicle()
        return jsonify({
            "count": count,
            "limit": limit,
            "isReached": (count+1 <= limit)
        })


    def index(self):
        # if(request.method == 'POST'):
        #     role = request.form.get('value')
        #     # form = appointment_dao.create_receptionForm(name=request.form.get('name'),
        #     #                                             request.form.get('name'))
        #
        #     if(role == 'customer'):
        #         self.createFormAsStaff()
        #     if(role == 'staff'):
        #         self.createFormAsStaff()
        #     else:
        #         pass
        return render_template("appointment.html", page="Đặt lịch sửa xe")
