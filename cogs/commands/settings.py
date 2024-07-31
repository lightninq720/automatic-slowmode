import nextcord
from nextcord.ext import commands
from nextcord.abc import GuildChannel
from nextcord.errors import NotFound
from config import get_channel_mode, get_channels, get_role_mode, get_roles, remove_channel, remove_role
from utils import create_warning_embed
from bot import Bot
from views import Options
from constants import COLOUR_MAIN
from typing import List


class Settings(commands.Cog):
    def __init__(self, client: Bot) -> None:
        self.client = client

    @nextcord.slash_command(name="settings", description="Modify your guilds settings")
    async def settings(self, interaction: nextcord.Interaction) -> None:
        if not interaction.user.guild_permissions.administrator: # Checks if user has administrator permissions, if not, prevents them running the command
            await interaction.send(embed=create_warning_embed(title="Lacking Permissions", description="You are lacking the `administrator` permission, contact the server administrators if you believe this is an error"), ephemeral=True)
            return
        embed = nextcord.Embed(title=f"{interaction.guild.name} Snipe Settings", colour=COLOUR_MAIN) # Creates the base embed, which will have sections added to it
        embed.add_field(name="Channel Mode:", value=get_channel_mode(interaction.guild_id).capitalize())
        channels: List[GuildChannel] = []
        for id in get_channels(interaction.guild_id): # Iterates through each channel id in the database list
            try: # If channel has been deleted this will error
                channels.append(await interaction.guild.fetch_channel(id)) # Fetches channel and adds it to channels list
            except NotFound: # If channel has been deleted, remove it from the database list
                remove_channel(interaction.guild_id, id)
        embed.add_field(name=f"Channels added to {get_channel_mode(interaction.guild_id)}:", value=", ".join([i.mention for i in channels]), inline=False)
        embed.set_footer(text="Coded by @_lightninq & @firestarad")
        embed.set_thumbnail(interaction.guild.icon.url if interaction.guild.icon else None) # Sets thumbnail to be guild icon, if it has one
        await interaction.send(embed=embed, view=Options(interaction.user.id))

def setup(client: Bot):
    client.add_cog(Settings(client))