from flask import Blueprint, request, jsonify
from models import WaterAsset, db
from datetime import datetime

water_assets_bp = Blueprint('water_assets', __name__)

@water_assets_bp.route("/", methods=["GET"])
def get_water_assets():
    water_assets = WaterAsset.query.all()
    return jsonify([
        {
            "id": wa.id,
            "name": wa.name,
            "asset_type": wa.asset_type,
            "installation_date": wa.installation_date.isoformat() if wa.installation_date else None,
            "material": wa.material,
            "capacity": wa.capacity,
            "location": wa.location,
            "latitude": wa.latitude,
            "longitude": wa.longitude,
            "status": wa.status,
            "last_maintenance": wa.last_maintenance.isoformat() if wa.last_maintenance else None,
        } for wa in water_assets
    ])

@water_assets_bp.route("/", methods=["POST"])
def create_water_asset():
    data = request.get_json()

    try:
        new_water_asset = WaterAsset(
            name=data["name"],
            asset_type=data["asset_type"],
            installation_date=datetime.strptime(data["installation_date"], "%Y-%m-%d") if data.get("installation_date") else None,
            material=data["material"],
            capacity=data["capacity"],
            location=data["location"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            status=data["status"],
            last_maintenance=datetime.strptime(data["last_maintenance"], "%Y-%m-%d") if data.get("last_maintenance") else None
        )

        db.session.add(new_water_asset)
        db.session.commit()

        return jsonify({
            "message": "Water asset created successfully.",
            "id": new_water_asset.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
