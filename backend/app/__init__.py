from flask import Flask
from app.extensions import db, migrate
from app.modules.water.routes import api
import os
from dotenv import load_dotenv
from app.modules.community_contributions.routes import bp as community_bp
from app.modules.om_visits.routes import bp as om_visits_bp
from app.modules.water_quality_tests.routes import bp as quality_bp
from app.modules.staff_development.routes import bp as staff_dev_bp

from app.modules.spare_parts_inventory.spare_parts_routes import bp as spare_parts_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api)
    app.register_blueprint(community_bp)
    app.register_blueprint(om_visits_bp)
    app.register_blueprint(quality_bp)
    app.register_blueprint(staff_dev_bp)
    app.register_blueprint(spare_parts_bp)

    return app
