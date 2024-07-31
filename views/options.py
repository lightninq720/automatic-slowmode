import nextcord
from nextcord.abc import GuildChannel
from nextcord.errors import NotFound
from utils import create_success_embed, create_error_embed, create_warning_embed
from config import get_channel_mode, get_channels, update_channel_mode, add_channel, remove_channel
from constants import COLOUR_MAIN
from typing import List
from views.items import ChannelSelect, Role_Select

class Options(nextcord.ui.View):
    def __init__(self, org_user: int) -> None:
        super().__init__(timeout=600, auto_defer=True)
        self.org_user = org_user
        self.embed = None

    async def __generate_embed(self, interaction: nextcord.Interaction) -> nextcord.Embed:
        # return nextcord.Embed(title=f"{interaction.guild.name} Snipe Settings", description=(f"\n\nChannel Mode: {get_channel_mode(interaction.guild_id)} \nChannels added to list {get_channels(interaction.guild_id) if len(get_channels(interaction.guild_id)) <= 5 else "List too long, press `Edit Channels` to view"} \n\nRole Mode: {get_role_mode(interaction.guild_id)} \nRoles added to list {get_roles(interaction.guild_id) if len(get_roles(interaction.guild_id)) <= 5 else "List too long, press `Edit Roles` to view"}"), colour=COLOUR_MAIN)
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
        return embed

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        if interaction.user.id != self.org_user: # Checks if user created the options panel, if not, prevents them from using it
            await interaction.send("You can't click this!", ephemeral=True)
            return False
        
        return True
    
    @nextcord.ui.button(label="Finish", style=nextcord.ButtonStyle.grey, row=3)
    async def finish(self, button: nextcord.ui.Button, interaction: nextcord.Interaction) -> None:
        await interaction.send(embed=create_success_embed(title="Success", description="Successfully finished editing options"), ephemeral=True)
        await interaction.edit(view=None)
        self.stop()

    @nextcord.ui.button(label="Toggle Channel Blacklist", style=nextcord.ButtonStyle.blurple, row=1)
    async def toggle_channel_mode(self, button: nextcord.ui.Button, interaction: nextcord.Interaction) -> None:
        if get_channel_mode(interaction.guild_id) == "blacklist": # If channel mode is blacklist, change it to whitelist mode
            update_channel_mode(interaction.guild_id, "whitelist")
            await interaction.send(embed=create_success_embed(title="Success", description="Successfully changed channel mode to `Whitelist`"), ephemeral=True)
        elif get_channel_mode(interaction.guild_id) == "whitelist": # If channel mode is whitelist, change it to blacklist mode
            update_channel_mode(interaction.guild_id, "blacklist")
            await interaction.send(embed=create_success_embed(title="Success", description="Successfully changed channel mode to `Blacklist`"), ephemeral=True)
        else: # If channel mode is neither, default it to blacklist
            update_channel_mode(interaction.guild_id, "blacklist")
            await interaction.send(embed=create_error_embed(title="Config Error", description="Channel mode was invalid, reset it to `Blacklist`"), ephemeral=True)
        await interaction.edit(embed=await self.__generate_embed(interaction)) # Regenerate options embed

    @nextcord.ui.button(label="Add Channel", style=nextcord.ButtonStyle.green, row=1)
    async def add_channel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction) -> None:
        channelview = ChannelSelect(interaction.user.id) # Create channel select view object
        msg = await interaction.send(embed=nextcord.Embed(title="Select Channel", description=f"Select the channel you wish to add to the {get_channel_mode(interaction.guild_id)}", colour=COLOUR_MAIN), view=channelview, ephemeral=True)
        await channelview.wait() # Wait for a selection to be made
        if not channelview.value.id in get_channels(interaction.guild_id): # If channel id isnt in database list then add it to the database
            add_channel(interaction.guild_id, channelview.value.id)
            await msg.edit(embed=create_success_embed(title="Success", description=f"Sucessfully added channel to the {get_channel_mode(interaction.guild_id)}"), view=None)
        else: # If channel id is in database list then tell the user and do nothing
            await msg.edit(embed=create_warning_embed(title="Warning", description=f"Channel was already in the {get_channel_mode(interaction.guild_id)}, no changes have been made"), view=None)
        await interaction.edit(embed=await self.__generate_embed(interaction)) # Regenerate options embed

    @nextcord.ui.button(label="Remove Channel", style=nextcord.ButtonStyle.red, row=1)
    async def remove_channel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction) -> None:
        channelview = ChannelSelect(interaction.user.id) # Create channel select view object
        msg = await interaction.send(embed=nextcord.Embed(title="Select Channel", description=f"Select the channel you wish to remove from the {get_channel_mode(interaction.guild_id)}", colour=COLOUR_MAIN), view=channelview, ephemeral=True)
        await channelview.wait() # Wait for a selection to be made
        if channelview.value.id in get_channels(interaction.guild_id): # If channel id is in database list then remove it from the database
            remove_channel(interaction.guild_id, channelview.value.id)
            await msg.edit(embed=create_success_embed(title="Success", description=f"Sucessfully removed channel from the {get_channel_mode(interaction.guild_id)}"), view=None)
        else: # If channel id isnt in database list then tell the user and do nothing
            await msg.edit(embed=create_warning_embed(title="Warning", description=f"Channel was not in the {get_channel_mode(interaction.guild_id)}, no changes have been made"), view=None)
        await interaction.edit(embed=await self.__generate_embed(interaction)) # Regenerate options embed
