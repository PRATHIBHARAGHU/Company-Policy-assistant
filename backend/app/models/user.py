"""
File: backend/app/models/user.py

Purpose:
    User model for authentication and RBAC.
"""

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Details
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Role
    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False,
    )

    # Audit
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationship (ONLY Role for now)
    role = relationship(
        "Role",
        back_populates="users"
    )

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"username='{self.username}', "
            f"email='{self.email}')>"
        )
documents = relationship(
    "Document",
    back_populates="owner",
    cascade="all, delete-orphan",
)

chat_history = relationship(
    "ChatHistory",
    back_populates="user",
    cascade="all, delete-orphan",
)

uploads = relationship(
    "Upload",
    back_populates="user",
    cascade="all, delete-orphan",
)