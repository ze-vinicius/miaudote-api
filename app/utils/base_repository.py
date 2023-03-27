from sqlalchemy.orm.session import Session


class BaseRepository:
  def __init__(self, db: Session):
    self.db = db