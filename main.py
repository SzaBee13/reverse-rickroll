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

ROAST_MESSAGES = [
    "🎯 {mention}, *caught red-handed*! Enjoy this instead: <{bait}>",
    "😈 Oops {mention}, your meme magic just got reversed. Here's a spicy one: <{bait}>",
    "🚨 RICKROLL DETECTED! {mention}, time to taste your own medicine: <{bait}>",
    "🎶 No no no... Not today, {mention}. Here's your punishment gift: <{bait}>",
    "🌀 Reverse Roll Engaged! {mention}, now feel the wrath: <{bait}>",
    "💀 You thought you were slick, {mention}... But you just got bamboozled: <{bait}>",
]

SUS_EMOJIS = [
    "rickroll", "rick", "roll", "rick_roll", "rick-roll"
]

SUS_TEXT_PHRASES = [
    "give you up",
    "nggyu",
    "rick roll",
    "never gonna"
    
    "we're no strangers to love",
    "You know the rules and so do I",
    "A full commitment's what I'm thinkin' of",
    "You wouldn't get this from any other guy",
    
    "I just wanna tell you how I'm feeling",
    "Gotta make you understand",
    
    "never gonna give you up",
    "never gonna let you down",
    "never gonna run around and desert you",
    "never gonna make you cry",
    "never gonna say goodbye",
    "never gonna tell a lie and hurt you",
    
    "We've known each other for so long",
    "Your heart's been aching, but you're too shy to say it",
    "Inside, we both know what's been going on",
    "We know the game and we're gonna play it",
    
    "And if you ask me how I'm feeling",
    "Don't tell me you're too blind to see"
]

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)

def has_sus_text(content):
    content_lower = content.lower()
    return any(phrase in content_lower for phrase in SUS_TEXT_PHRASES)

def get_random_response(mention):
    bait = random.choice(DECOY_LINKS)
    return random.choice(ROAST_MESSAGES).format(mention=mention, bait=bait)

def extract_video_id(message):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", message)
    return match.group(1) if match else None

def is_rickroll(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        resp = requests.get(f"https://noembed.com/embed?url={url}")
        if resp.status_code == 200:
            title = resp.json().get("title", "").lower()
            return "rick astley" in title or "never gonna give you up" in title
    except Exception as e:
        print("Error checking RickRoll:", e)
    return False

def has_sus_rick_emoji(content):
    # Match all :emoji_name: things
    matches = re.findall(r":([a-zA-Z0-9_\-]+):", content)
    return any(name.lower() in SUS_EMOJIS for name in matches)

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

    content = message.content or ""
    video_id = extract_video_id(content)
    is_roll = video_id and is_rickroll(video_id)
    has_sticker = bool(message.stickers)
    has_emojis = has_sus_rick_emoji(content)
    has_sus_text_content = has_sus_text(content)

    if is_roll or has_sticker or has_emojis or has_sus_text_content:
        try:
            await message.delete()

            if is_roll:
                roast = get_random_response(message.author.mention)
            elif has_sticker:
                roast = f"🎟️ {message.author.mention} tried to sneak a sticker past me... I SEE YOU 👁️\n<{random.choice(DECOY_LINKS)}>"
            elif has_emojis:
                roast = f"😏 Emojis won’t save you, {message.author.mention}… reverse time: <{random.choice(DECOY_LINKS)}>"
            elif has_sus_text_content:
                roast = f"📜 Quoting ancient meme scrolls won’t save you, {message.author.mention}!\n{random.choice(DECOY_LINKS)}"

            msg = await message.channel.send(roast)
            await msg.add_reaction("💀")
            await msg.add_reaction("🍆")
            await msg.add_reaction("👀")

        except Exception as e:
            print("Error:", e)

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