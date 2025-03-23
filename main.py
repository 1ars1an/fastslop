from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band

app = FastAPI()

BANDS = [
    {"id": 1, "name": "The Electric Unicorns", "genre": "Synth Rock"},
    {"id": 2, "name": "Velvet Thunder", "genre": "Classic Rock"},
    {"id": 3, "name": "Neon Howl", "genre": "Synthwave"},
    {"id": 4, "name": "Shadow Reverie", "genre": "Gothic Metal"},
    {"id": 5, "name": "The Cosmic Surfers", "genre": "Psychedelic Rock"},
    {"id": 6, "name": "Iron Phoenix", "genre": "Heavy Metal"},
    {"id": 7, "name": "The Quantum Rabbits", "genre": "Indie Pop"},
]

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/bands")
async def get_bands(genre: GenreURLChoices | None = None) -> list[Band]:
    if genre:
        return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]
    return [Band(**b) for b in BANDS]

@app.get("/bands/{band_id}") 
async def get_band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b["id"] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get("/genres/{genre}")
async def get_bands_by_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if b["genre"].lower() == genre.value]