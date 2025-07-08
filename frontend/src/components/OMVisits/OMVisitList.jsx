import React from 'react';

function OMVisitList({ visits, onEdit, onDelete }) {
  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    return new Date(dateStr).toISOString().slice(0, 10);
  };

  return (
    <table className="table table-bordered">
      <thead>
        <tr>
          <th>Water System</th>
          <th>Type</th>
          <th>Visit Date</th>
          <th>Notes</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {visits.map((visit) => (
          <tr key={visit.id}>
            <td>{visit.water_system}</td>
            <td>{visit.type}</td>
            <td>{formatDate(visit.visit_date)}</td>
            <td>{visit.notes}</td>
            <td>
              <button
                onClick={() => onEdit(visit)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(visit.id)}
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

export default OMVisitList;
