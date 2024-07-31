import pymysql
from typing import List
from constants import DEBENDPOINT, DBNAME, DBPASS, DBUSER, DBPORT
from utils import list_to_sql_string, sql_string_to_list