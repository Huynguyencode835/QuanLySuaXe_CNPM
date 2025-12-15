from app.routes.api.appointment_api import appointment_api
from app.routes.api.reception_api import reception_api

def route_api(app):
    app.register_blueprint(appointment_api, url_prefix="/api/appointment")
    app.register_blueprint(reception_api, url_prefix="/api/receptions")
