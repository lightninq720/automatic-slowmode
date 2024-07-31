import nextcord
from constants import GITLINK, KO_FI

class BotInfoLinkButton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(label="Ko-fi", url=KO_FI))
        self.add_item(nextcord.ui.Button(label="GitHub", url=GITLINK))