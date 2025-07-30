import React, { useState, useEffect } from "react";
import "./Navbar.css"; // Optional: Add styles for the toggle button

const ThemeToggle = () => {
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    document.body.className = theme;
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
  };

  return (
    <button onClick={toggleTheme} className="theme-toggle">
      Switch to {theme === "light" ? "Dark" : "Light"} Theme
    </button>
  );
};

export default ThemeToggle;
