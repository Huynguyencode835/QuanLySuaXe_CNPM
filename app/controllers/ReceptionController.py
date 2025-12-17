import math

from flask import Flask, render_template, request, jsonify, current_app
from flask_login import current_user

from app._init_ import create_app
from app.dao import appointment_dao,dao, receptionform_dao
from app.models.model import Form_status
from app.utils import receptionform_util


class ReceptionController():
    # [GET] /components
    def index(self):
        page = request.args.get("page")
        pages = math.ceil(receptionform_dao.count_form() / current_app.config["PAGE_SIZE"])
        return render_template("receptions.html",
                               page="Phiếu đặt lịch",
                               data = receptionform_util.get_receptionform((request.args.get("status_name")),page),
                               state = receptionform_util.parse_state(),
                               Form_status=Form_status,
                               vehicleType = dao.load_vehicletype(),
                               pages = pages)

    def updata_form(self, id):
        id = id
        name=request.json.get("name")
        phone=request.json.get("phone")
        car=request.json.get("car")
        vehicle_type=request.json.get("vehicle_type")
        status=request.json.get("status")
        appointment_date=request.json.get("appointment_date")
        description=request.json.get("description")
        res =appointment_dao.update_appointment(id,name,phone,car,vehicle_type,status,appointment_date,description)
        if res:
            return jsonify({
                "message": "Cập nhật thông tin thành công",
                "category": "success"
            })
        else:
            return jsonify({
                "message": "Cập nhật không thành công",
                "category": "error"
            })

    def delete_form(self, id):
        res = appointment_dao.delete_appointment(id)
        if res:
            return jsonify({
                "message": "Xóa phiếu thành công",
                "category": "success"
            })
        else:
            return jsonify({
                "message":  "Xóa thất bại",
                "category": "error"
            })

