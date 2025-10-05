import io
import os
import discord
import qrcode
import random
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')

@bot.command()
async def qr(ctx, *, text: str):
    img = qrcode.make(text)
    img.save("qr.png")
    await ctx.send(file=discord.File("qr.png"))

def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    if token is None:
        print("[Error] Token is missing")
        return
    bot.run(token)

if __name__ == '__main__':
    main()
