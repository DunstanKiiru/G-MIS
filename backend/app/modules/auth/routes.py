from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.extensions import db, jwt
from app.models.user import User
import logging

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

logger = logging.getLogger(__name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'msg': 'Bad username or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

from werkzeug.security import generate_password_hash

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            return jsonify({'msg': 'Missing username or password'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'msg': 'Username already exists'}), 409

        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg': 'User created successfully'}), 201
    except Exception as e:
        logger.error(f"Error during registration: {e}")
        return jsonify({'msg': 'Internal server error'}), 500
