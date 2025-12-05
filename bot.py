import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

NCSPC_URL = "https://blurzzud.github.io/NCRP/NCSPC.txt"

def split_text(text, limit=2000):
    chunks = []
    while len(text) > limit:
        split_index = text.rfind("\n", 0, limit)
        if split_index == -1:
            split_index = limit
        chunks.append(text[:split_index])
        text = text[split_index:]
    chunks.append(text)
    return chunks

def format_ncspc_markdown(text):
    lines = text.split("\n")
    formatted_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("TITLE"):
            formatted_lines.append(f"**{stripped}**")
        elif stripped.startswith("§"):
            formatted_lines.append(f"`{stripped}`")
        else:
            formatted_lines.append(stripped)
    return "\n".join(formatted_lines)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.tree.command(name="penalcode", description="Display the New California State Penal Code")
async def penalcode(interaction: discord.Interaction):
    await interaction.response.defer()
    response = requests.get(NCSPC_URL)
    if response.status_code == 200:
        text = response.text
        markdown_text = format_ncspc_markdown(text)
        chunks = split_text(markdown_text)
        for chunk in chunks:
            await interaction.followup.send(chunk)
    else:
        await interaction.followup.send("Failed to fetch the NCSPC text. Please try again later.")

bot.run(TOKEN)
