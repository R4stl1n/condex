from peewee import *

from models.BaseModel import BaseModel

class SupportedCoinModel(BaseModel):
    Ticker = CharField(unique=True, max_length=64)


