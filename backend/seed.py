from app.extensions import db
from app.models import (
    Location, SystemType, OperationalStatus, WaterSystem, Operator,
    TrainingRecord, Tariff, FundingSource, ContributionType,
    CommunityContribution, OMVisitType, OMVisit, SparePartType,
    SparePartInventory, WaterQualityTestType, WaterQualityTest,
    StaffDevelopmentNeed, StaffDevelopmentRecord, WaterAsset
)
from app import create_app
from datetime import datetime, timezone

def seed_data():
    locations_data = [
        {"county": "County 1", "ward": "Ward 1", "latitude": 0.0, "longitude": 0.0},
        {"county": "County 2", "ward": "Ward 2", "latitude": 1.0, "longitude": 1.0},
    ]
    for loc_data in locations_data:
        if not Location.query.filter_by(county=loc_data["county"], ward=loc_data["ward"]).first():
            db.session.add(Location(**loc_data))
    db.session.commit()

    system_types_data = [{"name": "System Type 1"}, {"name": "System Type 2"}]
    for st_data in system_types_data:
        if not SystemType.query.filter_by(name=st_data["name"]).first():
            db.session.add(SystemType(**st_data))
    db.session.commit()

    operational_statuses_data = [{"name": "Operational"}, {"name": "Non-operational"}]
    for os_data in operational_statuses_data:
        if not OperationalStatus.query.filter_by(name=os_data["name"]).first():
            db.session.add(OperationalStatus(**os_data))
    db.session.commit()

    system_type_1 = SystemType.query.filter_by(name="System Type 1").first()
    system_type_2 = SystemType.query.filter_by(name="System Type 2").first()
    operational_status_1 = OperationalStatus.query.filter_by(name="Operational").first()
    operational_status_2 = OperationalStatus.query.filter_by(name="Non-operational").first()
    location_1 = Location.query.filter_by(county="County 1", ward="Ward 1").first()
    location_2 = Location.query.filter_by(county="County 2", ward="Ward 2").first()

    water_systems_data = [
        {"unique_id": "WS1", "name": "Water System 1", "type_id": system_type_1.id, "status_id": operational_status_1.id, "location_id": location_1.id},
        {"unique_id": "WS2", "name": "Water System 2", "type_id": system_type_2.id, "status_id": operational_status_2.id, "location_id": location_2.id},
    ]
    for ws_data in water_systems_data:
        if not WaterSystem.query.filter_by(unique_id=ws_data["unique_id"]).first():
            db.session.add(WaterSystem(**ws_data))
    db.session.commit()

    water_system_1 = WaterSystem.query.filter_by(unique_id="WS1").first()
    water_system_2 = WaterSystem.query.filter_by(unique_id="WS2").first()

    operators_data = [
        {"water_system_id": water_system_1.id, "name": "Operator 1", "training_supported": True, "tariff_charged": False},
        {"water_system_id": water_system_2.id, "name": "Operator 2", "training_supported": False, "tariff_charged": True},
    ]
    for op_data in operators_data:
        if not Operator.query.filter_by(water_system_id=op_data["water_system_id"]).first():
            db.session.add(Operator(**op_data))
    db.session.commit()

    operator_1 = Operator.query.filter_by(name="Operator 1").first()
    operator_2 = Operator.query.filter_by(name="Operator 2").first()

    training_records_data = [
        {"operator_id": operator_1.id, "training_type": "Training Type 1"},
        {"operator_id": operator_2.id, "training_type": "Training Type 2"},
    ]
    for tr_data in training_records_data:
        if not TrainingRecord.query.filter_by(operator_id=tr_data["operator_id"], training_type=tr_data["training_type"]).first():
            db.session.add(TrainingRecord(**tr_data))
    db.session.commit()

    tariffs_data = [
        {"operator_id": operator_1.id, "for_domestic": True, "domestic_type": "Type A", "for_productive": False, "productive_type": None},
        {"operator_id": operator_2.id, "for_domestic": False, "domestic_type": None, "for_productive": True, "productive_type": "Type B"},
    ]
    for tariff_data in tariffs_data:
        if not Tariff.query.filter_by(operator_id=tariff_data["operator_id"]).first():
            db.session.add(Tariff(**tariff_data))
    db.session.commit()

    funding_sources_data = [
        {"water_system_id": water_system_1.id, "source_type": "O&M", "description": "Operation and Maintenance"},
        {"water_system_id": water_system_2.id, "source_type": "Capital", "description": "Capital Investment"},
    ]
    for fs_data in funding_sources_data:
        if not FundingSource.query.filter_by(water_system_id=fs_data["water_system_id"], source_type=fs_data["source_type"]).first():
            db.session.add(FundingSource(**fs_data))
    db.session.commit()

    contribution_types_data = [{"name": "Contribution Type 1"}, {"name": "Contribution Type 2"}]
    for ct_data in contribution_types_data:
        if not ContributionType.query.filter_by(name=ct_data["name"]).first():
            db.session.add(ContributionType(**ct_data))
    db.session.commit()

    contribution_type_1 = ContributionType.query.filter_by(name="Contribution Type 1").first()
    contribution_type_2 = ContributionType.query.filter_by(name="Contribution Type 2").first()

    community_contributions_data = [
        {"water_system_id": water_system_1.id, "contribution_type": contribution_type_1.id, "amount": 100.0, "date_recorded": "2023-01-01"},
        {"water_system_id": water_system_2.id, "contribution_type": contribution_type_2.id, "amount": 200.0, "date_recorded": "2023-01-02"},
    ]
    for cc_data in community_contributions_data:
        if not CommunityContribution.query.filter_by(water_system_id=cc_data["water_system_id"], contribution_type=cc_data["contribution_type"]).first():
            db.session.add(CommunityContribution(**cc_data))
    db.session.commit()

    om_visit_types_data = [{"name": "Visit Type 1"}, {"name": "Visit Type 2"}]
    for ovt_data in om_visit_types_data:
        if not OMVisitType.query.filter_by(name=ovt_data["name"]).first():
            db.session.add(OMVisitType(**ovt_data))
    db.session.commit()

    om_visit_type_1 = OMVisitType.query.filter_by(name="Visit Type 1").first()
    om_visit_type_2 = OMVisitType.query.filter_by(name="Visit Type 2").first()

    om_visits_data = [
        {"water_system_id": water_system_1.id, "visit_type": om_visit_type_1.id, "visit_date": "2023-01-01", "notes": "Notes 1"},
        {"water_system_id": water_system_2.id, "visit_type": om_visit_type_2.id, "visit_date": "2023-01-02", "notes": "Notes 2"},
    ]
    for ov_data in om_visits_data:
        if not OMVisit.query.filter_by(water_system_id=ov_data["water_system_id"], visit_type=ov_data["visit_type"], visit_date=ov_data["visit_date"]).first():
            db.session.add(OMVisit(**ov_data))
    db.session.commit()

    spare_part_types_data = [{"name": "Spare Part Type 1"}, {"name": "Spare Part Type 2"}]
    for spt_data in spare_part_types_data:
        if not SparePartType.query.filter_by(name=spt_data["name"]).first():
            db.session.add(SparePartType(**spt_data))
    db.session.commit()

    spare_part_type_1 = SparePartType.query.filter_by(name="Spare Part Type 1").first()
    spare_part_type_2 = SparePartType.query.filter_by(name="Spare Part Type 2").first()

    spare_part_inventories_data = [
        {"water_system_id": water_system_1.id, "part_type_id": spare_part_type_1.id, "quantity": 10, "last_restocked": "2023-01-01"},
        {"water_system_id": water_system_2.id, "part_type_id": spare_part_type_2.id, "quantity": 20, "last_restocked": "2023-01-02"},
    ]
    for spi_data in spare_part_inventories_data:
        if not SparePartInventory.query.filter_by(water_system_id=spi_data["water_system_id"], part_type_id=spi_data["part_type_id"]).first():
            db.session.add(SparePartInventory(**spi_data))
    db.session.commit()

    water_quality_test_types_data = [{"name": "Test Type 1"}, {"name": "Test Type 2"}]
    for wqtt_data in water_quality_test_types_data:
        if not WaterQualityTestType.query.filter_by(name=wqtt_data["name"]).first():
            db.session.add(WaterQualityTestType(**wqtt_data))
    db.session.commit()

    water_quality_test_type_1 = WaterQualityTestType.query.filter_by(name="Test Type 1").first()
    water_quality_test_type_2 = WaterQualityTestType.query.filter_by(name="Test Type 2").first()

    water_quality_tests_data = [
        {"system_id": water_system_1.id, "test_type_id": water_quality_test_type_1.id, "test_date": "2023-01-01", "value": 1.23},
        {"system_id": water_system_2.id, "test_type_id": water_quality_test_type_2.id, "test_date": "2023-01-02", "value": 4.56},
    ]
    for wqt_data in water_quality_tests_data:
        if not WaterQualityTest.query.filter_by(system_id=wqt_data["system_id"], test_type_id=wqt_data["test_type_id"], test_date=wqt_data["test_date"]).first():
            db.session.add(WaterQualityTest(**wqt_data))
    db.session.commit()

    staff_development_needs_data = [{"name": "Need 1"}, {"name": "Need 2"}]
    for sdn_data in staff_development_needs_data:
        if not StaffDevelopmentNeed.query.filter_by(name=sdn_data["name"]).first():
            db.session.add(StaffDevelopmentNeed(**sdn_data))
    db.session.commit()

    staff_development_need_1 = StaffDevelopmentNeed.query.filter_by(name="Need 1").first()
    staff_development_need_2 = StaffDevelopmentNeed.query.filter_by(name="Need 2").first()

    staff_development_records_data = [
        {"operator_id": operator_1.id, "need_id": staff_development_need_1.id, "date": "2023-01-01", "notes": "Notes 1"},
        {"operator_id": operator_2.id, "need_id": staff_development_need_2.id, "date": "2023-01-02", "notes": "Notes 2"},
    ]
    for sdr_data in staff_development_records_data:
        if not StaffDevelopmentRecord.query.filter_by(operator_id=sdr_data["operator_id"], need_id=sdr_data["need_id"], date=sdr_data["date"]).first():
            db.session.add(StaffDevelopmentRecord(**sdr_data))
    db.session.commit()

    water_assets_data = [
        {
            "name": "Water Asset 1",
            "asset_type": "Type A",
            "installation_date": datetime(2020, 1, 1, tzinfo=timezone.utc),
            "material": "Material A",
            "capacity": 100.0,
            "location": "Location A",
            "latitude": 0.0,
            "longitude": 0.0,
            "status": "Operational",
            "last_maintenance": datetime(2023, 1, 1, tzinfo=timezone.utc),
        },
        {
            "name": "Water Asset 2",
            "asset_type": "Type B",
            "installation_date": datetime(2021, 1, 1, tzinfo=timezone.utc),
            "material": "Material B",
            "capacity": 200.0,
            "location": "Location B",
            "latitude": 1.0,
            "longitude": 1.0,
            "status": "Non-operational",
            "last_maintenance": datetime(2023, 6, 1, tzinfo=timezone.utc),
        },
    ]
    for wa_data in water_assets_data:
        if not WaterAsset.query.filter_by(name=wa_data["name"]).first():
            db.session.add(WaterAsset(**wa_data))
    db.session.commit()

    print("Seed data added successfully.")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()
