# 🤖 Reverse RickRoll Bot

> A Discord bot that hunts down RickRolls, sussy emojis, and sneaky stickers… then flips the script. 🔁💥

## 🔍 What it Detects

- 🎥 YouTube RickRoll links
- 🧾 Stickers in messages
- 😂 Custom emoji names like `:rickroll:` or `:rick-roll:`
- ✏️ Suspicious text phrases, line from the song
- 👀 Files uploaded having a sus name.
- 🔁 And then... flips it back on the sender 😈

## 🛠 Setup
1. Clone the repo
2. Add you token to `.env` file `DISCORD_TOKEN=<token>`
3. Create a settings.json file
```json
{}
```
NOTE! YOU CAN ONLY USE ITS (for yourself) IF YOU WANT TO CONTRIBUTE TO THE REPO
YOU CAN STILL INVITE THE ORIGINAL BOT TO THE SERVER

### Docker
1. Docker build: `docker build -t <name> .`
2. Remove and stop previous `docker stop <name> docker rm <name>`
3. Docker run: `docker run --name <name> -d <name>`

### Python
1. Pip install: `pip install -r requirements.txt`
2. Run the bot: `python main.py`

## Setting up
1. Use `/settings` command in a guild