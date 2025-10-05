import io
import discord
import qrcode
import random
from discord.ext import commands

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
    if text is None:
        await ctx.send("❌ Please provide text to generate a QR code.\nExample: `!qr Hello world!`")
        return
    
    # Create QR code in memory
    img = qrcode.make(text)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Send as file
    await ctx.send(file=discord.File(buffer, filename="qr.png"))

bot.run('1')
