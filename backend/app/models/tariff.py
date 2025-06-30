# backend/app/models/tariff.py

from app.extensions import db

class Tariff(db.Model):
    __tablename__ = 'tariffs'
    id             = db.Column(db.Integer, primary_key=True)
    operator_id    = db.Column(db.Integer, db.ForeignKey('operators.id'), nullable=False)
    for_domestic   = db.Column(db.Boolean, default=False)
    domestic_type  = db.Column(db.String(100))
    for_productive = db.Column(db.Boolean, default=False)
    productive_type= db.Column(db.String(100))

    operator       = db.relationship('Operator', back_populates='tariffs')
