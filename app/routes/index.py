from flask import Flask, render_template,Blueprint
from routes.components import components_bp
from routes.site import site_bp

def route(app):
    app.register_blueprint(components_bp, url_prefix="/components")
    app.register_blueprint(site_bp, url_prefix="/")



