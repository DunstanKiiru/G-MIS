import React, { useEffect, useState } from 'react';
import axios from 'axios';
import StaffDevelopmentForm from '../components/StaffDevelopment/StaffDevelopmentForm';
import StaffDevelopmentList from '../components/StaffDevelopment/StaffDevelopmentList';

function StaffDevelopment() {
  const [records, setRecords] = useState([]);
  const [needs, setNeeds] = useState([]);
  const [operators, setOperators] = useState([]);
  const [editingRecord, setEditingRecord] = useState(null);

  const fetchData = async () => {
    try {
      const [needsRes, operatorsRes, recordsRes] = await Promise.all([
        axios.get('/api/staff-dev/needs'),
        axios.get('/api/operators'),
        axios.get('/api/staff-dev/records'),
      ]);
      setNeeds(needsRes.data);
      setOperators(operatorsRes.data);
      setRecords(recordsRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Failed to fetch data from server.');
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleEdit = (record) => {
    setEditingRecord(record);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this record?')) {
      try {
        await axios.delete(`/api/staff-dev/records/${id}`);
        fetchData();
      } catch (error) {
        console.error('Error deleting record:', error);
        alert('Failed to delete record.');
      }
    }
  };

  const handleSubmit = async (data, resetForm) => {
    try {
      if (editingRecord) {
        await axios.put(`/api/staff-dev/records/${editingRecord.id}`, data);
        setEditingRecord(null);
      } else {
        await axios.post('/api/staff-dev/records', data);
      }
      resetForm();
      fetchData();
    } catch (error) {
      console.error('Error submitting record:', error);
      alert('Failed to submit record.');
    }
  };

  return (
    <div className="staff-development-container">
      <div className="staff-development-form">
        <h2>{editingRecord ? 'Edit' : 'Add'} Staff Development Record</h2>
        <StaffDevelopmentForm
          record={editingRecord}
          onSubmit={handleSubmit}
          needs={needs}
          operators={operators}
        />
      </div>
      <div className="staff-development-list">
        <h3>Staff Development Records</h3>
        <StaffDevelopmentList
          records={records}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default StaffDevelopment;
