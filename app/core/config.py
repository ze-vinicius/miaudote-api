import os
from dotenv import load_dotenv

from pathlib import Path
from pydantic import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJET_NAME: str = "miaudote"
    PROJECT_VERSION: str = "0.1"

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    AWS_SECRET_KEY: str
    AWS_ACCESS_KEY_ID: str
    BUCKET_ENDPOINT: str
    AWS_BUCKET: str

    CORS_ORIGINS: str
    CORS_HEADERS: str


settings = Settings()
