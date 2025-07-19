from .base import Base
from sqlalchemy import Column, DateTime, Integer, String
from pgvector.sqlalchemy import Vector
from sqlalchemy.sql import func

EMBEDDING_DIMENSION = 384


class Embedding(Base):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    embedding: Vector = Column(Vector(384), nullable=False)
    origin = Column(String, nullable=False)
    source_name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<Embedding(id={self.id}, vector={self.embedding}, origin={self.origin}, source_name={self.source_name})>"
