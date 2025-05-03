import React from "react";
import "./Navbar.css";

const Navbar: React.FC = () => {
  return (
    <header className="navbar">
      <div className="logo">Rejoyn</div>
      <nav className="menu">
        <ul>
          <li>
            <a href="/register">Register</a>
          </li>
          <li>
            <a href="/login">Login</a>
          </li>
          <li>
            <a href="/tripform">TripForm</a>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
