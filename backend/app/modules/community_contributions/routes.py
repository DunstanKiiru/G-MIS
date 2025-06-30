# backend/app/routes/community_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import ContributionType, CommunityContribution
from flask import render_template



bp = Blueprint('community', __name__, url_prefix='/api/community')

# List all contribution types

# at top of file
from flask import render_template

@bp.route('/', methods=['GET'])
@jwt_required()
def ui_index():
    types         = ContributionType.query.all()
    water_systems = WaterSystem.query.all()
    contributions = CommunityContribution.query.all()
    return render_template(
        'community/index.html',
        types=types,
        water_systems=water_systems,
        contributions=contributions
    )
@bp.route('/types', methods=['GET'])
@jwt_required()

def list_types():
    types = ContributionType.query.all()
    return jsonify([{'id': t.id, 'name': t.name} for t in types])

# List all contributions
@bp.route('/contributions', methods=['GET'])
@jwt_required()
def list_contributions():
    recs = CommunityContribution.query.all()
    return jsonify([{
        'id': rec.id,
        'system_id': rec.water_system_id,
        'type': rec.type.name,
        'amount': float(rec.amount) if rec.amount is not None else None,
        'date_recorded': rec.date_recorded.isoformat()
    } for rec in recs])

# Create a contribution
@bp.route('/contributions', methods=['POST'])
@jwt_required()
def create_contribution():
    data = request.get_json()
    rec = CommunityContribution(
        water_system_id  = data['system_id'],
        contribution_type = data['contribution_type_id'],
        amount           = data.get('amount'),
        date_recorded    = data.get('date_recorded')
    )
    db.session.add(rec)
    db.session.commit()
    return jsonify({'message': 'Created', 'id': rec.id}), 201

# Update a contribution
@bp.route('/contributions/<int:id>', methods=['PUT'])
@jwt_required()
def update_contribution(id):
    rec = CommunityContribution.query.get_or_404(id)
    data = request.get_json()
    rec.amount        = data.get('amount', rec.amount)
    rec.date_recorded = data.get('date_recorded', rec.date_recorded)
    db.session.commit()
    return jsonify({'message': 'Updated'})

# Delete a contribution
@bp.route('/contributions/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_contribution(id):
    rec = CommunityContribution.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
