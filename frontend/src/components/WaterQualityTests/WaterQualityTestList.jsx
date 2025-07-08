import React from 'react';

function WaterQualityTestList({ tests, onEdit, onDelete }) {
  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    return new Date(dateStr).toISOString().slice(0, 10);
  };

  return (
    <table className="table table-bordered">
      <thead>
        <tr>
          <th>Water System</th>
          <th>Test Type</th>
          <th>Test Date</th>
          <th>Value</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {tests.map((test) => (
          <tr key={test.id}>
            <td>{test.system}</td>
            <td>{test.type}</td>
            <td>{formatDate(test.test_date)}</td>
            <td>{test.value}</td>
            <td>
              <button
                onClick={() => onEdit(test)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(test.id)}
                className="btn btn-sm btn-danger"
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default WaterQualityTestList;
