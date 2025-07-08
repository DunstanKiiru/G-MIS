import React, { useEffect, useState } from 'react';
import axios from 'axios';
import WaterQualityTestForm from '../components/WaterQualityTests/WaterQualityTestForm';
import WaterQualityTestList from '../components/WaterQualityTests/WaterQualityTestList';

function WaterQualityTests() {
  const [tests, setTests] = useState([]);
  const [types, setTypes] = useState([]);
  const [waterSystems, setWaterSystems] = useState([]);
  const [editingTest, setEditingTest] = useState(null);

  const fetchData = async () => {
    try {
      const [typesRes, waterSystemsRes, testsRes] = await Promise.all([
        axios.get('/api/quality-tests/types'),
        axios.get('/api/watersystems'),
        axios.get('/api/quality-tests'),
      ]);
      setTypes(typesRes.data);
      setWaterSystems(waterSystemsRes.data);
      setTests(testsRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Failed to fetch data from server.');
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleEdit = (test) => {
    setEditingTest(test);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this test record?')) {
      try {
        await axios.delete(`/api/quality-tests/${id}`);
        fetchData();
      } catch (error) {
        console.error('Error deleting test record:', error);
        alert('Failed to delete test record.');
      }
    }
  };

  const handleSubmit = async (data, resetForm) => {
    try {
      if (editingTest) {
        await axios.put(`/api/quality-tests/${editingTest.id}`, data);
        setEditingTest(null);
      } else {
        await axios.post('/api/quality-tests', data);
      }
      resetForm();
      fetchData();
    } catch (error) {
      console.error('Error submitting test record:', error);
      alert('Failed to submit test record.');
    }
  };

  return (
    <div className="water-quality-tests-container">
      <div className="water-quality-tests-form">
        <h2>{editingTest ? 'Edit' : 'Add'} Water Quality Test</h2>
        <WaterQualityTestForm
          test={editingTest}
          onSubmit={handleSubmit}
          types={types}
          waterSystems={waterSystems}
        />
      </div>
      <div className="water-quality-tests-list">
        <h3>Water Quality Tests</h3>
        <WaterQualityTestList
          tests={tests}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default WaterQualityTests;
