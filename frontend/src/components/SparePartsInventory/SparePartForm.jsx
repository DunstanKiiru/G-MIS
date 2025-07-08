import React, { useState, useEffect } from 'react';

const initialState = {
  system_id: '',
  part_type_id: '',
  quantity: '',
  last_restocked: ''
};

function SparePartForm({ part, onSubmit, types, waterSystems }) {
  const [form, setForm] = useState(initialState);

  useEffect(() => {
    if (part) {
      setForm({
        system_id: part.water_system_id || '',
        part_type_id: part.part_type_id || '',
        quantity: part.quantity || '',
        last_restocked: part.last_restocked ? part.last_restocked.slice(0, 10) : ''
      });
    } else {
      setForm(initialState);
    }
  }, [part]);

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
        name="part_type_id"
        value={form.part_type_id}
        onChange={handleChange}
        className="form-select mb-2"
        required
      >
        <option value="">Select Part Type</option>
        {types.map(type => (
          <option key={type.id} value={type.id}>{type.name}</option>
        ))}
      </select>

      <input
        type="number"
        name="quantity"
        placeholder="Quantity"
        value={form.quantity}
        onChange={handleChange}
        className="form-control mb-2"
      />

      <input
        type="date"
        name="last_restocked"
        placeholder="Last Restocked"
        value={form.last_restocked}
        onChange={handleChange}
        className="form-control mb-2"
      />

      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <button type="submit" className="btn btn-primary">
          {part ? 'Update' : 'Create'}
        </button>
      </div>
    </form>
  );
}

export default SparePartForm;
