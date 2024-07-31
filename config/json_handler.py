import json
from typing import List

def json_get_enabled() -> bool:
    with open("config/settings.json", "r") as f:
        data = json.load(f)

    return data["enabled"]

def json_set_enabled(enabled: bool) -> None:
    with open("config/settings.json", "r") as f:
        data = json.load(f)

    data["enabled"] = enabled

    with open("config/settings.json", "w") as f:
        json.dump(data, f)

def json_get_channel_mode() -> str:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["channel_mode"].lower() # Returns the channel mode in lower case

def json_update_channel_mode(mode: str) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["channel_mode"] = mode # Sets channel mode to be the new value
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_get_channels() -> List[int]:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["channels"] # Returns the channels list

def json_add_channel(channel_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["channels"].append(channel_id) # Adds channel id to channels list
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_remove_channel(channel_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    index = data["channels"].index(channel_id) # Finds the index where the channel id is
    del data["channels"][index] # Deletes the channel id using the index
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def get_slowmode_values() -> dict:
    with open("config/slowmode_values.json", "r") as f:
        data = json.load(f)

    return data["slowmode_values"]