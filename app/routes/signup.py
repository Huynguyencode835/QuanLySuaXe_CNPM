from app.controllers.signupController import SignupController
from flask import Blueprint

Signup = SignupController()

Signup_bp = Blueprint('signup_bp', __name__)

Signup_bp.add_url_rule('/', view_func=Signup.index)