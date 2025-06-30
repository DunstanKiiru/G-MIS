# backend/app/models/funding_source.py

from app.extensions import db

class FundingSource(db.Model):
    __tablename__ = 'funding_sources'
    id               = db.Column(db.Integer, primary_key=True)
    water_system_id  = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    source_type      = db.Column(db.String(100), nullable=False)  # e.g. “O&M”, “Capital”
    description      = db.Column(db.Text)

    water_system     = db.relationship('WaterSystem', back_populates='funding_sources')
