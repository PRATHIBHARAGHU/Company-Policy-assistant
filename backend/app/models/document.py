from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    page_count = Column(Integer, default=1)
    access_level = Column(String, default="employee")
    content = Column(Text, nullable=True)

    owner = relationship("User", back_populates="documents")

    # Purpose: Represent uploaded policy documents.
    # Inputs: Document metadata from upload pipeline.
    # Outputs: ORM model used for document management and access control.
    # Flow: Persist document metadata and content for retrieval.
