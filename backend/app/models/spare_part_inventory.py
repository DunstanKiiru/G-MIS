# backend/app/models/spare_part_inventory.py

from app.extensions import db

class SparePartInventory(db.Model):
    __tablename__ = 'spare_part_inventories'
    id               = db.Column(db.Integer, primary_key=True)
    water_system_id  = db.Column(db.Integer, db.ForeignKey('water_systems.id'), nullable=False)
    part_type_id     = db.Column(db.Integer, db.ForeignKey('spare_part_types.id'), nullable=False)
    quantity         = db.Column(db.Integer, nullable=False, default=0)
    last_restocked   = db.Column(db.Date)

    water_system     = db.relationship('WaterSystem', back_populates='spare_part_inventories')
    part_type        = db.relationship('SparePartType')
