from flask import Blueprint
from .controller import WaterAssetAPI

water_asset_bp = Blueprint("water_asset", __name__)
water_asset_bp.add_url_rule("/", view_func=WaterAssetAPI.as_view("asset_api"))