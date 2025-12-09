from flask import Flask, render_template,Blueprint
from app.routes.Components import components_bp
from app.routes.Transactions import Transaction_bp
from app.routes.Signup import Signup_bp
from app.routes.Site import site_bp
from app.routes.Appointment import appointment_bp
from app.routes.Receptions import receptions_bp


def route(app):
    app.register_blueprint(components_bp, url_prefix="/components")
    app.register_blueprint(Signup_bp, url_prefix="/signin")
    app.register_blueprint(Transaction_bp, url_prefix="/transactions")
    app.register_blueprint(appointment_bp, url_prefix="/appointment")
    app.register_blueprint(receptions_bp, url_prefix="/receptions")
    app.register_blueprint(site_bp, url_prefix="/")



