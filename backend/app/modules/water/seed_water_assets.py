from app.extensions import db
from app.models.water_asset import WaterAsset
from datetime import datetime, timezone
from app import create_app

def seed_water_assets():
    app = create_app()
    with app.app_context():
        assets = [
            WaterAsset(
                name="Main Water Tank",
                asset_type="Tank",
                installation_date=datetime(2023, 1, 15, 10, 0, 0, tzinfo=timezone.utc),
                material="Concrete",
                capacity=5000.0,
                location="Sector 12",
                latitude=40.7128,
                longitude=-74.0060,
                status="Active",
                last_maintenance=None
            ),
            WaterAsset(
                name="Secondary Pipe",
                asset_type="Pipe",
                installation_date=datetime(2022, 5, 20, 8, 30, 0, tzinfo=timezone.utc),
                material="PVC",
                capacity=200.0,
                location="Sector 7",
                latitude=40.7138,
                longitude=-74.0050,
                status="Inactive",
                last_maintenance=None
            ),
            WaterAsset(
                name="Backup Pump",
                asset_type="Pump",
                installation_date=datetime(2021, 11, 10, 14, 0, 0, tzinfo=timezone.utc),
                material="Steel",
                capacity=150.0,
                location="Sector 3",
                latitude=40.7148,
                longitude=-74.0040,
                status="Active",
                last_maintenance=None
            )
        ]

        for asset in assets:
            db.session.add(asset)
        db.session.commit()
        print("Seeded water assets successfully.")

if __name__ == "__main__":
    seed_water_assets()
