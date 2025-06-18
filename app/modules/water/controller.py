from flask.views import MethodView
from flask import request, jsonify
from app.models.water_asset import WaterAsset
from app.extensions import db
from datetime import datetime

class WaterAssetAPI(MethodView):
    def get(self):
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
            }
            for wa in water_assets
        ])

    def post(self):
        data = request.get_json()
        try:
            new_asset = WaterAsset(
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
            db.session.add(new_asset)
            db.session.commit()

            return jsonify({
                "message": "Water asset created successfully.",
                "id": new_asset.id
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    
    def put(self):
        data = request.get_json()
        asset_id = data.get("id")
        asset = WaterAsset.query.get(asset_id)
        if not asset:
            return jsonify({"error": "Asset not found"}), 404
        try:
            asset.name = data["name"]
            asset.asset_type = data["asset_type"]
            asset.installation_date = datetime.strptime(data["installation_date"], "%Y-%m-%d") if data.get("installation_date") else None
            asset.material = data["material"]
            asset.capacity = data["capacity"]
            asset.location = data["location"]
            asset.latitude = data["latitude"]
            asset.longitude = data["longitude"]
            asset.status = data["status"]
            asset.last_maintenance = datetime.strptime(data["last_maintenance"], "%Y-%m-%d") if data.get("last_maintenance") else None
            
            db.session.commit()
            return jsonify({"message": "Asset updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    
    def delete(self):
        data = request.get_json()
        asset_id = data.get("id")
        asset = WaterAsset.query.get(asset_id)
        if not asset:
            return jsonify({"error": "Asset not found"}), 404
        try:
            db.session.delete(asset)
            db.session.commit()
            return jsonify({"message": "Asset deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

