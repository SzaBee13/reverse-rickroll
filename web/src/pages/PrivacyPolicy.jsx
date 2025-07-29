import React from "react";

function PrivacyPolicy() {
  return (
    <div className="container home-hero">
      <h1>Privacy Policy</h1>
      <div className="hero-content column legal">
        <p>This bot may collect the following data:</p>
        <ul>
          <li>Guild IDs and settings for configuration purposes.</li>
          <li>
            Message content only when necessary for moderation (e.g. detecting
            RickRolls).
          </li>
          <li>No personal or sensitive data is stored permanently.</li>
        </ul>
        <p>
          Data is stored securely and only used to improve the Bot’s
          functionality. We do not sell or share your data with third parties.
        </p>
        <p>
          If you wish to remove your server's data, please contact the bot owner
          via Discord.
        </p>
      </div>
    </div>
  );
}

export default PrivacyPolicy;
