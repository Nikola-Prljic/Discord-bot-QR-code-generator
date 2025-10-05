import discord
from bot import create_bot, create_qr_code_img, get_token

bot = create_bot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')

@bot.command()
async def qr(ctx, *, text: str):
    img = create_qr_code_img(text)
    img.save("qr.png") # pyright: ignore[reportArgumentType]
    await ctx.send(file=discord.File("qr.png"))

def main():
    token = get_token()
    if token == "":
        return
    bot.run(get_token())

if __name__ == '__main__':
    main()
