from flask import Blueprint, request, jsonify
from app.models.water_asset import WaterAsset
from app.extensions import db
from datetime import datetime

water_assets_bp = Blueprint('water_assets', __name__, url_prefix='/api/assets')

@water_assets_bp.route('/', methods=['GET'])
def get_assets():
    query = WaterAsset.query

    asset_type = request.args.get('asset_type')
    status = request.args.get('status')
    if asset_type:
        query = query.filter_by(asset_type=asset_type)
    if status:
        query = query.filter_by(status=status)

    return jsonify([
        {
            "id": wa.id,
            "name": wa.name,
            "asset_type": wa.asset_type,
            "installation_date": wa.installation_date.isoformat(),
            "material": wa.material,
            "capacity": wa.capacity,
            "location": wa.location,
            "latitude": wa.latitude,
            "longitude": wa.longitude,
            "status": wa.status,
            "last_maintenance": wa.last_maintenance.isoformat()
        }
        for wa in query.all()
    ])

@water_assets_bp.route('/<int:id>', methods=['GET'])
def get_single_asset(id):
    wa = WaterAsset.query.get_or_404(id)
    return jsonify({
        "id": wa.id,
        "name": wa.name,
        "asset_type": wa.asset_type,
        "installation_date": wa.installation_date.isoformat(),
        "material": wa.material,
        "capacity": wa.capacity,
        "location": wa.location,
        "latitude": wa.latitude,
        "longitude": wa.longitude,
        "status": wa.status,
        "last_maintenance": wa.last_maintenance.isoformat()
    })

@water_assets_bp.route('/', methods=['POST'])
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

@water_assets_bp.route('/<int:id>', methods=['PUT'])
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

@water_assets_bp.route('/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = WaterAsset.query.get_or_404(id)
    db.session.delete(asset)
    db.session.commit()
    return jsonify({"message": "Asset deleted"})
