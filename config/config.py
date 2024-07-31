from typing import List
from .json_handler import *
from .sql_handler import *
from constants import DATABASE_MODE
from utils import colour_message

errormessage = colour_message(message="Inccorect database mode, use either 'SQL' or 'JSON'", colour="red") # Generates error message to be printed to console

def get_enabled(guild_id: int) -> bool:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_enabled(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_enabled()
    else:
        print(errormessage)

def get_slowmode_values() -> dict:
    return json_get_slowmode_values()

def set_enabled(guild_id: int, val: bool) -> None:
    if DATABASE_MODE.lower() == "sql":
        return sql_set_enabled(guild_id, val)
    elif DATABASE_MODE.lower() == "json":
        return json_set_enabled()
    else:
        print(errormessage)

def get_channel_mode(guild_id: int) -> str:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_channel_mode(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_channel_mode()
    else:
        print(errormessage)

def update_channel_mode(guild_id: int, mode: str) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_update_channel_mode(guild_id, mode)
    elif DATABASE_MODE.lower() == "json":
        json_update_channel_mode(mode)
    else:
        print(errormessage)

def get_channels(guild_id: int) -> List[int]:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_channels(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_channels()
    else:
        print(errormessage)

def add_channel(guild_id: int, channel: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_add_channel(guild_id, channel)
    elif DATABASE_MODE.lower() == "json":
        json_add_channel(channel)
    else:
        print(errormessage)

def remove_channel(guild_id: int, channel: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_remove_channel(guild_id, channel)
    elif DATABASE_MODE.lower() == "json":
        json_remove_channel(channel)
    else:
        print(errormessage)