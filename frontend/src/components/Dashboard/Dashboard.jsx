import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

const DashboardChart = ({ labels, dataValues }) => {
  const data = {
    labels: labels,
    datasets: [
      {
        data: dataValues,
        backgroundColor: [
          "green", // Functional
          "red", // Non-functional
          "#ffc107", // Other statuses
        ],
        borderColor: "#fff",
        borderWidth: 1,
      },
    ],
  };

  return (
    <div className="my-5 p-4 bg-white rounded shadow text-center">
      <h4 className="mb-4">Water Assets Status</h4>
      <div style={{ maxWidth: "400px", margin: "0 auto" }}>
        <Pie data={data} />
      </div>
    </div>
  );
};

export default DashboardChart;
