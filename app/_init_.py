from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

db = SQLAlchemy()
login_manager = LoginManager()


cloudinary.config(
    cloud_name= 'dkatgavs4',
    api_key='769513968994667',
    api_secret= 'oNIu8AMfcmwLlkhANlyCYXI40B0'
)

def create_app():
    app = Flask(__name__)

    app.secret_key = "asjdahjgưGƯEGgG4252#adsd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Abc123@localhost/app?charset=utf8mb4"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager.init_app(app)

    @app.context_processor
    def inject_cart_stats():
        import app.models.dao as dao
        cart = session.get('cart', {})
        return {'cart_stats': dao.count_cart(cart)}


    return app
