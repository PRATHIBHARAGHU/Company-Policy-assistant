"""
File: backend/app/models/role.py

Purpose:
    Defines application roles used for Role-Based Access Control (RBAC).

Responsibilities:
    - Store available roles.
    - Maintain relationship with users.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Role(Base):
    """
    Role Model

    Stores the available user roles within the system.

    Examples:
        - Admin
        - HR
        - Manager
        - Employee
    """

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(50),
        unique=True,
        nullable=False
    )

    description = Column(
        String(255),
        nullable=True
    )

    # Relationship with User model
    users = relationship(
        "User",
        back_populates="role"
    )

    def __repr__(self):
        return f"<Role(name='{self.name}')>"