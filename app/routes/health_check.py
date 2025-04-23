### --- flask-boilerplate/app/routes/health_check.py ---
from flask import jsonify
from . import api_bp

@api_bp.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'ok',
        'message': 'API is healthy'
    }), 200
