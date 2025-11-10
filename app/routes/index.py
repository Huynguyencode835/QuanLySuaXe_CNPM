from flask import Flask, render_template,Blueprint
from routes.components import components_bp
from routes.Transactions import Transaction_bp
from routes.site import site_bp

def route(app):
    app.register_blueprint(components_bp, url_prefix="/Dashboard")
    app.register_blueprint(Transaction_bp, url_prefix="/Transactions")
    app.register_blueprint(site_bp, url_prefix="/")



