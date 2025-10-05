import os
import qrcode
import discord
from discord.ext import commands
from dotenv import load_dotenv
    
def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    return commands.Bot(command_prefix="!", intents=intents)

def create_qr_code_img(data):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # pyright: ignore[reportAttributeAccessIssue]
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")

def get_token():
    load_dotenv()
    token = os.getenv('TOKEN')
    if token is None:
        print("[Error] Token is missing")
        return ""
    return token
