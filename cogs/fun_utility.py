import discord
from discord.ext import commands, tasks
import random
import os


class FunUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.MESSAGES_FILE = os.path.join(
            os.path.dirname(self.BASE_DIR), "zpravy.txt")

        self.CHANNEL_ID = 1424102844969259142
        self.ADMIN_ID = 1170772595587686410

        self.seconds = None
        self.target_user = None
        self.spam_message = None
        self.owner_active = False

    def load_messages(self):
        if not os.path.exists(self.MESSAGES_FILE):
            print(f"ERROR: File not found in path: {self.MESSAGES_FILE}")
            return ["ERROR MESSAGE: The message file is missing "]
        with open(self.MESSAGES_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    # --- 3. Automatic tasks (Tasks / loops) ---

    # hourly loop and random message output

    @tasks.loop(hours=6)
    async def hourly_message(self):
        channel = self.bot.get_channel(self.CHANNEL_ID)
        if not channel:
            print(f"Channel {self.CHANNEL_ID} was not found")
            return
        messages = self.load_messages()
        await channel.send(random.choice(messages))

    # loop for spamming

    @tasks.loop(seconds=5)
    async def spam_task(self):
        channel = self.bot.get_channel(self.CHANNEL_ID)
        if self.target_user and self.spam_message and channel:
            await channel.send(f"{self.target_user.mention} {self.spam_message}")

    # --- 4. commands ---

    @discord.app_commands.command(name="spamm_target", description="bot is going to spamm target")
    async def spamm_target(self, interaction: discord.Interaction, member: discord.Member, message: str, seconds: int = 5):
        if self.owner_active and interaction.user.id != self.ADMIN_ID:
            await interaction.response.send_message("Bot is controlled by admin. You don't have permission!", ephemeral=True)
            return

        self.owner_active = (interaction.user.id == self.ADMIN_ID)
        self.seconds = seconds
        self.target_user = member
        self.spam_message = message

        if self.spam_task.is_running():
            self.spam_task.stop()

        self.spam_task.change_interval(seconds=seconds)
        self.spam_task.start()
        await interaction.response.send_message(f"starting spam: {member.display_name} with message {message} every {seconds}s")

    @discord.app_commands.command(name="stop_spam", description="ending spam")
    async def stop_spam(self, interaction: discord.Interaction):
        if self.owner_active and interaction.user.id != self.ADMIN_ID:
            await interaction.response.send_message("Bot is controlled by admin. You don't have permission!", ephemeral=True)
            return

        self.seconds = None
        self.target_user = None
        self.owner_active = False
        self.spam_task.stop()
        await interaction.response.send_message("spamming stopped.")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Modul FunUtility running")
        if not self.hourly_message.is_running():
            self.hourly_message.start()


async def setup(bot):
    await bot.add_cog(FunUtility(bot))
