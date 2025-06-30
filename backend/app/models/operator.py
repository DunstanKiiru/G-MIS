# backend/app/models/operator.py

from app.extensions import db

class Operator(db.Model):
    __tablename__ = 'operators'
    id                  = db.Column(db.Integer, primary_key=True)
    water_system_id     = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    name                = db.Column(db.String(200))
    training_supported  = db.Column(db.Boolean, default=False)
    tariff_charged      = db.Column(db.Boolean, default=False)

    water_system        = db.relationship('WaterSystem', back_populates='operator')
    trainings           = db.relationship('TrainingRecord', back_populates='operator', cascade='all, delete-orphan')
    tariffs             = db.relationship('Tariff', back_populates='operator', cascade='all, delete-orphan')
    staff_development   = db.relationship('StaffDevelopmentRecord', back_populates='operator', cascade='all, delete-orphan')
