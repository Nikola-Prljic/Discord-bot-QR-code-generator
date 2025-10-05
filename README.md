# DevProjects - Discord bot: QR code generator

This is an open source project from [DevProjects](http://www.codementor.io/projects). Feedback and questions are welcome!
Find the project requirements here: [Discord bot: QR code generator](https://www.codementor.io/projects/tool/discord-bot-qr-code-generator-cgkm8b16qf)

## Tech/framework used
Built with:
- [discord.py](https://pypi.org/project/discord/) (v2.3.2)
- [qrcode](https://pypi.org/project/qrcode/) (v8.2)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (v1.1.1)
- [Pillow](https://pypi.org/project/Pillow/)

## Screenshots and demo
![QR Code Example](qr.png)

## Features
- Generate QR codes from text via Discord commands
- Responds to `!qr <text>` with a QR code image
- Simple `!ping` command for bot status check

## Installation

1. **Clone the repository:**

        git clone <repository-url>

        cd Discord-bot-QR-code-generator

2. **install requirements**

        pip install -r requirements.txt

3. **Create a .env file in the project root**

    following content:

        TOKEN=your_discord_bot_token_here

## License
[MIT](https://choosealicense.com/licenses/mit/)
Most open source projects use the MIT license. Feel free to choose whichever license you prefer.
