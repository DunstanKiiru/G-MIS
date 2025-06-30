# backend/app/models/system_type.py

from app.extensions import db

class SystemType(db.Model):
    __tablename__ = 'system_types'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    water_systems = db.relationship('WaterSystem', back_populates='system_type')
