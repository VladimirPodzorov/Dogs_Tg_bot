from datetime import datetime
from peewee import *

db = SqliteDatabase("history.db")


class History(Model):
    user_id = CharField()
    user_resp = CharField()

    class Meta:
        database = db
