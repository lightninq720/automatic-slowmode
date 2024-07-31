from typing import List
from .json_handler import *
from .sql_handler import *
from constants import DATABASE_MODE
from utils import colour_message

errormessage = colour_message(message="Inccorect database mode, use either 'SQL' or 'JSON'", colour="red") # Generates error message to be printed to console