from fastapi import FastAPI

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
async def get_bands() -> list[dict]:
    return BANDS

@app.get("/bands/{band_id}")
async def get_band(band_id: int) -> str:
    band = next((b for b in BANDS if b["id"] == band_id), None)
    if band:
        return band
    else:
        return {"message": "Band not found"}