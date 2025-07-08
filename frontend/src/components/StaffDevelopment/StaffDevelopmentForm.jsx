import React, { useState, useEffect } from 'react';

const initialState = {
  operator_id: '',
  need_id: '',
  is_met: false,
  date_met: ''
};

function StaffDevelopmentForm({ record, onSubmit, needs, operators }) {
  const [form, setForm] = useState(initialState);

  useEffect(() => {
    if (record) {
      setForm({
        operator_id: record.operator_id || '',
        need_id: record.need_id || '',
        is_met: record.is_met || false,
        date_met: record.date_met ? record.date_met.slice(0, 10) : ''
      });
    } else {
      setForm(initialState);
    }
  }, [record]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form, () => setForm(initialState));
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <select
        name="operator_id"
        value={form.operator_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Operator</option>
        {operators.map(op => (
          <option key={op.id} value={op.id}>{op.name || op.id}</option>
        ))}
      </select>

      <select
        name="need_id"
        value={form.need_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Development Need</option>
        {needs.map(need => (
          <option key={need.id} value={need.id}>{need.name}</option>
        ))}
      </select>

      <div className="form-check mb-2">
        <input
          type="checkbox"
          name="is_met"
          id="is_met"
          checked={form.is_met}
          onChange={handleChange}
          className="form-check-input"
        />
        <label htmlFor="is_met" className="form-check-label">Is Met</label>
      </div>

      <input
        type="date"
        name="date_met"
        placeholder="Date Met"
        value={form.date_met}
        onChange={handleChange}
        className="form-control mb-2"
      />

      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <button type="submit" className="btn btn-primary">
          {record ? 'Update' : 'Create'}
        </button>
      </div>
    </form>
  );
}

export default StaffDevelopmentForm;
