from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.core.database import Base

import enum


class UserRole(str, enum.Enum):
    employee = "employee"
    hr = "hr"
    manager = "manager"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=UserRole.employee.value, nullable=False)

    documents = relationship("Document", back_populates="owner")

    # Purpose: Represent the application user entity.
    # Inputs: Registration details.
    # Outputs: ORM model for persistence and authorization.
    # Flow: Store identity and role for RBAC.
