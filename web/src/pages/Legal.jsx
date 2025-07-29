import React from "react";
import { Link } from "react-router-dom";

function Legal() {
  return (
    <div className="container home-hero">
      <h1>Legal</h1>
      <div className="hero-content column">
        <p>
          This is a legal document for the Reverse Rickroll Discord bot.
        </p>
        <a href="https://discord.com/terms" target="_blank" className="text-blue-500 underline">
          Discord Terms of Service
        </a>
        <br />
        <a href="https://discord.com/guidelines" target="_blank" className="text-blue-500 underline">
          Discord Community Guidelines
        </a>
        <br />
        <Link to="/privacy-policy" className="text-blue-500 underline">
          Privacy Policy
        </Link>
        <br />
        <Link to="/terms-of-service" className="text-blue-500 underline">
          Terms of Service
        </Link>
        <p>
          By using this bot, you agree to abide by these legal documents.
        </p>
      </div>
    </div>
  );
}

export default Legal;
