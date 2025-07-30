import React from "react";

function License() {
  return (
    <div className="container home-hero">
      <h1>License</h1>
      <div className="hero-content column legal">
        <p>Copyright (c) 2025 SzaBee13</p>
        <p>This Discord bot is licensed under the following terms:</p>
        <h2>✅ You MAY:</h2>
        <ul>
          <li>Use this bot <strong>only</strong> for testing, debugging, or contributing to its development.</li>
          <li>Fork, clone, or run the code locally in a dev environment.</li>
          <li>Submit pull requests or suggestions to improve the bot.</li>
        </ul>
        <h2>❌ You may NOT:</h2>
        <ul>
          <li>Use, host, or deploy this bot for public or personal use outside of development purposes.</li>
          <li>Modify and rebrand this bot as your own or redistribute it without permission.</li>
          <li>Use this bot in production unless you are the original creator or have explicit permission.</li>
        </ul>
        <h2>⚠️ Use the original if you're not here to help</h2>
        <p>
          If you're not testing or contributing, go grab the original version <a href="https://reverse-rickroll.pages.dev" target="_blank" rel="noopener noreferrer">here</a>.
          Don't be that guy.
        </p>
        <p>
          This license is intentionally restrictive. For anything beyond development or contribution, contact the original author.
        </p>
      </div>
    </div>
  );
}

export default License;