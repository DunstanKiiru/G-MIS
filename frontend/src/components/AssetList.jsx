function AssetList({ assets, onEdit, onDelete }) {
  return (
    <ul>
      {assets.map((asset) => (
        <li key={asset.id} style={{ marginBottom: 10 }}>
          <strong>{asset.name}</strong> — {asset.asset_type} ({asset.status})
          <br />
          <button onClick={() => onEdit(asset)}>Edit</button>
          <button onClick={() => onDelete(asset.id)} style={{ marginLeft: 10 }}>
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
}

export default AssetList;
