import React, { useState } from 'react';

function AssetList({ assets, onEdit }) {
  const [filterType, setFilterType] = useState('All');
  const [filterStatus, setFilterStatus] = useState('All');

  const assetTypes = ['All', ...Array.from(new Set(assets.map(a => a.asset_type)))];
  const statuses = ['All', ...Array.from(new Set(assets.map(a => a.status)))];

  const filteredAssets = assets.filter(asset => {
    return (filterType === 'All' || asset.asset_type === filterType) &&
           (filterStatus === 'All' || asset.status === filterStatus);
  });

  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    return new Date(dateStr).toISOString().slice(0, 10);
  };

  return (
    <>
      <div className="mb-3 d-flex gap-3">
        <div>
          <label htmlFor="filterType" className="form-label">Filter by Type:</label>
          <select
            id="filterType"
            className="form-select"
            value={filterType}
            onChange={e => setFilterType(e.target.value)}
          >
            {assetTypes.map(type => (
              <option key={type} value={type}>{type}</option>
            ))}
          </select>
        </div>
        <div>
          <label htmlFor="filterStatus" className="form-label">Filter by Status:</label>
          <select
            id="filterStatus"
            className="form-select"
            value={filterStatus}
            onChange={e => setFilterStatus(e.target.value)}
          >
            {statuses.map(status => (
              <option key={status} value={status}>{status}</option>
            ))}
          </select>
        </div>
      </div>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Status</th>
            <th>Location</th>
            <th>Installation Date</th>
            <th>Last Maintenance</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredAssets.map((asset) => (
            <tr key={asset.id}>
              <td>{asset.name}</td>
              <td>{asset.asset_type}</td>
              <td>{asset.status}</td>
              <td>{asset.location}</td>
              <td>{formatDate(asset.installation_date)}</td>
              <td>{formatDate(asset.last_maintenance)}</td>
              <td>
                <button
                  onClick={() => onEdit(asset)}
                  className="btn btn-sm btn-warning"
                >
                  Edit
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}

export default AssetList;
