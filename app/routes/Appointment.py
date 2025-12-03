from app.controllers.AppointmentController import AppointmentController
from flask import Blueprint

appointment = AppointmentController()

appointment_bp = Blueprint('appointment_bp', __name__)

appointment_bp.add_url_rule('/', view_func=appointment.index)