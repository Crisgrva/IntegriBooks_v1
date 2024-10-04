from flask import Flask
from .config import Config
from .database.db import init_db
from flask_cors import CORS
from flasgger import Swagger
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    init_db(app)

    Swagger(app)
    from .views import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
