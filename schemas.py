from enum import Enum
from pydantic import BaseModel

class GenreURLChoices(Enum):
    ROCK = 'synth rock'

class Band(BaseModel):
    id: int
    name: str
    genre: str