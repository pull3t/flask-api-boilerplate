### --- flask-boilerplate/app/__init__.py ---
from flask import Flask
from .routes import api_bp
from .config import Config
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
from .extensions import db 

# db = SQLAlchemy()
load_dotenv() 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    return app