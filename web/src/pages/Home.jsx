import React from "react";

const Home = () => {
  return (
    <div className="container home-hero">
      <div className="hero-content">
        <img
          src="https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif"
          alt="Rick Astley dancing"
          className="hero-img"
        />
        <div>
          <h1>Reverse RickRoll Bot 🤖</h1>
          <p className="lead">
            The Discord bot that <b>hunts down RickRolls</b>, sussy emojis, and
            sneaky stickers… then flips the script!
          </p>
          <a
            href="https://github.com/szabee13/reverse-rickroll"
            className="cta-btn"
            target="_blank"
            rel="noopener noreferrer"
          >
            View on GitHub
          </a>
          <a
            href="https://dockerhub.com/szabee13/reverse-rickroll"
            className="cta-btn"
            target="_blank"
            rel="noopener noreferrer"
          >
            View on Docker Hub
          </a>
        </div>
      </div>
      <section className="features">
        <h2>✨ Features</h2>
        <ul>
          <li>Detects YouTube RickRoll links</li>
          <li>Identifies stickers and custom emojis</li>
          <li>Recognizes suspicious text phrases</li>
          <li>Responds with humorous messages and decoy links</li>
        </ul>
      </section>
      <section>
        <h2>🚀 Getting Started</h2>
        <p>
          Clone the repository and follow the instructions in <b>README.md</b>.
          <br />
          You can run the bot using <b>Docker</b> or <b>Python</b>.
        </p>
        <div className="logos">
          <img src="/discord.png" alt="Discord logo" className="discord-img" />
        </div>
      </section>
    </div>
  );
};

export default Home;
