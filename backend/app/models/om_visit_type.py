# backend/app/models/om_visit_type.py

from app.extensions import db

class OMVisitType(db.Model):
    __tablename__ = 'om_visit_types'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
