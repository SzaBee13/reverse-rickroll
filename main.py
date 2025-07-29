import discord
import re
import requests
import random
import os
import json
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

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
    "never gonna",
    
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

SUS_FILE_KEYWORDS = [
    "rickroll", "rick", "roll", "rick_roll", "rick-roll"
]

SUS_FILE_EXTENSIONS = [
    ".mp4", ".mov", ".avi", ".webm", ".mkv", ".gif",
    "png", "jpeg", "jpg", "svg", "webp"
]

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_settings = {}
default_triggers = {
  "emoji": True,
  "text": True,
  "sticker": True,
  "file": True,
  "video": True
}

def has_sus_file_upload(message):
    for attachment in message.attachments:
        filename = attachment.filename.lower()
        if any(kw in filename for kw in SUS_FILE_KEYWORDS) and any(filename.endswith(ext) for ext in SUS_FILE_EXTENSIONS):
            return True, filename
    return False, None

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
    await tree.sync()

    # 👀 Set presence
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Rick Astley - Never Gonna Give You Up"
    )
    await client.change_presence(activity=activity)
    
    # Import guild settings from file
    global guild_settings
    with open("settings.json", "r") as f:
        guild_settings = json.load(f)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content or ""
    gid = message.guild.id if message.guild else None
    video_id = extract_video_id(content)
    is_roll = video_id and is_rickroll(video_id)
    has_sticker = bool(message.stickers)
    has_emojis = has_sus_rick_emoji(content)
    has_sus_text_content = has_sus_text(content)
    has_sus_file, sus_filename = has_sus_file_upload(message)
    settings = guild_settings.get(gid, default_triggers)

    if is_roll or has_sticker or has_emojis or has_sus_text_content or has_sus_file:
        try:
            await message.delete()

            if is_roll and settings["video"]:
                roast = get_random_response(message.author.mention)
            elif has_sticker and settings["sticker"]:
                roast = f"🎟️ {message.author.mention} tried to sneak a sticker past me... I SEE YOU 👁️\n<{random.choice(DECOY_LINKS)}>"
            elif has_emojis and settings["emoji"]:
                roast = f"😏 Emojis won’t save you, {message.author.mention}… reverse time: <{random.choice(DECOY_LINKS)}>"
            elif has_sus_text_content and settings["text"]:
                roast = f"📜 Quoting ancient meme scrolls won’t save you, {message.author.mention}!\n<{random.choice(DECOY_LINKS)}>"
            elif has_sus_file and settings["file"]:
                roast = f"📁 A wild *sussy file* appeared: `{sus_filename}`\n{message.author.mention}, reverse time!\n<{random.choice(DECOY_LINKS)}>"
            else:
                return  # No valid trigger found
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

@tree.command(name="settings", description="Update detection settings for your server!")
@app_commands.describe(
    emoji="Detect emoji-based RickRolls",
    text="Detect sus text lyrics",
    sticker="Detect stickers",
    file="Detect sus file uploads",
    video="Detect YouTube links"
)
async def settings_command(interaction: discord.Interaction,
    emoji: bool = None,
    text: bool = None,
    sticker: bool = None,
    file: bool = None,
    video: bool = None):
  if not interaction.guild:
    await interaction.response.send_message(
      "❌ This command can only be used in a server!",
      ephemeral=True
    )
    return

  if not interaction.user.guild_permissions.administrator:
    await interaction.response.send_message(
      "🚫 You must be an admin to use this command!",
      ephemeral=True
    )
    return

  gid = interaction.guild.id
  
  if gid not in guild_settings:
    guild_settings[gid] = default_triggers.copy()

  updated = guild_settings[gid]

  if emoji is not None: updated["emoji"] = emoji
  if text is not None: updated["text"] = text
  if sticker is not None: updated["sticker"] = sticker
  if file is not None: updated["file"] = file
  if video is not None: updated["video"] = video

  # write in ./settings.json
  with open("settings.json", "w") as f:
    json.dump(guild_settings, f, indent=2)

  await interaction.response.send_message(
    f"✅ Updated settings:\n```json\n{updated}```",
    ephemeral=True
  )

@tree.command(name="report", description="Report an issue or send feedback to the bot owner.")
@app_commands.describe(message="Describe your issue or feedback")
async def report_command(interaction: discord.Interaction, message: str):
    if not interaction.guild:
        await interaction.response.send_message(
            "❌ You can only send reports from within a server.",
            ephemeral=True
        )
        return

    # Log to file
    log_entry = {
        "user": str(interaction.user),
        "user_id": interaction.user.id,
        "guild": str(interaction.guild),
        "guild_id": interaction.guild.id,
        "message": message,
    }

    with open("reports.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    await interaction.response.send_message("✅ Your report has been logged. Thanks!", ephemeral=True)

    # Optional: also send to you via DM
    owner = await client.fetch_user(OWNER_ID)
    if owner:
        try:
            await owner.send(f"📨 New report from {interaction.user} in {interaction.guild.name}:\n```\n{message}\n```")
        except:
            print("❌ Could not DM the owner.")

@tree.command(name="ping", description="Check the bot's latency.")
async def ping_command(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! Latency: {latency}ms", ephemeral=True)

@tree.command(name="reset", description="Reset the bot's settings for this server.")
async def reset_command(interaction: discord.Interaction):
    if not interaction.guild:
        await interaction.response.send_message(
            "❌ This command can only be used in a server!",
            ephemeral=True
        )
        return

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "🚫 You must be an admin to use this command!",
            ephemeral=True
        )
        return

    gid = interaction.guild.id
    guild_settings[gid] = default_triggers.copy()

    # Write the updated settings back to the file
    with open("settings.json", "w") as f:
        json.dump(guild_settings, f, indent=2)

    await interaction.response.send_message(
        "✅ Settings have been reset to default.",
        ephemeral=True
    )

# If the bot gets kicked or removed from a server, remove its settings
@client.event
async def on_guild_remove(guild):
    if guild.id in guild_settings:
        del guild_settings[guild.id]
        # Write the updated settings back to the file
        with open("settings.json", "w") as f:
            json.dump(guild_settings, f, indent=2)

client.run(TOKEN)