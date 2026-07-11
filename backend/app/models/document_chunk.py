"""
Document Chunk Model

Stores chunks indexed inside Qdrant.
"""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    String,
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False,
    )

    page_number = Column(Integer, nullable=False)

    chunk_index = Column(Integer, nullable=False)

    chunk_text = Column(Text, nullable=False)

    qdrant_point_id = Column(
        String(120),
        nullable=True,
    )

    document = relationship(
        "Document",
        back_populates="chunks",
    )

    def __repr__(self):

        return f"<Chunk {self.chunk_index}>"