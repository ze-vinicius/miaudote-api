from databases import Database
from sqlalchemy import MetaData, create_engine

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)


database = Database(
    settings.DATABASE_URL, force_rollback=settings.ENVIRONMENT.is_testing
)
metadata = MetaData()


async def get_db():
    yield database
