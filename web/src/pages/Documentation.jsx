import React from "react";

const Documentation = () => {
    return (
        <div className="documentation container">
            <h1>Documentation</h1>
            <div>
                <h1 id="-reverse-rickroll-bot">🤖 Reverse RickRoll Bot</h1>
                <blockquote>
                    <p>
                        A Discord bot that hunts down RickRolls, sussy emojis,
                        and sneaky stickers… then flips the script. 🔁💥
                    </p>
                </blockquote>
                <h2 id="-what-it-detects">🔍 What it Detects</h2>
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
                <h2 id="-setup">🛠 Setup</h2>
                <ol>
                    <li>Clone the repo</li>
                    <li>
                        Add you token to <code>.env</code> file{" "}
                        <code>DISCORD_TOKEN=&lt;token&gt;</code>
                    </li>
                </ol>
                <h3 id="docker">Docker</h3>
                <ol>
                    <li>
                        Docker build:{" "}
                        <code>docker build -t &lt;name&gt; .</code>
                    </li>
                    <li>
                        Remove and stop previous{" "}
                        <code>
                            docker stop &lt;name&gt; docker rm &lt;name&gt;
                        </code>
                    </li>
                    <li>
                        Docker run:{" "}
                        <code>
                            docker run --name &lt;name&gt; -d &lt;name&gt;
                        </code>
                    </li>
                </ol>
                <h3 id="python">Python</h3>
                <ol>
                    <li>
                        Pip install:{" "}
                        <code>pip install -r requirements.txt</code>
                    </li>
                    <li>
                        Run the bot: <code>python main.py</code>
                    </li>
                </ol>
            </div>
        </div>
    );
};

export default Documentation;
