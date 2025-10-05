import discord
import os
import random
import qrcode
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('TOKEN')
""" if token is None:
    return """

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

""" 
@bot.command()
async def qr(ctx, *, text: str):
    img = qrcode.make(text)
    img.save("qr.png")
    await ctx.send(file=discord.File("qr.png")) """

bot.run(token)
