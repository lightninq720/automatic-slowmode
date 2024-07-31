import nextcord, time, asyncio
from nextcord.ext import commands
from bot import Bot
from constants import COLOUR_MAIN, KO_FI, GITLINK
from views import PingView, PingRetry, BotInfoLinkButton

class Misc(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client
    
    @nextcord.slash_command(name="botinfo", description="Information about the bot")
    async def botinfo(self, interaction: nextcord.Interaction) -> None:
        await interaction.response.defer()
        before = time.monotonic()
        msg = await interaction.send("Loading bot information")
        ping = (time.monotonic() - before) * 1000 # Uses time module to calculate how long it takes to send a message
        embed = nextcord.Embed(title="Bot Infomation", description=f"Ping: {round(ping)}ms \nSupport Me: [Ko-fi]({KO_FI}) \nGitHub: [GitHub]({GITLINK})", colour=COLOUR_MAIN)
        embed.set_footer(text="Coded by @_lightninq")
        await msg.edit(content = " ", embed=embed, view=BotInfoLinkButton()) # Edits message to add the embed

    @nextcord.slash_command(name="ping", description="Get the bot's ping")
    async def ping(self, interaction: nextcord.Interaction) -> None:
        msg = await interaction.send("Checking Ping")
        before = time.monotonic()
        await msg.edit("Checking Ping!")
        ping = round(((time.monotonic() - before) * 1000),2) # Uses time module to calculate how long it takes to send a message
        await msg.edit(content=None, view=PingView(ping))
        await asyncio.sleep(5) # Waits 5 seconds
        await msg.edit(content=None, view=PingRetry(ping)) # Edits message to add Redo Ping button

def setup(client: Bot):
    client.add_cog(Misc(client))