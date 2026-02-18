import discord
from discord.ext import tasks
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

# Where is this script on the PC?
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# attaching a folder with a script
MESSAGES_FILE = os.path.join(BASE_DIR, "zpravy.txt")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1424102844969259142

# authorization for bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


# reading and filtering file


def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    else:
        print(f"ERROR: File not found in path: {MESSAGES_FILE}")
        return ["DEFAULT MESSAGE: The message file is missing "]

# hourly loop and random message output


@tasks.loop(seconds=0.5)
async def hourly_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        meessages = load_messages()
        await channel.send(random.choice(meessages))

# run the boot


@bot.event
async def on_ready():
    print(f"bot logged in as: {bot.user.name}")
    hourly_message.start()

bot.run(TOKEN)
