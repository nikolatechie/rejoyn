import React from 'react';
import './Navbar.css';

const Navbar: React.FC = () => {
  return (
    <header className="navbar">
      <div className="logo">Rejoyn</div>
      <nav className="menu">
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
