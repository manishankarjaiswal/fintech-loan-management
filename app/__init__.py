from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)
    jwt.init_app(app)

    from app.routes import auth, loan, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(loan.bp)
    app.register_blueprint(admin.bp)

    return app
