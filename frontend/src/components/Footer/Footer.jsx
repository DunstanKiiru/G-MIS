import React from "react";
import { NavLink } from "react-router-dom";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="f-wrapper">
      <div className="f-container">
        <div className="f-left">
          <NavLink to="/">
            <img
              src="/garissa.png"
              alt="GARUWASCO Logo"
              width={100}
              className="footer-logo"
            />
          </NavLink>
          <p className="secondaryText">
            GARUWASCO - Garissa Rural Water and Sanitation Corporation <br />
            Safe, adequate and sustainable rural water services
          </p>
        </div>

        <div className="quick-links-section">
          <p className="primaryText mb-2">Quick Links</p>
          <nav className="f-menu vertical-menu">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/waterassets">Assets</NavLink>
            <NavLink to="/about">About</NavLink>
            <NavLink to="/contact">Contact</NavLink>
            <NavLink to="/login">Login</NavLink>
          </nav>
        </div>

        <div className="contact-section">
          <p className="contactText mt-3">
            Garissa, Kenya
            <br />
            P.O BOX 563 - 70100
            <br />
            Email: info@garuwasco.co.ke
          </p>
        </div>
      </div>

      <div className="f-bottom text-center w-100 mt-3">
        <small className="text-muted">
          &copy; {new Date().getFullYear()} Developed by Alex Dunstan Kiiru Mureithi. All Rights Deserved
        </small>
      </div>
    </footer>
  );
};

export default Footer;
