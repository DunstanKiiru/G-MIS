import React, { useState, useEffect } from "react";

const initialState = {
    name: "",
    asset_type: "",
    installation_date: "",
    material: "",
    capacity: "",
    location: "",
    latitude: "",
    longitude: "",
    status: "",
    last_maintenance: ""
}

function AssetForm({asset, onSubmit}){
    const [form, setForm] = useState(initialState)

    useEffect(() => {
        if (asset) setForm(asset)
        else setForm(initialState)
    }, [asset])

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        onSubmit(form, () => setForm(initialState))
    }

    return(
        <form onSubmit={handleSubmit}>
            {Object.keys(form).map((field) => (
                <input
                    key={field}
                    name={field}
                    placeholder={field}
                    value={form[field]}
                    onChange={handleChange}
                />
            ))}
            <button type="Submit">{asset ? 'Update': 'Create'}</button>

        </form>
    )
}


export default AssetForm