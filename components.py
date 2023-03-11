from dotenv import load_dotenv
from pathlib import Path
import sqlite3 as sql
from sqlalchemy import create_engine
import sqlalchemy as sa


ENV_PATH = Path('/config/.env')


class Storage:

    def __init__(self, database: str, *args, **kwargs):
        self.db = database
        self.args = args
        self.kwargs = kwargs
