import pymysql
from typing import List
from constants import DBENDPOINT, DBNAME, DBPASS, DBUSER, DBPORT
from utils import list_to_sql_string, sql_string_to_list

def sql_add_data(guild_id: int, channel_mode: str = "blacklist", enabled: bool = True) -> None:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("INSERT INTO `slowmode_config` (guild_id, channel_mode, enabled) VALUES (%s, %s, %s)", (guild_id, channel_mode, enabled))
    conn.commit() # Saves changes to the database

def sql_get_enabled(guild_id: int) -> bool:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    conn.commit() # Saves changes to the database
    if not data: # If no data exists, creates default data
        sql_add_data(guild_id=guild_id)
        return True
    return data[0][2] # Returns enabled value

def sql_set_enabled(guild_id: int, enabled: bool):
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    if not data: # If no data exists, creates default data
        conn.commit() # Saves changes to the database
        sql_add_data(guild_id=guild_id, enabled=enabled)
        return
    cur.execute("UPDATE `slowmode_config` SET enabled = %s WHERE guild_id = %s", (enabled, guild_id))
    conn.commit() # Saves changes to the database


def sql_get_channel_mode(guild_id: int) -> str:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    conn.commit() # Saves changes to the database
    if not data: # If no data exists, creates default data
        sql_add_data(guild_id=guild_id)
        return "blacklist"
    return data[0][1].lower() # Returns channel mode in lower case

def sql_update_channel_mode(guild_id: int, mode: str) -> None:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    if not data: # If no data exists, creates default data
        conn.commit() # Saves changes to the database
        sql_add_data(guild_id=guild_id, channel_mode=mode)
        return
    cur.execute("UPDATE `slowmode_config` SET channel_mode = %s WHERE guild_id = %s", (mode, guild_id))
    conn.commit() # Saves changes to the database


def sql_get_channels(guild_id: int) -> List[int]:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    conn.commit() # Saves changes to the database
    if not data: # If no data exists, creates default data
        sql_add_data(guild_id=guild_id)
        return []
    if not data[0][2]: # If no data in database, returns empty list
        return []
    l = sql_string_to_list(data[0][2]) # Turns string from sql into string list
    ll = [int(i) for i in l] # Turns string list into int list
    return ll # Returns int list

def sql_add_channel(guild_id: int, channel_id: int) -> None:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    if not data: # If no data exists, creates default data
        conn.commit() # Saves changes to the database
        sql_add_data(guild_id=guild_id)
        return
    if not data[0][2]: # If no data exisits skips list manipulation
        cur.execute("UPDATE `slowmode_config` SET channels = %s WHERE guild_id = %s", (channel_id, guild_id))
        conn.commit() # Saves changes to the database
        return
    l = sql_string_to_list(data[0][2]) # Turns string from sql into string list
    l.append(str(channel_id)) # Adds channel id to list
    cur.execute("UPDATE `slowmode_config` SET channels = %s WHERE guild_id = %s", (list_to_sql_string(l), guild_id)) # Turns string list into string when putting it into database
    conn.commit() # Saves changes to the database

def sql_remove_channel(guild_id: int, channel_id: int) -> None:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    if not data: # If no data exists, creates default data
        conn.commit() # Saves changes to the database
        sql_add_data(guild_id=guild_id)
        return
    if not data[0][2]: # If no data exisits skips list manipulation
        conn.commit() # Saves changes to the database
        return
    l = sql_string_to_list(data[0][2]) # Turns string from sql into string list
    index = l.index(str(channel_id))  # Finds the index where the channel id is
    del l[index] # Deletes the channel id using the index
    cur.execute("UPDATE `slowmode_config` SET channels = %s WHERE guild_id = %s", (list_to_sql_string(l), guild_id)) # Turns string list into string when putting it into database
    conn.commit() # Saves changes to the database



def sql_get_guild_data(guild_id: int) -> List[str]:
    conn = pymysql.connect(host=DBENDPOINT, port=DBPORT, user=DBUSER, password=DBPASS, db=DBNAME) # Connects to database and creates a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM `slowmode_config` WHERE guild_id = %s", (guild_id))
    data = cur.fetchall()
    conn.commit() # Saves changes to the database
    return data # Returns full data set