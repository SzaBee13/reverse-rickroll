import React from "react";

function TermsOfService() {
  return (
    <div className="container home-hero">
      <h1>Terms of Service</h1>
      <div className="hero-content column legal">
        <p>
          By using our Discord bot Reverse Rickroll, you agree to the following
          terms:
        </p>
        <ul>
          <li>The Bot is provided "as-is" with no guarantees or warranties.</li>
          <li>
            You may not abuse or misuse the Bot in any form, including spamming,
            exploiting, or reverse engineering.
          </li>
          <li>
            We reserve the right to update, restrict, or remove access to the
            Bot at any time without notice.
          </li>
          <li>
            Your use of the Bot must comply with Discord's{" "}
            <a
              href="https://discord.com/terms"
              target="_blank"
              className="text-blue-500 underline"
            >
              Terms of Service
            </a>{" "}
            and{" "}
            <a
              href="https://discord.com/guidelines"
              target="_blank"
              className="text-blue-500 underline"
            >
              Community Guidelines
            </a>
            .
          </li>
          <li>
            YOU CAN ONLY USE THE BOT IF YOU WANT TO CONTRIBUTE TO THE REPO
          </li>
        </ul>
      </div>
    </div>
  );
}

export default TermsOfService;
