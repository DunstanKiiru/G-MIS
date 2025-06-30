# backend/app/

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from flask import render_template
from app.models import StaffDevelopmentNeed, StaffDevelopmentRecord

bp = Blueprint('staff_dev', __name__, url_prefix='/api/staff-dev')


@bp.route('/', methods=['GET'])
@jwt_required()
def ui_index():
    needs     = StaffDevelopmentNeed.query.all()
    operators = Operator.query.all()
    records   = StaffDevelopmentRecord.query.all()
    return render_template(
        'staff_dev/index.html',
        needs=needs,
        operators=operators,
        records=records
    )

# List development needs
@bp.route('/needs', methods=['GET'])
@jwt_required()
def list_needs():
    needs = StaffDevelopmentNeed.query.all()
    return jsonify([{'id': n.id, 'name': n.name} for n in needs])

# List staff development records
@bp.route('/records', methods=['GET'])
@jwt_required()
def list_records():
    recs = StaffDevelopmentRecord.query.all()
    return jsonify([{
        'id': rec.id,
        'operator_id': rec.operator_id,
        'need': rec.need.name,
        'is_met': rec.is_met,
        'date_met': rec.date_met.isoformat() if rec.date_met else None
    } for rec in recs])

# Create a record
@bp.route('/records', methods=['POST'])
@jwt_required()
def create_record():
    data = request.get_json()
    rec = StaffDevelopmentRecord(
        operator_id = data['operator_id'],
        need_id     = data['need_id'],
        is_met      = data.get('is_met', False),
        date_met    = data.get('date_met')
    )
    db.session.add(rec)
    db.session.commit()
    return jsonify({'message': 'Created', 'id': rec.id}), 201

# Update a record
@bp.route('/records/<int:id>', methods=['PUT'])
@jwt_required()
def update_record(id):
    rec = StaffDevelopmentRecord.query.get_or_404(id)
    data = request.get_json()
    rec.is_met   = data.get('is_met', rec.is_met)
    rec.date_met = data.get('date_met', rec.date_met)
    db.session.commit()
    return jsonify({'message': 'Updated'})

# Delete a record
@bp.route('/records/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_record(id):
    rec = StaffDevelopmentRecord.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
