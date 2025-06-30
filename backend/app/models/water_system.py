# backend/app/models/water_system.py

from app.extensions import db

class WaterSystem(db.Model):
    __tablename__ = 'water_systems'
    id                   = db.Column(db.Integer, primary_key=True)
    unique_id            = db.Column(db.String(50), unique=True, nullable=False)
    name                 = db.Column(db.String(200), nullable=False)
    type_id              = db.Column(db.Integer, db.ForeignKey('system_types.id'))
    status_id            = db.Column(db.Integer, db.ForeignKey('operational_statuses.id'))
    location_id          = db.Column(db.Integer, db.ForeignKey('locations.id'))

    system_type          = db.relationship('SystemType', back_populates='water_systems')
    status               = db.relationship('OperationalStatus', back_populates='water_systems')
    location             = db.relationship('Location', back_populates='water_systems')
    operator             = db.relationship('Operator', uselist=False, back_populates='water_system')
    funding_sources      = db.relationship('FundingSource', back_populates='water_system', cascade='all, delete-orphan')
    community_contributions = db.relationship('CommunityContribution', back_populates='water_system', cascade='all, delete-orphan')
    om_visits            = db.relationship('OMVisit', back_populates='water_system', cascade='all, delete-orphan')
    spare_part_inventories = db.relationship('SparePartInventory', back_populates='water_system', cascade='all, delete-orphan')
    quality_tests        = db.relationship('WaterQualityTest', back_populates='system', cascade='all, delete-orphan')
