from app.extensions import db

class Location(db.Model):
    __tablename__ = 'locations'
    
    id        = db.Column(db.Integer, primary_key=True)
    county    = db.Column(db.String(100), nullable=False)
    ward      = db.Column(db.String(100), nullable=False)
    latitude  = db.Column(db.Float)
    longitude = db.Column(db.Float)

    water_systems = db.relationship("WaterSystem", back_populates="location", cascade="all, delete-orphan")
