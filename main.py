import discord
import re
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 🎣 Decoy links – reverse bait!
DECOY_LINKS = [
    "https://youtu.be/IwzUs1IMdyQ",   # Crab Rave
    "https://youtu.be/KxGRhd_iWuE",   # The Duck Song
    "https://youtu.be/tVj0ZTS4WF4",   # Sneaky roll
    "https://youtu.be/dQw4w9WgXcQ?t=43", # RickRoll twist
    "https://youtu.be/oHg5SJYRHA0",   # Classic RickAstley
    "https://youtu.be/j5a0jTc9S10",   # Nyan Cat
]

# 🗣️ Snappy replies to pranksters
RESPONSES = [
    "🎯 {mention}, *caught red-handed*! Enjoy this instead: <{bait}>",
    "😈 Oops {mention}, your meme magic just got reversed. Here's a spicy one: <{bait}>",
    "🚨 RICKROLL DETECTED! {mention}, time to taste your own medicine: <{bait}>",
    "🎶 No no no... Not today, {mention}. Here's your punishment gift: <{bait}>",
    "🌀 Reverse Roll Engaged! {mention}, now feel the wrath: <{bait}>",
    "💀 You thought you were slick, {mention}... But you just got bamboozled: <{bait}>",
]

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)

def is_rickroll(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        resp = requests.get(f"https://noembed.com/embed?url={url}")
        if resp.status_code == 200:
            title = resp.json().get("title", "").lower()
            return "rick astley" in title or "never gonna give you up" in title
    except Exception as e:
        print("Error:", e)
    return False

def extract_video_id(message):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", message)
    return match.group(1) if match else None

def get_random_response(mention):
    bait = random.choice(DECOY_LINKS)
    response = random.choice(RESPONSES)
    return response.format(mention=mention, bait=bait)

@client.event
async def on_ready():
    print(f"✅ Bot is online as {client.user}!")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content
    if "youtube.com" in content or "youtu.be" in content:
        video_id = extract_video_id(content)
        if video_id and is_rickroll(video_id):
            try:
                await message.delete()
                roast = get_random_response(message.author.mention)
                await message.channel.send(roast)
            except discord.Forbidden:
                print("❌ Missing permissions to delete messages.")
            except Exception as e:
                print(f"⚠️ Error: {e}")

client.run(TOKEN)
