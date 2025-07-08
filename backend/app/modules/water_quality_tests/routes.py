# backend/app/routes/water_quality_routes.py

from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import WaterQualityTestType, WaterQualityTest,WaterSystem
from flask import render_template

bp = Blueprint('water_quality', __name__, url_prefix='/api/quality-tests')


@bp.route('/', methods=['GET'])

def ui_index():
    types   = WaterQualityTestType.query.all()
    systems = WaterSystem.query.all()
    tests   = WaterQualityTest.query.all()
    return render_template(
        'quality_tests/index.html',
        types=types,
        water_systems=systems,
        tests=tests
    )

# List test types
@bp.route('/types', methods=['GET'])
def list_test_types():
    types = WaterQualityTestType.query.all()
    return jsonify([{'id': t.id, 'name': t.name} for t in types])

# List test records
@bp.route('', methods=['GET'])
def list_tests():
    recs = WaterQualityTest.query.all()
    return jsonify([{
        'id': rec.id,
        'system': rec.system.name,
        'type': rec.test_type.name,
        'test_date': rec.test_date.isoformat(),
        'value': rec.value
    } for rec in recs])

# Create test record
@bp.route('', methods=['POST'])
def create_test():
    data = request.get_json()
    rec = WaterQualityTest(
        system_id = data['system_id'],
        test_type_id = data['test_type_id'],
        test_date = data.get('test_date'),
        value     = data.get('value')
    )
    db.session.add(rec)
    db.session.commit()
    return jsonify({'message': 'Created', 'id': rec.id}), 201

# Update test record
@bp.route('/<int:id>', methods=['PUT'])
def update_test(id):
    rec = WaterQualityTest.query.get_or_404(id)
    data = request.get_json()
    rec.test_date = data.get('test_date', rec.test_date)
    rec.value     = data.get('value', rec.value)
    db.session.commit()
    return jsonify({'message': 'Updated'})

# Delete test record
@bp.route('/<int:id>', methods=['DELETE'])
def delete_test(id):
    rec = WaterQualityTest.query.get_or_404(id)
    db.session.delete(rec)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
