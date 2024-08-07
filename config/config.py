from typing import List
from .json_handler import *
from utils import colour_message

errormessage = colour_message(message="Inccorect database mode, use either 'SQL' or 'JSON'", colour="red") # Generates error message to be printed to console

def get_enabled(guild_id: int) -> bool:
    return json_get_enabled()

def get_slowmode_values() -> dict:
    return json_get_slowmode_values()

def set_enabled(guild_id: int, val: bool) -> None:
    return json_set_enabled()
    

def get_channel_mode(guild_id: int) -> str:
    return json_get_channel_mode()
    

def update_channel_mode(guild_id: int, mode: str) -> None:
    json_update_channel_mode(mode)
    

def get_channels(guild_id: int) -> List[int]:
    return json_get_channels()
    

def add_channel(guild_id: int, channel: int) -> None:
    json_add_channel(channel)
    

def remove_channel(guild_id: int, channel: int) -> None:
    json_remove_channel(channel)
    