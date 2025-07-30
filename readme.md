# 🤖 Reverse RickRoll Bot

> A Discord bot that hunts down RickRolls, sussy emojis, and sneaky stickers… then flips the script. 🔁💥

## 🔍 What it Detects

- 🎥 YouTube RickRoll links
- 🧾 Stickers in messages
- 😂 Custom emoji names like `:rickroll:` or `:rick-roll:`
- ✏️ Suspicious text phrases, line from the song
- 👀 Files uploaded having a sus name.
- 🔁 And then... flips it back on the sender 😈

## 🛠 Setup Using Docker
NOTE! Please read the [LICENSE](./LICENSE.md) before you use it.
```sh
docker pull szabee13/reverse-rickroll:latest
touch reports.log
nano .env
nano settings.json "{}"
docker run -d \
  --name reverse-rickroll-bot \
  --env-file .env \
  -v "$(pwd)/settings.json:/app/settings.json" \
  -v "$(pwd)/reports.log:/app/reports.log" \
  szabee13/reverse-rickroll:latest

```

## Setting up
1. Use `/settings` command in a guild
