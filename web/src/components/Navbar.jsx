import { Link } from "react-router-dom";
import { useState, useEffect, useRef } from "react";
import "./Navbar.css";

const MOBILE_BREAKPOINT = 768; // px

const Navbar = ({ toggleTheme }) => {
  const [open, setOpen] = useState(window.innerWidth >= MOBILE_BREAKPOINT);
  const linksRef = useRef(null);

  // Handle window resize to update open state
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= MOBILE_BREAKPOINT) {
        setOpen(true);
      } else {
        setOpen(false);
      }
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    if (linksRef.current) {
      linksRef.current.style.display = open ? "flex" : "none";
    }
  }, [open]);

  // Only close nav on mobile after clicking a link
  const handleNavLinkClick = () => {
    if (window.innerWidth < MOBILE_BREAKPOINT) {
      setOpen(false);
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/" className="navbar-logo">
          Reverse RickRoll Bot
        </Link>
      </div>
      <button
        className="hamburger"
        aria-label="Toggle menu"
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
        style={{
          display: window.innerWidth < MOBILE_BREAKPOINT ? "flex" : "none",
        }}
      >
        <span />
        <span />
        <span />
      </button>
      <div className="navbar-links" id="navbar-links" ref={linksRef}>
        <Link to="/" className="navbar-link" onClick={handleNavLinkClick}>
          Home
        </Link>
        <Link
          to="/documentation"
          className="navbar-link"
          onClick={handleNavLinkClick}
        >
          Documentation
        </Link>
        <Link to="/invite" className="navbar-link" onClick={handleNavLinkClick} target="_blank" rel="noopener noreferrer">
          Invite
        </Link>
        <Link to="/discord" className="navbar-link" onClick={handleNavLinkClick} target="_blank" rel="noopener noreferrer">
          Discord Server
        </Link>
        <Link to="/legal" className="navbar-link" onClick={handleNavLinkClick}>
          Legal
        </Link>
        <a
          href="https://szabee13.pages.dev"
          target="_blank"
          rel="noopener noreferrer"
          className="navbar-link"
          style={{ fontWeight: "bold" }}
          onClick={handleNavLinkClick}
        >
          Creator
        </a>
        <button className="theme-toggle-btn" onClick={toggleTheme}>
          Toggle Theme
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
