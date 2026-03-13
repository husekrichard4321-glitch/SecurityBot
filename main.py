import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        cogs_folder = os.path.join(BASE_DIR, "cogs")
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

        await self.tree.sync()


bot = MyBot()
bot.run(os.getenv("DISCORD_TOKEN"))
