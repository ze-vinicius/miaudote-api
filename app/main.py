from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import database
from app.modules.auth.router import router as auth_router
from app.modules.pet_shelter.router import router as pet_shelter_router

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


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck():
    return {"status": "ok"}
