from entities.embedding import EmbeddingEntity
from .base_dto import BaseDTO
from datetime import datetime


class EmbeddingDTO(BaseDTO):
    id: int | None = None
    text: str
    embedding: list[float]
    origin: str
    source_name: str
    created_at: datetime | None = None

    @classmethod
    def to_entity(cls, obj: "EmbeddingDTO") -> EmbeddingEntity:
        return EmbeddingEntity(
            id=obj.id,
            text=obj.text,
            embedding=obj.embedding,
            origin=obj.origin,
            source_name=obj.source_name,
        )
