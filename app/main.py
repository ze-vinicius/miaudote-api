from fastapi import FastAPI
from app.db.base import engine, Base

from app.modules.pet_shelter.router import router as pet_shelter_router

app = FastAPI()

app.include_router(pet_shelter_router)


@app.get("/")
async def root():
    return {"message": "Server running..."}

Base.metadata.create_all(engine)