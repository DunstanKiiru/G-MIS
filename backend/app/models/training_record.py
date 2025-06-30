# backend/app/models/training_record.py

from datetime import datetime
from app.extensions import db

class TrainingRecord(db.Model):
    __tablename__ = 'training_records'
    id            = db.Column(db.Integer, primary_key=True)
    operator_id   = db.Column(db.Integer, db.ForeignKey('operators.id'), nullable=False)
    training_type = db.Column(db.String(200), nullable=False)
    date_received = db.Column(db.Date, default=datetime.utcnow)

    operator      = db.relationship('Operator', back_populates='trainings')
