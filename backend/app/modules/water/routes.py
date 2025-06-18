from flask import Blueprint
from .controller import list_assets, get_asset, create_asset

water_bp = Blueprint('water', __name__)

water_bp.route("/", methods=["GET"])(list_assets)
water_bp.route("/<int:asset_id>", methods=["GET"])(get_asset)
water_bp.route("/", methods=["POST"])(create_asset)
