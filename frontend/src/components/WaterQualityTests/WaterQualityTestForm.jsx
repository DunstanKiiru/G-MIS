import React, { useState, useEffect } from 'react';

const initialState = {
  system_id: '',
  test_type_id: '',
  test_date: '',
  value: ''
};

function WaterQualityTestForm({ test, onSubmit, types, waterSystems }) {
  const [form, setForm] = useState(initialState);

  useEffect(() => {
    if (test) {
      setForm({
        system_id: test.system_id || '',
        test_type_id: test.test_type_id || '',
        test_date: test.test_date ? test.test_date.slice(0, 10) : '',
        value: test.value || ''
      });
    } else {
      setForm(initialState);
    }
  }, [test]);

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
        name="test_type_id"
        value={form.test_type_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Test Type</option>
        {types.map(type => (
          <option key={type.id} value={type.id}>{type.name}</option>
        ))}
      </select>

      <input
        type="date"
        name="test_date"
        placeholder="Test Date"
        value={form.test_date}
        onChange={handleChange}
        className="form-control mb-2"
      />

      <input
        type="number"
        name="value"
        placeholder="Value"
        value={form.value}
        onChange={handleChange}
        className="form-control mb-2"
        step="any"
      />

      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <button type="submit" className="btn btn-primary">
          {test ? 'Update' : 'Create'}
        </button>
      </div>
    </form>
  );
}

export default WaterQualityTestForm;
