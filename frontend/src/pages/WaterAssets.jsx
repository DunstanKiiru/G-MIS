import React, { useEffect } from 'react'
import axios from 'axios'
import AssetForm from '../components/AssetForm'
import AssetList from '../components/AssetList'

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
      await axios.delete('/api/assets/${id}')
      fetchAssets()
    }
  }

  const handleSubmit = async (data, resetForm) =>{
    if (editingAsset){
      await axios.put(`/api/assets/${editingAsset.id}`, data)
      setEditingAsset(null)
    } else {
      await axios.post('/api/assets', data)
    }
    resetForm()
    fetchAssets()
  }

  return (
    <>
      <div className="EditContainer">
        <h2>{editingAsset ? "Edit" : "Add"} Water Assed</h2>
        <AssetForm asset={editingAsset} onSubmit={handleSubmit} />
        <h3>Garissa County Water Assets</h3>
        <AssetList assets={assets} onEdit={handleEdit} onDelete={handleDelete} />
      </div>
    </>
  );
}


export default WaterAssets