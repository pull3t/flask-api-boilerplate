### --- flask-boilerplate/app/routes/__init__.py ---
from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import health_check
from . import user_routes
