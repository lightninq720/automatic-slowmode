import nextcord

class roleselect(nextcord.ui.RoleSelect):
    def __init__(self) -> None:
        super().__init__(placeholder="Select Role", min_values=1, max_values=1)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.view.value = self.values[0] # Sets Parent Views value to be selected role
        self.view.stop() # Stops the Role Select Parent View

class Role_Select(nextcord.ui.View):
    def __init__(self, org_user: int) -> None:
        super().__init__(timeout=600)
        self.add_item(roleselect()) # Adds the channel list dropdown to the view
        self.value = None
        self.org_user = org_user

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        if interaction.user.id != self.org_user: # Checks if user created the role select panel, if not, prevents them from using it
            await interaction.send("You can't click this!", ephemeral=True)
            return False
        
        return True