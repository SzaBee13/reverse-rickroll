# 🤖 Reverse RickRoll Bot

> A Discord bot that hunts down RickRolls, sussy emojis, and sneaky stickers… then flips the script. 🔁💥

## 🔍 What it Detects

- 🎥 YouTube RickRoll links
- 🧾 Stickers in messages
- 😂 Custom emoji names like `:rickroll:` or `:rick-roll:`
- ✏️ Suspicious text phrases, line from the song
- 🔁 And then... flips it back on the sender 😈

## 🛠 Setup
1. Clone the repo
2. Add you token to `.env` file `DISCORD_TOKEN=<token>`

### Docker
1. Docker build: `docker build -t <name> .`
2. Remove and stop previous `docker stop <name> docker rm <name>`
3. Docker run: `docker run --name <name> -d <name>`

### Python
1. Pip install: `pip install -r requirements.txt`
2. Run the bot: `python main.py`