from flask import request, jsonify
from app.extensions import db
from app.models.water_asset import WaterAsset

def list_assets():
    assets = WaterAsset.query.all()
    return jsonify([asset.to_dict() for asset in assets])

def get_asset(asset_id):
    asset = WaterAsset.query.get_or_404(asset_id)
    return jsonify(asset.to_dict())

def create_asset():
    data = request.get_json()

    asset = WaterAsset(
        name=data["name"],
        asset_type=data["asset_type"],
        material=data["material"],
        capacity=data["capacity"],
        location=data["location"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        status=data["status"]
    )

    db.session.add(asset)
    db.session.commit()
    return jsonify(asset.to_dict()), 201
