from flask import Blueprint, request, jsonify
from app.models import WaterAsset
from app.extensions import db
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/api/assets', methods=['GET'])
def get_assets():
    query = WaterAsset.query
    asset_type = request.args.get('asset_type')
    status = request.args.get('status')
    if asset_type:
        query = query.filter_by(asset_type=asset_type)
    if status:
        query = query.filter_by(status=status)

    assets = query.all()
    return jsonify([{
        "id": a.id,
        "name": a.name,
        "asset_type": a.asset_type,
        "installation_date": a.installation_date.isoformat(),
        "material": a.material,
        "capacity": a.capacity,
        "location": a.location,
        "latitude": a.latitude,
        "longitude": a.longitude,
        "status": a.status,
        "last_maintenance": a.last_maintenance.isoformat()
    } for a in assets])

@api.route('/api/assets/<int:id>', methods=['GET'])
def get_asset(id):
    asset = WaterAsset.query.get_or_404(id)
    return jsonify({
        "id": asset.id,
        "name": asset.name,
        "asset_type": asset.asset_type,
        "installation_date": asset.installation_date.isoformat(),
        "material": asset.material,
        "capacity": asset.capacity,
        "location": asset.location,
        "latitude": asset.latitude,
        "longitude": asset.longitude,
        "status": asset.status,
        "last_maintenance": asset.last_maintenance.isoformat()
    })

@api.route('/api/assets', methods=['POST'])
def create_asset():
    data = request.get_json()
    asset = WaterAsset(
        name=data['name'],
        asset_type=data['asset_type'],
        installation_date=datetime.fromisoformat(data['installation_date']),
        material=data['material'],
        capacity=data['capacity'],
        location=data['location'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        status=data['status'],
        last_maintenance=datetime.fromisoformat(data['last_maintenance'])
    )
    db.session.add(asset)
    db.session.commit()
    return jsonify({"message": "Asset created", "id": asset.id}), 201

@api.route('/api/assets/<int:id>', methods=['PUT'])
def update_asset(id):
    asset = WaterAsset.query.get_or_404(id)
    data = request.get_json()
    for field in ['name', 'asset_type', 'material', 'capacity', 'location', 'latitude', 'longitude', 'status']:
        if field in data:
            setattr(asset, field, data[field])
    if 'installation_date' in data:
        asset.installation_date = datetime.fromisoformat(data['installation_date'])
    if 'last_maintenance' in data:
        asset.last_maintenance = datetime.fromisoformat(data['last_maintenance'])
    db.session.commit()
    return jsonify({"message": "Asset updated"})

@api.route('/api/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = WaterAsset.query.get_or_404(id)
    db.session.delete(asset)
    db.session.commit()
    return jsonify({"message": "Asset deleted"})
