from app.extensions import db

class StaffDevelopmentNeed(db.Model):
    __tablename__ = 'staff_development_needs'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    records     = db.relationship('StaffDevelopmentRecord', back_populates='need', cascade='all, delete-orphan')
