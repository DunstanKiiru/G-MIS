import React from "react"
import { Pie, Bar } from "react-chartjs-2"
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
} from "chart.js"

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  Title
)

const DashboardChart = ({
  statusLabels,
  statusValues,
  typeLabels,
  typeValues,
  kpis,
}) => {
  const pieData = {
    labels: statusLabels,
    datasets: [
      {
        data: statusValues,
        backgroundColor: [
          "#198754", // green
          "#dc3545", // red
          "#ffc107", // yellow
          "#0d6efd", // blue
          "#6f42c1", // purple
        ],
        borderColor: "#fff",
        borderWidth: 1,
      },
    ],
  }

  const barData = {
    labels: typeLabels,
    datasets: [
      {
        label: "Number of Assets",
        data: typeValues,
        backgroundColor: "#0d6efd",
      },
    ],
  }

  return (
    <div className="my-5 container">
      {/* KPI Grid */}
      <div className="row text-center mb-5">
        {(kpis || []).map(({ label, value }, idx) => (
          <div key={idx} className="col-6 col-md-3 mb-3">
            <div className="p-3 bg-light border rounded shadow-sm">
              <h2>{value}</h2>
              <p className="text-muted mb-0">{label}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Charts Section */}
      <div className="row mb-5">
        {/* Pie Chart */}
        <div className="col-12 col-lg-6 mb-4 mb-lg-0 d-flex flex-column align-items-center">
          <h5 className="text-center">Assets Status</h5>
          <div style={{ width: "100%", maxWidth: 400 }}>
            <Pie data={pieData} />
          </div>
        </div>

        {/* Bar Chart */}
        <div className="col-12 col-lg-6 d-flex flex-column align-items-center">
          <h5 className="text-center">Assets by Type</h5>
          <div style={{ width: "100%", maxWidth: 600, height: 400 }}>
            <Bar
              data={barData}
              options={{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                  legend: { display: false },
                },
                scales: {
                  y: {
                    beginAtZero: true,
                    ticks: { stepSize: 1 },
                  },
                },
              }}
            />
          </div>
        </div>
      </div>
    </div>
  )
}

export default DashboardChart
