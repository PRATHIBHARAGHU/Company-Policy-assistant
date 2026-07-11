"""
Document Model

Stores uploaded document metadata.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    file_name = Column(String(255), nullable=False)

    file_type = Column(String(20), nullable=False)

    s3_url = Column(String(500), nullable=True)

    access_level = Column(
        String(50),
        default="employee",
        nullable=False,
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    owner = relationship(
        "User",
        back_populates="documents",
    )

    chunks = relationship(
        "DocumentChunk",
        back_populates="document",
        cascade="all, delete-orphan",
    )

    uploads = relationship(
        "Upload",
        back_populates="document",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Document(title='{self.title}')>"