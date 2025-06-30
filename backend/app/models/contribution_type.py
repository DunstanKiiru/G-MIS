# backend/app/models/contribution_type.py

from app.extensions import db

class ContributionType(db.Model):
    __tablename__ = 'contribution_types'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
