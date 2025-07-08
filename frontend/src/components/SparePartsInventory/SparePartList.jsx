import React from 'react';

function SparePartList({ inventory, onEdit, onDelete }) {
  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    return new Date(dateStr).toISOString().slice(0, 10);
  };

  return (
    <table className="table table-bordered">
      <thead>
        <tr>
          <th>Water System</th>
          <th>Part Type</th>
          <th>Quantity</th>
          <th>Last Restocked</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {inventory.map((part) => (
          <tr key={part.id}>
            <td>{part.water_system}</td>
            <td>{part.part_type}</td>
            <td>{part.quantity}</td>
            <td>{formatDate(part.last_restocked)}</td>
            <td>
              <button
                onClick={() => onEdit(part)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(part.id)}
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

export default SparePartList;
