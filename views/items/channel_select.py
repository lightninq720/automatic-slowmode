import nextcord

class ChannelList(nextcord.ui.ChannelSelect):
    def __init__(self) -> None:
        super().__init__(placeholder="Select channel", min_values=1, max_values=1, channel_types=[nextcord.ChannelType.text, nextcord.ChannelType.news])

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.view.value = self.values[0] # Sets Parent Views value to be selected channel
        self.view.stop() # Stops the Channel Select Parent View

class ChannelSelect(nextcord.ui.View):
    def __init__(self, org_user:int) -> None:
        super().__init__(timeout=600)
        self.add_item(ChannelList()) # Adds the channel list dropdown to the view
        self.value = None
        self.org_user = org_user

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        if interaction.user.id != self.org_user: # Checks if user created the channel select panel, if not, prevents them from using it
            await interaction.send("You can't click this!", ephemeral=True)
            return False
        
        return True