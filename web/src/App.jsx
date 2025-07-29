import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Documentation from "./pages/Documentation";
import { useState, useEffect } from "react";
import "./index.css";
import "./themes/light.css";
import "./themes/dark.css";

function Invite() {
    window.location.href = "https://discord.com/oauth2/authorize?client_id=1384237022826336316";
    return (<div></div>); // This component does not render anything
}

function App() {
    // Load theme from localStorage or default to light
    const [theme, setTheme] = useState(() => localStorage.getItem("theme") || "light");

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
                </Routes>
            </Router>
        </div>
    );
}

export default App;