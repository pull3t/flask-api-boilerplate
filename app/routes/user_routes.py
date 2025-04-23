### --- flask-boilerplate/app/routes/user_routes.py ---
from flask import request, jsonify
from . import api_bp
from app.services.user_services import (
    create_user, get_user, get_all_users,
    update_user, delete_user
)



@api_bp.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    try:
        user = create_user(username)
        return jsonify({'user_id': user.user_id, 'username': user.username}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 409

@api_bp.route('/users/<user_id>', methods=['GET'])
def read(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user_id': user.user_id, 'username': user.username})

@api_bp.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify([{'user_id': u.user_id, 'username': u.username} for u in users])

@api_bp.route('/users/<user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    new_username = data.get('username')
    if not new_username:
        return jsonify({'error': 'New username is required'}), 400
    try:
        user = update_user(user_id, new_username)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'user_id': user.user_id, 'username': user.username})
    except ValueError as e:
        return jsonify({'error': str(e)}), 409

@api_bp.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    if delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404
