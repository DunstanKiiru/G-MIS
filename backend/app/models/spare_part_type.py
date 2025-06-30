# backend/app/models/spare_part_type.py

from app.extensions import db

class SparePartType(db.Model):
    __tablename__ = 'spare_part_types'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    unit = db.Column(db.String(50))   # e.g. ‘pcs’, ‘meters’
