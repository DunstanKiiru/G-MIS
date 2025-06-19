import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

const Header = () => {
  return (
    <section className="h-wrapper">
      <div className="Columncenter  h-container">
        <img src="/garissa.png" alt="MIS logo" width={100} />
      </div>

      <div className="ColumnCenter h-menu">
        <Link to="/">Home</Link>
        <Link to="/waterassets">Assets</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
        <Link to="/login" className="btn btn-outline-primary mt-2">
          Login
        </Link>
      </div>
    </section>
  );
};

export default Header;
