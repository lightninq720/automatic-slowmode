import nextcord, os
from nextcord.ext import commands
from constants import TOKEN
from utils import colour_message

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="nom!", intents=nextcord.Intents.all()) # Creates a new bot instance
        self.unloaded_cogs = []

    def initialize(self) -> None:
        os.system("cls") # Clears the terminal for easy reading
        print(colour_message(message='Automatic Slowmode Online', colour="yellow"))
        print(colour_message(message="Bot has started", colour="green"))
        self.load_extensions()
        self.run(TOKEN) # Runs the bot, using the token
    
    def load_extensions(self) -> None: # Loads the cog extensions
        for folder in os.listdir("./cogs"): # Finds all the folders in cogs folder
            for cog in os.listdir(f"./cogs/{folder}"): # For each folder finds all files
                if cog.endswith(".py"): # Checks if the file is a python file
                    try: # If a file errors it will trip this try/except
                        self.load_extension(name=f"cogs.{folder}.{cog[:-3]}") # Loads each cog
                        print(colour_message(message=f"Loaded {cog[:-3]} cog", colour="blue"))

                    except Exception as e: # Catches each error and prints it to console
                        print(e)
                        print(colour_message(message=f"Failed to load {cog[:-3]} cog", colour="yellow"))
                        self.unloaded_cogs.append(cog.capitalize()[-3])
    
    async def on_ready(self) -> None: # Runs when the bot is ready to be used
        print(colour_message(message=f"Logged in as {self.user}!", colour="green"))
        await self.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Setting Slowmodes")) # Sets the bots status