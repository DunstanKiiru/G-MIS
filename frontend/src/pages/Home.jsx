import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import DashboardChart from "../components/Dashboard/Dashboard";

const Home = () => {
  const [assets, setAssets] = useState([]);

  useEffect(() => {
    axios.get("/api/assets").then((res) => setAssets(res.data));
  }, []);

  const totalAssets = assets.length;
  const statusCounts = assets.reduce((acc, asset) => {
    const status = asset.status || "Unknown";
    acc[status] = (acc[status] || 0) + 1;
    return acc;
  }, {});

  const labels = Object.keys(statusCounts);
  const dataValues = Object.values(statusCounts);

  return (
    <div className="container mt-5 text-center">
      <h1>GARUWASCO MIS</h1>
      <p>
        Garissa Rural Water and Sanitation Company — Safe, adequate and
        sustainable rural water services
      </p>

      <div className="my-4">
        <Link to="/waterassets" className="btn btn-primary btn-lg me-3">
          View Water Assets
        </Link>
        <Link to="/contact" className="btn btn-outline-secondary btn-lg">
          Contact Us
        </Link>
      </div>
      {assets.length > 0 ? (
        <DashboardChart labels={labels} dataValues={dataValues} />
      ) : (
        <p>Loading asset data...</p>
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
