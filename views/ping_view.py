import nextcord, time, asyncio

class PingView(nextcord.ui.View):

    def __init__(self, ping) -> None:
        super().__init__()
        self.add_item(nextcord.ui.Button(label=f"Ping: {ping}", style = nextcord.ButtonStyle.blurple, disabled=False))
    
    @staticmethod
    async def callback(interaction: nextcord.Interaction) -> None:
        await interaction.response.defer(with_message=False)

class PingRetry(nextcord.ui.View):
    def __init__(self, ping) -> None:
        super().__init__()
        self.add_item(nextcord.ui.Button(label=f"Ping: {ping}", style = nextcord.ButtonStyle.blurple, disabled=True))

    @nextcord.ui.button(label="Redo Ping", style=nextcord.ButtonStyle.green)
    async def submit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction) -> None:
        await interaction.response.defer(with_message=False)
        await interaction.edit_original_message(content="Checking Ping", view=None)
        before = time.monotonic()
        await interaction.edit_original_message(content="Checking Ping!", view=None)
        ping = round(((time.monotonic() - before) * 1000),2) # Uses time module to calculate how long it takes to send a message
        await interaction.edit_original_message(content=None, view=PingView(ping))
        await asyncio.sleep(5) # Waits 5 seconds
        await interaction.edit_original_message(content=None, view=PingRetry(ping)) # Edits message to add Redo Ping button