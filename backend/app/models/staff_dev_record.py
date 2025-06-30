from app.extensions import db

class StaffDevelopmentRecord(db.Model):
    __tablename__ = 'staff_development_records'
    id          = db.Column(db.Integer, primary_key=True)
    operator_id = db.Column(db.Integer, nullable=False)
    need_id     = db.Column(db.Integer, nullable=False)
    date        = db.Column(db.Date, nullable=True)
    notes       = db.Column(db.Text, nullable=True)
