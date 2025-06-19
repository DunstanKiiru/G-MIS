function AssetList({ assets, onEdit, onDelete }) {
  return (
    <table className="table table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Status</th>
          <th>Location</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {assets.map((asset) => (
          <tr key={asset.id}>
            <td>{asset.name}</td>
            <td>{asset.asset_type}</td>
            <td>{asset.status}</td>
            <td>{asset.location}</td>
            <td>
              <button
                onClick={() => onEdit(asset)}
                className="btn btn-sm btn-warning me-2"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(asset.id)}
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

export default AssetList