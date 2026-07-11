"""
Upload Model

Stores upload audit logs.
"""

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Upload(Base):

    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False,
    )

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="uploads",
    )

    document = relationship(
        "Document",
        back_populates="uploads",
    )

    def __repr__(self):

        return f"<Upload {self.id}>"