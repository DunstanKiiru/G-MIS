# backend/app/routes/om_visit_routes.py

from flask import Blueprint, request, jsonify
from app.extensions import db
from flask import render_template
from app.models import OMVisitType, OMVisit, WaterSystem

bp = Blueprint('om_visits', __name__, url_prefix='/api/om-visits')

# List visit types
@bp.route('/types', methods=['GET'])
def list_visit_types():
    types = OMVisitType.query.all()
    return jsonify([{'id': t.id, 'name': t.name} for t in types])


@bp.route('/', methods=['GET'])
def ui_index():
    types   = OMVisitType.query.all()
    systems = WaterSystem.query.all()
    visits  = OMVisit.query.all()
    return render_template(
        'om_visits/index.html',
        types=types,
        water_systems=systems,
        visits=visits
    )

# List visits
@bp.route('', methods=['GET'])
def list_visits():
    recs = OMVisit.query.all()
    return jsonify([{
        'id': rec.id,
        'system_id': rec.water_system_id,
        'type': rec.type.name,
        'visit_date': rec.visit_date.isoformat(),
        'notes': rec.notes
    } for rec in recs])

# Create visit
@bp.route('', methods=['POST'])
def create_visit():
    data = request.get_json()
    rec = OMVisit(
        water_system_id = data['system_id'],
        visit_type      = data['visit_type_id'],
        visit_date      = data.get('visit_date'),
        notes           = data.get('notes')
    )
    db.session.add(rec)
    db.session.commit()
    return jsonify({'message': 'Created', 'id': rec.id}), 201

# Update visit
@bp.route('/<int:id>', methods=['PUT'])
def update_visit(id):
    rec = OMVisit.query.get_or_404(id)
    data = request.get_json()
    rec.visit_date = data.get('visit_date', rec.visit_date)
    rec.notes      = data.get('notes', rec.notes)
    db.session.commit()
    return jsonify({'message': 'Updated'})

# Delete visit
@bp.route('/<int:id>', methods=['DELETE'])
def delete_visit(id):
    rec = OMVisit.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return jsonify({'message': 'Deleted'})

