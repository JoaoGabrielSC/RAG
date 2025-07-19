from src.database.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, Session as SQLAlchemySession

metadata = [Base.metadata]


class DatabaseConnection:
    def __init__(self, database_url: str):
        self._database_url = database_url
        self._engine = self._create_engine()
        self._SessionLocal = sessionmaker(bind=self._engine)

    def _create_engine(self):
        return create_engine(self._database_url, echo=False, future=True)

    def get_engine(self):
        return self._engine

    def get_session(self) -> SQLAlchemySession:
        return self._SessionLocal()
