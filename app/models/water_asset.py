from app.extensions import db
from datetime import datetime

class WaterAsset(db.model):
    __tablename__ = 'water_assets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    asset_type = db.Column(db.String, nullable = False)