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


settings = Settings()
