from app.extensions import db

class StaffDevelopmentRecord(db.Model):
    __tablename__ = 'staff_development_records'

    id          = db.Column(db.Integer, primary_key=True)
    operator_id = db.Column(db.Integer, db.ForeignKey('operators.id'), nullable=False)
    need_id     = db.Column(db.Integer, db.ForeignKey('staff_development_needs.id'), nullable=False)
    is_met      = db.Column(db.Boolean, default=False, nullable=False)
    date_met    = db.Column(db.Date, nullable=False)
    date        = db.Column(db.Date, nullable=True)
    notes       = db.Column(db.Text, nullable=True)

    operator    = db.relationship('Operator', back_populates='staff_development')
    need        = db.relationship('StaffDevelopmentNeed', back_populates='records')
