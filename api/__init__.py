from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import psycopg2
from flask_cors import CORS

db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
jwt = JWTManager()



def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    from api.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    
    CORS(app)
    
    return app

app=create_app()

from api import models