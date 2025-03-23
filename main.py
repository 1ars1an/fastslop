from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandCreate, BandWithID

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
async def get_bands(genre: GenreURLChoices | None = None) -> list[BandWithID]:
    if genre:
        return [BandWithID(**b) for b in BANDS if b["genre"].lower() == genre.value]
    return [BandWithID(**b) for b in BANDS]

@app.get("/bands/{band_id}") 
async def get_band(band_id: int) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b["id"] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get("/genres/{genre}")
async def get_bands_by_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if b["genre"].lower() == genre.value]

@app.post("/bands")
async def create_band(band: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band.model_dump()).model_dump()
    BANDS.append(band)
    return band