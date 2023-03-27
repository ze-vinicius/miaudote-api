from fastapi import FastAPI
from app.db.base import engine, Base

from app.modules.pet_shelter.router import router as pet_shelter_router
from app.modules.auth.router import router as auth_router

app = FastAPI()

app.include_router(pet_shelter_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Server running..."}


Base.metadata.create_all(engine)
