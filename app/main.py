from fastapi import FastAPI
from app.db.base import engine, Base

from starlette.middleware.cors import CORSMiddleware
from app.modules.pet_shelter.router import router as pet_shelter_router
from app.modules.auth.router import router as auth_router
from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)

app.include_router(pet_shelter_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Server running..."}


Base.metadata.create_all(engine)
