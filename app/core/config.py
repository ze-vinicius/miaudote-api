from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

from app.core.constants import Environment

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "miaudote"
    PROJECT_VERSION: str = "0.1"

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    AWS_SECRET_KEY: str
    AWS_ACCESS_KEY_ID: str
    BUCKET_ENDPOINT: str
    AWS_BUCKET: str

    CORS_ORIGINS: str
    CORS_HEADERS: str

    ENVIRONMENT: Environment = Environment.PRODUCTION


settings = Settings()
