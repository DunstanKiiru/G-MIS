from flask import Blueprint, request, render_template, redirect, url_for
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import SparePartType, SparePartInventory, WaterSystem

bp = Blueprint('spare_parts', __name__, url_prefix='/spare-parts')

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
    db.session.add(rec); db.session.commit()
    return redirect(url_for('spare_parts.ui_index'))

@bp.route('/<int:id>/edit', methods=['POST'])
@jwt_required()
def update_inv(id):
    rec  = SparePartInventory.query.get_or_404(id)
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
    db.session.delete(rec); db.session.commit()
    return redirect(url_for('spare_parts.ui_index'))
