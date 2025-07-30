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
        <a href="https://discord.com/terms"target="_blank">
          Discord Terms of Service
        </a>
        <a href="https://discord.com/guidelines"target="_blank">
          Discord Community Guidelines
        </a>
        <Link to="/license">
          License
        </Link>
        <Link to="/privacy-policy">
          Privacy Policy
        </Link>
        <Link to="/terms-of-service">
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
