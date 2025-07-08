from flask import Flask, jsonify
from app.extensions import db, migrate, jwt
from app.modules.water.routes import api
import os
from dotenv import load_dotenv
from app.modules.community_contributions.routes import bp as community_bp
from app.modules.om_visits.routes import bp as om_visits_bp
from app.modules.water_quality_tests.routes import bp as quality_bp
from app.modules.staff_development.routes import bp as staff_dev_bp

from app.modules.spare_parts_inventory.spare_parts_routes import bp as spare_parts_bp

from flask_cors import CORS

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')
    app.config['JWT_TOKEN_LOCATION'] = ['headers']

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        app.logger.error(f"JWT unauthorized error: {callback}")
        return jsonify({
            'error': 'Authorization required',
            'description': 'Request does not contain an access token.'
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_response(callback):
        app.logger.error(f"JWT invalid token error: {callback}")
        return jsonify({
            'error': 'Invalid token',
            'description': 'Signature verification failed.'
        }), 422

    @jwt.expired_token_loader
    def expired_token_response(jwt_header, jwt_payload):
        app.logger.error("JWT token expired error")
        return jsonify({
            'error': 'Token expired',
            'description': 'The token has expired.'
        }), 401

    from app.modules.auth.routes import bp as auth_bp

    app.register_blueprint(api)
    app.register_blueprint(community_bp)
    app.register_blueprint(om_visits_bp)
    app.register_blueprint(quality_bp)
    app.register_blueprint(staff_dev_bp)
    app.register_blueprint(spare_parts_bp)
    app.register_blueprint(auth_bp)

    return app
