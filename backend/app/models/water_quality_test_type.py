from app.extensions import db

class WaterQualityTestType(db.Model):
    __tablename__ = 'water_quality_test_types'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    tests = db.relationship('WaterQualityTest', back_populates='test_type', cascade='all, delete-orphan')
