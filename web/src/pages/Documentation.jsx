import React from "react";

const Documentation = () => {
  return (
    <div className="documentation container">
      <h1>Documentation</h1>
      <div>
        <h1 id="-reverse-rickroll-bot">🤖 Reverse RickRoll Bot</h1>
        <blockquote>
          <p>
            A Discord bot that hunts down RickRolls, sussy emojis, and sneaky
            stickers… then flips the script. 🔁💥
          </p>
        </blockquote>
        <h2 id="what-it-detects">🔍 What it Detects</h2>
        <ul>
          <li>🎥 YouTube RickRoll links</li>
          <li>🧾 Stickers in messages</li>
          <li>
            😂 Custom emoji names like <code>:rickroll:</code> or{" "}
            <code>:rick-roll:</code>
          </li>
          <li>✏️ Suspicious text phrases, line from the song</li>
          <li>👀 Files uploaded having a sus name.</li>
          <li>🔁 And then... flips it back on the sender 😈</li>
        </ul>
        <h2 id="setup-using-docker">🛠 Setup Using Docker</h2>
        <p>NOTE! YOU CAN ONLY USE THE SOFTWARE FOR YOURSELF IF YOU WANT TO CONTRIBUTE TO THE REPO FOR TEST ELSE PLEASE USE THE OFFICIAL REPO</p>
        <pre>
          <code class="lang-sh">
            docker pull szabee13/reverse-rickroll:latest touch reports
            <span class="hljs-selector-class">.log</span>
            nano <span class="hljs-selector-class">.env</span>
            nano settings<span class="hljs-selector-class">.json</span>{" "}
            <span class="hljs-string">"{}"</span>
            docker run -d \ --name reverse-rickroll-bot \ --env-file{" "}
            <span class="hljs-selector-class">.env</span> \ -v{" "}
            <span class="hljs-string">
              "$(pwd)/settings.json:/app/settings.json"
            </span>{" "}
            \ -v{" "}
            <span class="hljs-string">
              "$(pwd)/reports.log:/app/reports.log"
            </span>{" "}
            \ szabee13/reverse-rickroll:latest
          </code>
        </pre>
        <h2 id="setting-up">Setting up</h2>
        <ol>
          <li>
            Use <code>/settings</code> command in a guild
          </li>
        </ol>
      </div>
    </div>
  );
};

export default Documentation;
