from app.extensions import db
from datetime import datetime, timezone
datetime.now(timezone.utc)

class WaterAsset(db.Model):
    __tablename__ = 'water_assets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    asset_type = db.Column(db.String, nullable = False)
    installation_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    material = db.Column(db.String, nullable = False)
    capacity = db.Column(db.Float)
    location = db.Column(db.String, nullable = False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    status = db.Column(db.String)
    last_maintenance = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
