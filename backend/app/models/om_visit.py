# backend/app/models/om_visit.py

from app.extensions import db

class OMVisit(db.Model):
    __tablename__ = 'om_visits'
    id               = db.Column(db.Integer, primary_key=True)
    water_system_id  = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    visit_type       = db.Column(db.Integer, db.ForeignKey('om_visit_types.id'), nullable=False)
    visit_date       = db.Column(db.Date, nullable=False)
    notes            = db.Column(db.Text)

    water_system     = db.relationship('WaterSystem', back_populates='om_visits')
    type             = db.relationship('OMVisitType')
