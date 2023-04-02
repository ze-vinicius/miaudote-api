import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJET_NAME: str = "miaudote"
    PROJECT_VERSION: str = "0.1"

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"

    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    BUCKET_ENDPOINT: str = os.getenv("BUCKET_ENDPOINT")
    AWS_BUCKET: str = os.getenv("AWS_BUCKET")


settings = Settings()
