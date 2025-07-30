import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Documentation from "./pages/Documentation";
import PrivacyPolicy from "./pages/PrivacyPolicy";
import TermsOfService from "./pages/TermsOfService";
import Legal from "./pages/Legal";
import License from "./pages/License";
import { useState, useEffect } from "react";
import "./index.css";
import "./themes/light.css";
import "./themes/dark.css";

function Invite() {
  window.location.href =
    "https://discord.com/oauth2/authorize?client_id=1384237022826336316";
  return <div></div>; // This component does not render anything
}

function Docker() {
    window.location.href = "https://hub.docker.com/r/szabee13/reverse-rickroll";
    return <div></div>; // This component does not render anything
}

function GitHub() {
  window.location.href = "https://github.com/szabee13/reverse-rickroll";
  return <div></div>; // This component does not render anything
}

function App() {
  // Load theme from localStorage or default to light
  const [theme, setTheme] = useState(
    () => localStorage.getItem("theme") || "light"
  );

  useEffect(() => {
    document.body.classList.remove("light", "dark");
    document.body.classList.add(theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
  };

  return (
    <div>
      <Router>
        <Navbar toggleTheme={toggleTheme} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/documentation" element={<Documentation />} />
          <Route path="/invite" element={<Invite />} />
          <Route path="/docker" element={<Docker />} />
          <Route path="/github" element={<GitHub />} />
          <Route path="/privacy-policy" element={<PrivacyPolicy />} />
          <Route path="/terms-of-service" element={<TermsOfService />} />
          <Route path="/license" element={<License />} />
          <Route path="/legal" element={<Legal />} />
          <Route path="*" element={<Home />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
