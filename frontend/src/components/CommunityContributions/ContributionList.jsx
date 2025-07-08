import React from 'react';

function ContributionList({ contributions, onEdit, onDelete }) {
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
          <th>Amount</th>
          <th>Date Recorded</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {contributions.map((contribution) => (
          <tr key={contribution.id}>
            <td>{contribution.system_id}</td>
            <td>{contribution.type}</td>
            <td>{contribution.amount}</td>
            <td>{formatDate(contribution.date_recorded)}</td>
            <td>
              <button
                onClick={() => onEdit(contribution)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(contribution.id)}
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

export default ContributionList;
