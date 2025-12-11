from app.routes.api.appointment_api import appointment_api

def route_api(app):
    app.register_blueprint(appointment_api, url_prefix="/api/appointment")