import React, { useEffect, useState } from "react";
import axios from "axios";
import SparePartForm from "../components/SparePartsInventory/SparePartForm";
import SparePartList from "../components/SparePartsInventory/SparePartList";

function SparePartsInventory() {
  const [inventory, setInventory] = useState([]);
  const [types, setTypes] = useState([]);
  const [waterSystems, setWaterSystems] = useState([]);
  const [editingPart, setEditingPart] = useState(null);

  const fetchData = async () => {
    try {
      const [typesRes, waterSystemsRes, inventoryRes] = await Promise.all([
        axios.get("/api/spare-parts/types"),
        axios.get("/api/watersystems"),
        axios.get("/api/spare-parts/inventory"),
      ]);
      setTypes(typesRes.data);
      setWaterSystems(waterSystemsRes.data);
      setInventory(inventoryRes.data);
    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Failed to fetch data from server.");
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleEdit = (part) => {
    setEditingPart(part);
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this spare part?")) {
      try {
        await axios.delete(`/api/spare-parts/inventory/${id}`);
        fetchData();
      } catch (error) {
        console.error("Error deleting spare part:", error);
        alert("Failed to delete spare part.");
      }
    }
  };

  const handleSubmit = async (data, resetForm) => {
    try {
      const payload = {
        water_system_id: data.system_id,
        part_type_id: data.part_type_id,
        quantity: data.quantity,
        last_restocked: data.last_restocked
      };
      if (editingPart) {
        await axios.put(`/api/spare-parts/inventory/${editingPart.id}`, payload);
        setEditingPart(null);
      } else {
        await axios.post("/api/spare-parts/inventory", payload);
      }
      resetForm();
      fetchData();
    } catch (error) {
      console.error("Error submitting spare part:", error);
      alert("Failed to submit spare part.");
    }
  };

  return (
    <div className="spare-parts-inventory-container">
      <div className="spare-parts-form">
        <h2>{editingPart ? "Edit" : "Add"} Spare Part Inventory</h2>
        <SparePartForm
          part={editingPart}
          onSubmit={handleSubmit}
          types={types}
          waterSystems={waterSystems}
        />
      </div>
      <div className="spare-parts-list">
        <h3>Spare Parts Inventory</h3>
        <SparePartList
          inventory={inventory}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default SparePartsInventory;
