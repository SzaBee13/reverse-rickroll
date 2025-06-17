import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = ({ toggleTheme }) => {
    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to="/" className="navbar-logo">Reverse RickRoll Bot</Link>
            </div>
            <div className="navbar-links">
                <Link to="/" className="navbar-link">Home</Link>
                <Link to="/documentation" className="navbar-link">Documentation</Link>
            </div>
            <a
                href="https://szabee13.pages.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="navbar-link"
                style={{ fontWeight: "bold" }}
            >
                szabee13
            </a>
            <button className="theme-toggle-btn" onClick={toggleTheme}>
                Toggle Theme
            </button>
        </nav>
    );
};

export default Navbar;