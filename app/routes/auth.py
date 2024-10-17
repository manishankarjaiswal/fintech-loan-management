from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from app.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if User.get_user_by_email(email):
        return jsonify({"message": "Email already registered"}), 400

    User.create_user(name, email, phone, password)
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(email, password)

    user = User.get_user_by_email(email)
    if not user or not User.check_password(user['password_hash'], password):
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user['_id']))
    refresh_token = create_refresh_token(identity=str(user['_id']))
    return jsonify(access_token=access_token, refresh_token=refresh_token, is_admin=user['is_admin']), 200

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200