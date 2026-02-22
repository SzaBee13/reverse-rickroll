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
REPORT_CHANNEL_ID = int(os.getenv("REPORT_CHANNEL_ID", 1401097099889872966))  # Default to a specific channel if not set

STATIC_JSON_PATH = "static.json"
if not os.path.exists(STATIC_JSON_PATH):
    with open(STATIC_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({}, f)
        f.close()
    print(f"Created {STATIC_JSON_PATH} with empty content. Please fill it with the required data.")

STATIC_JSON = json.load(open(STATIC_JSON_PATH, "r", encoding="utf-8"))

DECOY_LINKS = STATIC_JSON.get("decoy_links")

ROAST_MESSAGES = STATIC_JSON.get("roast_messages")

SUS_EMOJIS = STATIC_JSON.get("sus_emojis")

SUS_TEXT_PHRASES = STATIC_JSON.get("sus_text_phrases")

SUS_FILE_KEYWORDS = STATIC_JSON.get("sus_file_keywords")

SUS_FILE_EXTENSIONS = STATIC_JSON.get("sus_file_extensions")

SUS_LINKS = STATIC_JSON.get("sus_links", [])

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_settings = {}
default_triggers = STATIC_JSON.get("default_triggers")
disabled_triggers = STATIC_JSON.get("disabled_triggers")

def has_sus_file_upload(message):
    for attachment in message.attachments:
        filename = attachment.filename.lower()
        if any(kw in filename for kw in SUS_FILE_KEYWORDS) and any(filename.endswith(ext) for ext in SUS_FILE_EXTENSIONS):
            return True, filename
    return False, None

def has_sus_text(content):
    content_lower = content.lower().replace("'", "").replace("’", "").replace("_", " ").replace("-", " ").replace(":", " ").replace(";", " ").replace(",", " ").replace(".", " ").replace("+", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("  ", " ")
    return any(phrase in content_lower for phrase in SUS_TEXT_PHRASES)

def get_random_response(mention):
    bait = random.choice(DECOY_LINKS)
    return random.choice(ROAST_MESSAGES).format(mention=mention, bait=bait)

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
        print("🔧 Loaded guild settings from settings.json")
        f.close()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content or ""
    gid = message.guild.id if message.guild else None
    has_link = any(link in content for link in SUS_LINKS)
    has_sticker = bool(message.stickers)
    has_emojis = has_sus_rick_emoji(content)
    has_sus_text_content = has_sus_text(content)
    has_sus_file, sus_filename = has_sus_file_upload(message)
    settings = guild_settings.get(gid, default_triggers)

    if (has_link and settings["link"]) or (has_sticker and settings["sticker"]) or (has_emojis and settings["emoji"]) or (has_sus_text_content and settings["text"]) or (has_sus_file and settings["file"]):
        try:
            if has_link and settings["link"]:
                await message.delete()
                roast = get_random_response(message.author.mention)
            elif has_sticker and settings["sticker"]:
                await message.delete()
                roast = f"🎟️ {message.author.mention} tried to sneak a sticker past me... I SEE YOU 👁️\n<{random.choice(DECOY_LINKS)}>"
            elif has_emojis and settings["emoji"]:
                await message.delete()
                roast = f"😏 Emojis won’t save you, {message.author.mention}… reverse time: <{random.choice(DECOY_LINKS)}>"
            elif has_sus_text_content and settings["text"]:
                await message.delete()
                roast = f"📜 Quoting ancient meme scrolls won’t save you, {message.author.mention}!\n<{random.choice(DECOY_LINKS)}>"
            elif has_sus_file and settings["file"]:
                await message.delete()
                roast = f"📁 A wild *sussy file* appeared: `{sus_filename}`\n{message.author.mention}, reverse time!\n<{random.choice(DECOY_LINKS)}>"
            else:
                return  # No valid trigger foud
            
            if not roast:
                return
            msg = await message.channel.send(roast)
            await msg.add_reaction("💀")
            await msg.add_reaction("👀")

        except Exception as e:
            print("Error:", e)

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

  if emoji == None and text == None and sticker == None and file == None and video == None:
    await interaction.response.send_message(
      f"No changes made. The current settings are:\n```json\n{updated}```",
      ephemeral=True
    )
    return

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
    
    report_channel = client.get_channel(REPORT_CHANNEL_ID)
    if report_channel:
        try:
            embed = discord.Embed(
                title="New Report",
                description=message,
                color=discord.Color.red()
            )
            embed.add_field(name="User", value=f"{interaction.user} (ID: {interaction.user.id})", inline=False)
            embed.add_field(name="Guild", value=f"{interaction.guild.name} (ID: {interaction.guild.id})", inline=False)
            await report_channel.send("New report received!", embed=embed)
        except Exception as e:
            print(f"❌ Could not send report to the report channel: {e}")

@tree.command(name="ping", description="Check the bot's latency.")
async def ping_command(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! Latency: {latency}ms", ephemeral=True)

@tree.command(name="enable", description="Enable all detection type.")
async def enable_command(interaction: discord.Interaction):
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
        "✅ All settings have been enabled.",
        ephemeral=True
    )

@tree.command(name="disable", description="Disable all detection type")
async def disable_command(interaction: discord.Integration):
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
    guild_settings[gid] = disabled_triggers.copy()

    # Write the updated settings back to the file
    with open("settings.json", "w") as f:
        json.dump(guild_settings, f, indent=2)

    await interaction.response.send_message(
        "✅ All settings have been disabled.",
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