import discord
import re
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

DECOY_LINKS = [
    "https://youtu.be/IwzUs1IMdyQ",
    "https://youtu.be/KxGRhd_iWuE",
    "https://youtu.be/tVj0ZTS4WF4",
    "https://youtu.be/dQw4w9WgXcQ?t=43",
    "https://youtu.be/oHg5SJYRHA0",
    "https://youtu.be/j5a0jTc9S10",
]

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

def extract_video_id(message):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", message)
    return match.group(1) if match else None

def is_rickroll_video(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        resp = requests.get(f"https://noembed.com/embed?url={url}")
        if resp.status_code == 200:
            title = resp.json().get("title", "").lower()
            return "rick astley" in title or "never gonna give you up" in title
    except:
        pass
    return False

def is_rickroll_image_url(url):
    url = url.lower()
    triggers = ["rick", "roll", "astley", "never_gonna", "never-gonna", "nevergonnagive"]
    return any(trigger in url for trigger in triggers)

def get_random_response(mention):
    bait = random.choice(DECOY_LINKS)
    return random.choice(RESPONSES).format(mention=mention, bait=bait)

@client.event
async def on_ready():
    print(f"✅ Bot is online as {client.user}!")

    # 👀 Set presence
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Rick Astley - Never Gonna Give You Up"
    )
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Check message content for YouTube RickRoll
    video_id = extract_video_id(message.content)
    if video_id and is_rickroll_video(video_id):
        await handle_rickroll(message)
        return

    # Check for RickRoll-y image links
    urls = re.findall(r'(https?://\S+)', message.content)
    for url in urls:
        if is_rickroll_image_url(url):
            await handle_rickroll(message)
            return

    # Check image attachments
    for attachment in message.attachments:
        if is_rickroll_image_url(attachment.filename) or is_rickroll_image_url(attachment.url):
            await handle_rickroll(message)
            return

async def handle_rickroll(message):
    try:
        await message.delete()
        roast = get_random_response(message.author.mention)
        await message.channel.send(roast)
    except discord.Forbidden:
        print("❌ Missing permissions to delete messages.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

client.run(TOKEN)