import React, { useState, useEffect } from 'react';

const initialState = {
  system_id: '',
  visit_type_id: '',
  visit_date: '',
  notes: ''
};

function OMVisitForm({ visit, onSubmit, types, waterSystems }) {
  const [form, setForm] = useState(initialState);

  useEffect(() => {
    if (visit) {
      setForm({
        system_id: visit.system_id || '',
        visit_type_id: visit.visit_type_id || '',
        visit_date: visit.visit_date ? visit.visit_date.slice(0, 10) : '',
        notes: visit.notes || ''
      });
    } else {
      setForm(initialState);
    }
  }, [visit]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form, () => setForm(initialState));
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <select
        name="system_id"
        value={form.system_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Water System</option>
        {waterSystems.map(ws => (
          <option key={ws.id} value={ws.id}>{ws.name || ws.id}</option>
        ))}
      </select>

      <select
        name="visit_type_id"
        value={form.visit_type_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Visit Type</option>
        {types.map(type => (
          <option key={type.id} value={type.id}>{type.name}</option>
        ))}
      </select>

      <input
        type="date"
        name="visit_date"
        placeholder="Visit Date"
        value={form.visit_date}
        onChange={handleChange}
        className="form-control mb-2"
      />

      <textarea
        name="notes"
        placeholder="Notes"
        value={form.notes}
        onChange={handleChange}
        className="form-control mb-2"
        rows={3}
      />

      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <button type="submit" className="btn btn-primary">
          {visit ? 'Update' : 'Create'}
        </button>
      </div>
    </form>
  );
}

export default OMVisitForm;
