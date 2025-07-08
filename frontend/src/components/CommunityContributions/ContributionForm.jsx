import React, { useState, useEffect } from "react";

const ContributionForm = ({
  types,
  waterSystems,
  onSubmit,
  initialData,
  onCancel,
}) => {
  const [formData, setFormData] = useState({
    system_id: "",
    contribution_type_id: "",
    amount: "",
    date_recorded: "",
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        system_id: initialData.system_id || "",
        contribution_type_id:
          types.find((t) => t.name === initialData.type)?.id || "",
        amount: initialData.amount || "",
        date_recorded: initialData.date_recorded
          ? initialData.date_recorded.split("T")[0]
          : "",
      });
    } else {
      setFormData({
        system_id: "",
        contribution_type_id: "",
        amount: "",
        date_recorded: "",
      });
    }
  }, [initialData, types]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      system_id: parseInt(formData.system_id),
      contribution_type_id: parseInt(formData.contribution_type_id),
      amount: parseFloat(formData.amount),
      date_recorded: formData.date_recorded,
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Water System:
        <select
          name="system_id"
          value={formData.system_id}
          onChange={handleChange}
          required
        >
          <option value="">Select a water system</option>
          {waterSystems.map((ws) => (
            <option key={ws.id} value={ws.id}>
              {ws.name}
            </option>
          ))}
        </select>
      </label>
      <br />
      <label>
        Contribution Type:
        <select
          name="contribution_type_id"
          value={formData.contribution_type_id}
          onChange={handleChange}
          required
        >
          <option value="">Select a contribution type</option>
          {types.map((type) => (
            <option key={type.id} value={type.id}>
              {type.name}
            </option>
          ))}
        </select>
      </label>
      <br />
      <label>
        Amount:
        <input
          type="number"
          name="amount"
          value={formData.amount}
          onChange={handleChange}
          step="0.01"
          required
        />
      </label>
      <br />
      <label>
        Date Recorded:
        <input
          type="date"
          name="date_recorded"
          value={formData.date_recorded}
          onChange={handleChange}
          required
        />
      </label>
      <br />
      <button type="submit">Submit</button>
      {onCancel && (
        <button type="button" onClick={onCancel}>
          Cancel
        </button>
      )}
    </form>
  );
};

export default ContributionForm;
