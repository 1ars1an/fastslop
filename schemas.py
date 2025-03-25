from enum import Enum
from pydantic import BaseModel, validator
from datetime import date

class GenreURLChoices(Enum):
    ROCK = 'synth rock'

class Album(BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []

class BandCreate(BandBase):
    pass

class BandWithID(BandBase):
    id: int

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None