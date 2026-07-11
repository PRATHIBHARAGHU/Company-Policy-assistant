"""
User Schemas

Purpose:
    Request and Response schemas for user operations.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """
    Common User Fields
    """

    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create User
    """

    password: str


class UserUpdate(BaseModel):
    """
    Update User Profile
    """

    username: str | None = None
    email: EmailStr | None = None


class UserResponse(UserBase):
    """
    User Response Schema
    """

    id: int

    role: str

    is_active: bool

    is_verified: bool

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserProfile(UserResponse):
    """
    Current User Profile
    """

    pass