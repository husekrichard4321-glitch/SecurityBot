import discord
from discord.ext import commands
from datetime import datetime, timedelta


class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.join_logs = []
        self.raid_threshold = 5
        self.time_window = 10
        self.channel_id = 1424126177227837593
        self.ADMIN_ID = 1170772595587686410

    @commands.Cog.listener()
    async def on_member_join(self, member):
        now = datetime.now()
        self.join_logs.append(now)

        self.join_logs = [t for t in self.join_logs if (
            now - t).total_seconds() < self.time_window]

        if len(self.join_logs) >= self.raid_threshold:
            await self.alert_admins(member.guild)

    async def alert_admins(self, guild):
        channel = self.bot.get_channel(self.channel_id)
        if channel:
            await channel.send(
                f"⚠️ -------POSSIBLE RAID DETECTED------- ⚠️ \n"
                f"in a short time {len(self.join_logs)} users joined"
            )
        else:
            print(
                f"DEBUG: security_allert couldn't find channel ID {self.channel_id}")

    @discord.app_commands.command(name="test_raid", description="Simulates 5 quick joins to test security")
    async def test_raid(self, interaction: discord.Interaction):
        if interaction.user.id != self.ADMIN_ID:
            await interaction.response.send_message("Only admin can test this!", ephemeral=True)
            return

        await interaction.response.send_message("🚀 Simulating raid... check logs!", ephemeral=True)

        now = datetime.now()
        for _ in range(5):
            self.join_logs.append(now)

        if len(self.join_logs) >= self.raid_threshold:
            await self.alert_admins(interaction.guild)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Modul Security_allert running")


async def setup(bot):
    await bot.add_cog(Security(bot))
