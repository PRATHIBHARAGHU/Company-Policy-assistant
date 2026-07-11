from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    s3_key = Column(String(512), unique=True, nullable=False)
    file_type = Column(String(10), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    min_clearance_level = Column(Integer, default=0, nullable=False) 
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")