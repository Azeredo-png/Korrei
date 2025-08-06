import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
