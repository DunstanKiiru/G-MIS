# backend/app/models/operational_status.py

from app.extensions import db

class OperationalStatus(db.Model):
    __tablename__ = 'operational_statuses'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    water_systems = db.relationship('WaterSystem', back_populates='status')
