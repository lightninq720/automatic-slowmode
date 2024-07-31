import os
from typing import Text, Dict
from dotenv import load_dotenv

load_dotenv() # Load private variables from .env file

TOKEN: Text = os.environ['TOKEN'] # Gets the token from .env file


COLOURS: Dict[str, str] = {"red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m", "blue": "\033[34m", "default": "\033[37m"}


COLOUR_MAIN = 0x43a1e8
COLOUR_GOOD = 0x03C04A
COLOUR_NEUTRAL = 0xFCAE1E
COLOUR_BAD = 0x900D09


KO_FI = "https://ko-fi.com/lightninq"
GITLINK = "https://github.com/lightninq720/automatic-slowmode"

DBENDPOINT = os.environ['DBENDPOINT'] # Gets the DBENDPOINT from .env file
DBUSER = os.environ['DBUSER'] # Gets the DBUSER from .env file
DBPASS = os.environ['DBPASS'] # Gets the DBPASS from .env file
DBNAME = os.environ['DBNAME'] # Gets the DBNAME from .env file
DBPORT = int(os.environ['DBPORT']) # Gets the DBPORT from .env file

DATABASE_MODE = "JSON" # USE EITHER "SQL" or "JSON" ONLY. Select the database mode you want to use. NB: JSON only supports single server uses