# backend/app/

from flask import Blueprint, request, jsonify
from app.extensions import db
from flask import render_template
from app.models import StaffDevelopmentNeed, StaffDevelopmentRecord, Operator

bp = Blueprint('staff_dev', __name__, url_prefix='/api/staff-dev')



@bp.route('/', methods=['GET'])
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


# List operators
@bp.route('/operators', methods=['GET'])
def list_operators():
    operators = Operator.query.all()
    return jsonify([{'id': op.id, 'name': op.name} for op in operators])


# List development needs
@bp.route('/needs', methods=['GET'])
def list_needs():
    needs = StaffDevelopmentNeed.query.all()
    return jsonify([{'id': n.id, 'name': n.name} for n in needs])

# List staff development records
@bp.route('/records', methods=['GET'])
def list_records():
    recs = StaffDevelopmentRecord.query.all()
    return jsonify([{
        'id': rec.id,
        'operator_id': rec.operator_id,
        'need': rec.need.name,
        'date': rec.date.isoformat() if rec.date else None,
        'notes': rec.notes,
        'is_met': rec.is_met,
        'date_met': rec.date_met.isoformat() if rec.date_met else None
    } for rec in recs])

# Create a record
@bp.route('/records', methods=['POST'])
def create_record():
    data = request.get_json()
    rec = StaffDevelopmentRecord(
        operator_id = data['operator_id'],
        need_id     = data['need_id'],
        date        = data.get('date'),
        notes       = data.get('notes')
    )
    db.session.add(rec)
    db.session.commit()
    return jsonify({'message': 'Created', 'id': rec.id}), 201

# Update a record
@bp.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    rec = StaffDevelopmentRecord.query.get_or_404(id)
    data = request.get_json()
    rec.date    = data.get('date', rec.date)
    rec.notes   = data.get('notes', rec.notes)
    rec.is_met  = data.get('is_met', rec.is_met)
    rec.date_met = data.get('date_met', rec.date_met)
    db.session.commit()
    return jsonify({'message': 'Updated'})

# Delete a record
@bp.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    rec = StaffDevelopmentRecord.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
