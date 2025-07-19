from dataclasses import dataclass
from typing import List, Optional
from src.database.dto.embedding_dto import EmbeddingDTO
from datetime import datetime


@dataclass
class EmbeddingEntity:
    text: str
    embedding: List[float]
    origin: str
    source_name: str
    created_at: Optional[datetime] = None
    id: Optional[int] = None

    def __repr__(self) -> str:
        return (
            f"<EmbeddingEntity(id={self.id}, text={self.text}, "
            f"embedding={self.embedding}, origin={self.origin}, "
            f"source_name={self.source_name})>"
        )

    def is_valid(self) -> bool:
        return self.embedding is not None and len(self.embedding) > 0

    @classmethod
    def from_dto(cls, dto: "EmbeddingDTO") -> "EmbeddingEntity":
        return cls(
            id=dto.id,
            text=dto.text,
            embedding=dto.embedding,
            origin=dto.origin,
            source_name=dto.source_name or "",
        )

    def to_dto(self) -> "EmbeddingDTO":
        return EmbeddingDTO(
            id=self.id,
            text=self.text,
            embedding=self.embedding,
            origin=self.origin,
            source_name=self.source_name,
            created_at=self.created_at or datetime.now(),
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "text": self.text,
            "embedding": self.embedding,
            "origin": self.origin,
            "source_name": self.source_name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
