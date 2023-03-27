from fastapi import FastAPI
from .db.base import engine, Base

from app.routers import pets, pet_shelters

app = FastAPI()

app.include_router(pets.router)
app.include_router(pet_shelters.router)


@app.get("/")
async def root():
    return {"message": "Server running..."}

Base.metadata.create_all(engine)