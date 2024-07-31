import nextcord, traceback
from nextcord.ext import commands, tasks
from bot import Bot
from datetime import datetime
from config import get_slowmode_values, get_channels, get_channel_mode

messages = {}

class On_Message(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client
        self.values = get_slowmode_values()

        self.check_slowmode.start()

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
        
        if not message.channel.id in messages:
            messages[message.channel.id] = 1
            return
        
        messages[message.channel.id] += 1

        # cur_message
        # fetch last 10 messages
        # check timestamp of earliest message of 10
        # compare difference in time between earliest message and cur_message
        # if less than 30 seconds, add slowmode

    @tasks.loop(seconds=5)
    async def check_slowmode(self):
        values = get_slowmode_values()
        for guild in self.client.guilds:
            channels = get_channels(guild_id =guild.id)
            channel_mode = get_channel_mode(guild_id = guild.id)
            guild_channels = [channel.id for channel in guild.text_channels]
            if channel_mode == "blacklist":
                valid_channels = list(set(guild_channels) - set(channels))
            else:
                valid_channels = channels

            for channel in valid_channels:
                try:
                    chan = guild.get_channel(channel)
                    cur_slowmode = 0

                    messages = await chan.history(limit=max([int(limit) for limit in values.keys()])).flatten()

                    for message_limit, time in values.items():
                        message_limit = int(message_limit)

                        if datetime.now().timestamp() - messages[min(message_limit-1, len(messages)-1)].created_at.timestamp() <= 30:
                            cur_slowmode = time
                    
                    await chan.edit(slowmode_delay=cur_slowmode)

                except Exception as e:
                    traceback.print_exc()

                



def setup(client: Bot):
    client.add_cog(On_Message(client))