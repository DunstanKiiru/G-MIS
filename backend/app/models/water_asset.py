from app.extensions import db
from datetime import datetime, timezone

class WaterAsset(db.Model):
    __tablename__ = 'water_assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    asset_type = db.Column(db.String(50), nullable=False)
    installation_date = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    material = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    last_maintenance = db.Column(
        db.DateTime,
        nullable=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "asset_type": self.asset_type,
            "installation_date": self.installation_date.isoformat(),
            "material": self.material,
            "capacity": self.capacity,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "status": self.status,
            "last_maintenance": self.last_maintenance.isoformat() if self.last_maintenance else None,
        }
    