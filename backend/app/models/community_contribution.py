from app.extensions import db
from .water_system import WaterSystem
from .contribution_type import ContributionType

class CommunityContribution(db.Model):
    __tablename__ = 'community_contributions'
    id                = db.Column(db.Integer, primary_key=True)
    water_system_id   = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    contribution_type = db.Column(db.Integer, db.ForeignKey('contribution_types.id'), nullable=False)
    amount            = db.Column(db.Numeric)
    date_recorded     = db.Column(db.Date, nullable=False)

    water_system      = db.relationship('WaterSystem', back_populates='community_contributions')
    contribution_type_rel = db.relationship('ContributionType') 