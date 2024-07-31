import nextcord
from typing import List
from constants import COLOURS, COLOUR_GOOD, COLOUR_NEUTRAL, COLOUR_BAD

def colour_message(message: str, colour: str = COLOURS["default"]) -> str: # Used to generate coloured messages to print them to console
    colour = COLOURS.get(colour, COLOURS["default"])
    return colour + message + "\033[0m"

def create_success_embed(title: str = "\u200b", description: str = "\u200b") -> nextcord.Embed:
    embed = nextcord.Embed(title=title, description=description, color=COLOUR_GOOD)
    embed.set_thumbnail(url="https://media.tenor.com/AWKzZ19awFYAAAAi/checkmark-transparent.gif") # Sets embed thumbnail
    return embed

def create_warning_embed(title: str = "\u200b", description: str = "\u200b") -> nextcord.Embed:
    embed = nextcord.Embed(title=title, description=description, color=COLOUR_NEUTRAL)
    embed.set_thumbnail(url="https://c.tenor.com/26pNa498OS0AAAAi/warning-joypixels.gif") # Sets embed thumbnail
    return embed

def create_error_embed(title: str = "\u200b", description: str = "\u200b") -> nextcord.Embed:
    embed = nextcord.Embed(title=title, description=description, color=COLOUR_BAD)
    embed.set_thumbnail(url="https://media.tenor.com/Gbp8h-dqDHkAAAAi/error.gif") # Sets embed thumbnail
    return embed

def sql_string_to_list(string: str) -> List[str]:
    return string.split(":") # Splits string at colon, creating a string list

def list_to_sql_string(list: List[str]) -> str:
    s = ""
    for i in list:
        s = s + i + ":" # For each id in list adds its to sting, followed by a colon
    return s[:-1] # Returns string, removing the last colon
