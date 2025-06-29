from flask import Flask
from app.extensions import db, migrate
from app.modules.water.routes import api
import os
from dotenv import load_dotenv
from .routes.community_routes    import bp as community_bp
from .routes.om_visit_routes     import bp as om_visits_bp
from .routes.water_quality_routes import bp as quality_bp
from .routes.staff_dev_routes    import bp as staff_dev_bp

from app.routes.spare_parts_routes   import bp as spare_parts_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api)

    return app
