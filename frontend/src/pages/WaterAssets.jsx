import React, { useEffect } from 'react'
import axios from 'axios'
import AssetForm from '../components/Assets/AssetForm'
import AssetList from '../components/Assets/AssetList'

function WaterAssets(){
  const [assets, setAssets] = React.useState([])
  const [editingAsset, setEditingAsset] = React.useState(null)

  const fetchAssets = async () => {
    const res = await axios.get('/api/assets')
    setAssets(res.data)
  }
  useEffect(() => {
    fetchAssets()
  }, [])

  const handleEdit = (asset) => {
    setEditingAsset(asset)
  }

  const handleDelete = async (id) => {
    if (confirm('Are you sure you want to delete this asset?')){
      await axios.delete(`/api/assets/${id}`)
      fetchAssets()
    }
  }

  const handleSubmit = async (data, resetForm) => {
    try {
      // Convert capacity, latitude, longitude to floats
      const convertedData = {
        ...data,
        capacity: parseFloat(data.capacity),
        latitude: parseFloat(data.latitude),
        longitude: parseFloat(data.longitude),
      };

      if (editingAsset) {
        await axios.put(`/api/assets/${editingAsset.id}`, convertedData);
        setEditingAsset(null);
      } else {
        await axios.post('/api/assets', convertedData);
      }
      resetForm();
      fetchAssets();
    } catch (error) {
      console.error('Error submitting asset:', error);
      alert('Failed to submit asset. Please check the input values and try again.');
    }
  }

  return (
    <>
      <div className="water-assets-container">
        <div className="water-assets-form">
          <h2>{editingAsset ? "Edit" : "Add"} Water Asset</h2>
          <AssetForm asset={editingAsset} onSubmit={handleSubmit} />
        </div>
        <div className="water-assets-list">
          <h3>Garissa County Water Assets</h3>
          <AssetList assets={assets} onEdit={handleEdit} onDelete={handleDelete} />
        </div>
      </div>
    </>
  );
}

export default WaterAssets
