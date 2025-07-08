import React, { useEffect, useState } from 'react';
import ContributionForm from '../components/CommunityContributions/ContributionForm';

const CommunityContributions = () => {
  const [contributions, setContributions] = useState([]);
  const [types, setTypes] = useState([]);
  const [waterSystems, setWaterSystems] = useState([]);
  const [editingContribution, setEditingContribution] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [typesRes, systemsRes, contributionsRes] = await Promise.all([
        fetch('/api/community/types', { credentials: 'include' }),
        fetch('/api/water-systems', { credentials: 'include' }),
        fetch('/api/community/contributions', { credentials: 'include' }),
      ]);
      const typesData = await typesRes.json();
      const systemsData = await systemsRes.json();
      const contributionsData = await contributionsRes.json();
      setTypes(typesData);
      setWaterSystems(systemsData);
      setContributions(contributionsData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleCreate = async (data) => {
    try {
      const res = await fetch('/api/community/contributions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(data),
      });
      if (res.ok) {
        fetchData();
      } else {
        console.error('Failed to create contribution');
      }
    } catch (error) {
      console.error('Error creating contribution:', error);
    }
  };

  const handleUpdate = async (id, data) => {
    try {
      const res = await fetch(`/api/community/contributions/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(data),
      });
      if (res.ok) {
        setEditingContribution(null);
        fetchData();
      } else {
        console.error('Failed to update contribution');
      }
    } catch (error) {
      console.error('Error updating contribution:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const res = await fetch(`/api/community/contributions/${id}`, {
        method: 'DELETE',
        credentials: 'include',
      });
      if (res.ok) {
        fetchData();
      } else {
        console.error('Failed to delete contribution');
      }
    } catch (error) {
      console.error('Error deleting contribution:', error);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Community Contributions</h1>
      <ContributionForm
        types={types}
        waterSystems={waterSystems}
        onSubmit={editingContribution ? (data) => handleUpdate(editingContribution.id, data) : handleCreate}
        initialData={editingContribution}
        onCancel={() => setEditingContribution(null)}
      />
      <table>
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
              <td>{waterSystems.find(ws => ws.id === contribution.system_id)?.name || contribution.system_id}</td>
              <td>{contribution.type}</td>
              <td>{contribution.amount}</td>
              <td>{new Date(contribution.date_recorded).toLocaleDateString()}</td>
              <td>
                <button onClick={() => setEditingContribution(contribution)}>Edit</button>
                <button onClick={() => handleDelete(contribution.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CommunityContributions;
