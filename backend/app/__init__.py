from flask import Flask
from .config import Config
from .extensions import db,migrate
from .modules.water.routes import water_asset_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    app.register_blueprint(water_asset_bp, url_prefix="/api/assets")
    
    return app