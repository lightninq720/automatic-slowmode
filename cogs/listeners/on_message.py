import nextcord
from nextcord.ext import commands
from bot import Bot
from config import get_slowmode_values, get_channels, get_channel_mode

class On_Message(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client
        self.values = get_slowmode_values()

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.bot:
            return
        channels = get_channels(guild_id = message.guild.id)
        channel_mode = get_channel_mode(guild_id = message.guild.id)
        guild_channels = [channel.id for channel in message.guild.channels]
        if channel_mode == "blacklist":
            valid_channels = list(set(guild_channels) - set(channels))
        else:
            valid_channels = channels

        if not message.channel.id in valid_channels:
            return
        
        