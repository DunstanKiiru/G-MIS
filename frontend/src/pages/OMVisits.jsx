import React, { useEffect, useState } from 'react';
import axios from 'axios';
import OMVisitForm from '../components/OMVisits/OMVisitForm';
import OMVisitList from '../components/OMVisits/OMVisitList';

function OMVisits() {
  const [visits, setVisits] = useState([]);
  const [types, setTypes] = useState([]);
  const [waterSystems, setWaterSystems] = useState([]);
  const [editingVisit, setEditingVisit] = useState(null);

  const fetchData = async () => {
    try {
      const [typesRes, waterSystemsRes, visitsRes] = await Promise.all([
        axios.get('/api/om-visits/types'),
        axios.get('/api/watersystems'),
        axios.get('/api/om-visits'),
      ]);
      setTypes(typesRes.data);
      setWaterSystems(waterSystemsRes.data);
      setVisits(visitsRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Failed to fetch data from server.');
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleEdit = (visit) => {
    setEditingVisit(visit);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this visit?')) {
      try {
        await axios.delete(`/api/om-visits/${id}`);
        fetchData();
      } catch (error) {
        console.error('Error deleting visit:', error);
        alert('Failed to delete visit.');
      }
    }
  };

  const handleSubmit = async (data, resetForm) => {
    try {
      if (editingVisit) {
        await axios.put(`/api/om-visits/${editingVisit.id}`, data);
        setEditingVisit(null);
      } else {
        await axios.post('/api/om-visits', data);
      }
      resetForm();
      fetchData();
    } catch (error) {
      console.error('Error submitting visit:', error);
      alert('Failed to submit visit.');
    }
  };

  return (
    <div className="om-visits-container">
      <div className="om-visits-form">
        <h2>{editingVisit ? 'Edit' : 'Add'} OM Visit</h2>
        <OMVisitForm
          visit={editingVisit}
          onSubmit={handleSubmit}
          types={types}
          waterSystems={waterSystems}
        />
      </div>
      <div className="om-visits-list">
        <h3>OM Visits</h3>
        <OMVisitList
          visits={visits}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default OMVisits;
