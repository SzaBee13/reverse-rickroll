import React from "react";

function Beta() {
  return (
    <div className="container home-hero">
      <div className="hero-content">
        <h1>Beta Bot</h1>
        <a
          href="https://discord.com/oauth2/authorize?client_id=1401481064144441364"
          className="cta-btn"
          target="_blank"
          rel="noopener noreferrer"
        >
          Invite
        </a>
        <p>
          NOTE: ADMIN IS FOR TESTING WE DON'T WANNA DO THE ROLES DIFFERENTLY
        </p>
        <p>Beta testing is for developers, contributors, etc.</p>
        <p>The beta 99% to have bugs in it</p>
      </div>
    </div>
  );
}

export default Beta;
