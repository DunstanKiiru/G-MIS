import React from 'react';

function StaffDevelopmentList({ records, onEdit, onDelete }) {
  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    return new Date(dateStr).toISOString().slice(0, 10);
  };

  return (
    <table className="table table-bordered">
      <thead>
        <tr>
          <th>Operator</th>
          <th>Development Need</th>
          <th>Is Met</th>
          <th>Date Met</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {records.map((record) => (
          <tr key={record.id}>
            <td>{record.operator_id}</td>
            <td>{record.need}</td>
            <td>{record.is_met ? 'Yes' : 'No'}</td>
            <td>{formatDate(record.date_met)}</td>
            <td>
              <button
                onClick={() => onEdit(record)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(record.id)}
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

export default StaffDevelopmentList;
