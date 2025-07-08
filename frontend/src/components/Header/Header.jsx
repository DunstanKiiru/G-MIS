import React, { useState, useEffect } from "react";
import { NavLink, useNavigate } from "react-router-dom";

import "./Header.css";

const Header = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    setIsLoggedIn(!!token);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setIsLoggedIn(false);
    navigate('/login');
  };

  return (
    <section className="h-wrapper">
      <div className="h-container">
        <NavLink to="/">
          <img src="/garissa.png" alt="MIS logo" width={100} className="logo" />
        </NavLink>
      </div>

      <div className="h-menu">
        <NavLink to="/" end>
          Home
        </NavLink>
        <NavLink to="/waterassets">Assets</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/contact">Contact</NavLink>
        {isLoggedIn && (
          <>
            <NavLink to="/omvisits">OM Visits</NavLink>
            <NavLink to="/sparepartsinventory">Spare Parts Inventory</NavLink>
            <NavLink to="/staffdevelopment">Staff Development</NavLink>
            <NavLink to="/waterquality">Water Quality</NavLink>
          </>
        )}
        {!isLoggedIn ? (
          <NavLink to="/login" className="btn btn-outline-primary mt-2">
            Login
          </NavLink>
        ) : (
          <button onClick={handleLogout} className="btn btn-outline-danger mt-2">
            Logout
          </button>
        )}
      </div>
    </section>
  );
};

export default Header;
