from app.extensions import db

class WaterQualityTest(db.Model):
    __tablename__ = 'water_quality_tests'
    id           = db.Column(db.Integer, primary_key=True)
    system_id    = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    test_type_id = db.Column(db.Integer, db.ForeignKey('water_quality_test_types.id'), nullable=False)  # renamed
    test_date    = db.Column(db.Date, nullable=True)
    value        = db.Column(db.Float, nullable=True)

    system    = db.relationship('WaterSystem', back_populates='quality_tests')
    test_type = db.relationship('WaterQualityTestType', back_populates='tests')
