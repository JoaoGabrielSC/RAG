from src.repositories import BaseRepository
from sqlalchemy.orm import Session
from src.database.dto import EmbeddingDTO
from src.database.models.embedding import Embedding


class PgVectorRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = Embedding

    def get_by_id(self, id: int) -> EmbeddingDTO | None:
        embedding = self.session.query(self.model).filter_by(id=id).first()
        if embedding:
            return EmbeddingDTO.model_validate(embedding)
        return None

    def create(self, data: EmbeddingDTO) -> EmbeddingDTO:
        db_model = Embedding(
            text=data.text,
            embedding=data.embedding,
            origin=data.origin,
            source_name=data.source_name,
        )

        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)

        return EmbeddingDTO.model_validate(db_model)
