import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import DashboardChart from "../components/Dashboard/Dashboard";

const Home = () => {
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("/api/assets")
      .then((res) => setAssets(res.data))
      .catch(() => setError("Failed to fetch assets."))
      .finally(() => setLoading(false));
  }, []);

  // Status
  const statusCounts = assets.reduce((acc, asset) => {
    const status = asset.status || "Unknown";
    acc[status] = (acc[status] || 0) + 1;
    return acc;
  }, {});

  const statusLabels = Object.keys(statusCounts);
  const statusValues = Object.values(statusCounts);

  // Type
  const typeCounts = assets.reduce((acc, asset) => {
    const type = asset.asset_type || "Unknown";
    acc[type] = (acc[type] || 0) + 1;
    return acc;
  }, {});

  const typeLabels = Object.keys(typeCounts);
  const typeValues = Object.values(typeCounts);

  // KPI
  const totalAssets = assets.length;
  const activeAssets = statusCounts["Active"] || 0;
  const inactiveAssets = statusCounts["Inactive"] || 0;
  const unknownStatusAssets = statusCounts["Unknown"] || 0;

  const kpis = [
    { label: "Total Assets", value: totalAssets },
    { label: "Active Assets", value: activeAssets },
    { label: "Inactive Assets", value: inactiveAssets },
    { label: "Unknown Status", value: unknownStatusAssets },
  ];

  return (
    <div className="container mt-5 text-center">
      <h1>GARUWASCO MIS</h1>
      <p>
        Garissa Rural Water and Sanitation Company — Safe, adequate and
        sustainable rural water services
      </p>

      {/* Mini Navigation*/}
      <div className="my-4">
        <Link to="/waterassets" className="btn btn-primary btn-lg me-3">
          View Water Assets
        </Link>
        <Link to="/contact" className="btn btn-outline-secondary btn-lg">
          Contact Us
        </Link>
      </div>

      {/*Chart*/}
      {loading ? (
        <p>Loading asset data...</p>
      ) : error ? (
        <p className="text-danger">{error}</p>
      ) : (
        <DashboardChart
          statusLabels={statusLabels}
          statusValues={statusValues}
          typeLabels={typeLabels}
          typeValues={typeValues}
          kpis={kpis}
        />
      )}

      <section className="mt-5">
        <h2 className="h4 text-secondary">Our Mission</h2>
        <p className="text-muted">
          To provide safe, reliable, and affordable water services to all
          residents of Garissa County through efficient infrastructure
          management and community engagement.
        </p>
      </section>
    </div>
  );
};

export default Home;
