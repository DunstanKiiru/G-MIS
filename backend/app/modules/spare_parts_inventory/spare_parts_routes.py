from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import SparePartType, SparePartInventory, WaterSystem
from datetime import datetime

bp = Blueprint('spare_parts', __name__, url_prefix='/spare-parts')

# =====================
# UI ROUTES
# =====================

@bp.route('/')
@jwt_required()
def ui_index():
    types   = SparePartType.query.all()
    systems = WaterSystem.query.all()
    inv     = SparePartInventory.query.all()
    return render_template('spare_parts/index.html',
                           types=types,
                           water_systems=systems,
                           inventory=inv)

@bp.route('/create', methods=['POST'])
@jwt_required()
def create_inv():
    data = request.form
    rec = SparePartInventory(
        water_system_id = data['system_id'],
        part_type_id    = data['part_type_id'],
        quantity        = data.get('quantity', 0),
        last_restocked  = data.get('last_restocked')
    )
    db.session.add(rec)
    db.session.commit()
    return redirect(url_for('spare_parts.ui_index'))

@bp.route('/<int:id>/edit', methods=['POST'])
@jwt_required()
def update_inv(id):
    rec = SparePartInventory.query.get_or_404(id)
    data = request.form
    rec.water_system_id = data['system_id']
    rec.part_type_id    = data['part_type_id']
    rec.quantity        = data.get('quantity', rec.quantity)
    rec.last_restocked  = data.get('last_restocked', rec.last_restocked)
    db.session.commit()
    return redirect(url_for('spare_parts.ui_index'))

@bp.route('/<int:id>/delete', methods=['POST'])
@jwt_required()
def delete_inv(id):
    rec = SparePartInventory.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return redirect(url_for('spare_parts.ui_index'))


# =====================
# API ROUTES
# =====================

@bp.route('/api/spare-parts/types', methods=['GET'])
def api_get_types():
    types = SparePartType.query.all()
    return jsonify([{
        "id": t.id,
        "name": t.name
    } for t in types])

@bp.route('/api/spare-parts/inventory', methods=['GET'])
def api_get_inventory():
    inventory = SparePartInventory.query.all()
    return jsonify([{
        "id": i.id,
        "part_type_id": i.part_type_id,
        "part_type": i.part_type.name,
        "water_system_id": i.water_system_id,
        "water_system": i.water_system.name,
        "quantity": i.quantity,
        "last_restocked": i.last_restocked.isoformat() if i.last_restocked else None
    } for i in inventory])

@bp.route('/api/spare-parts/inventory/<int:id>', methods=['DELETE'])
def api_delete_inventory(id):
    record = SparePartInventory.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Spare part deleted"})

@bp.route('/api/watersystems', methods=['GET'])
def api_get_watersystems():
    systems = WaterSystem.query.all()
    return jsonify([{
        "id": s.id,
        "name": s.name
    } for s in systems])
