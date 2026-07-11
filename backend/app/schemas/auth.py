"""
Authentication Schemas

Purpose:
    Request and Response schemas for authentication APIs.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    """
    User Registration Request
    """

    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    """
    User Login Request
    """

    email: EmailStr
    password: str


class Token(BaseModel):
    """
    JWT Response
    """

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    JWT Payload
    """

    user_id: int | None = None


class MessageResponse(BaseModel):
    """
    Generic Success Message
    """

    message: str


class LoginResponse(BaseModel):
    """
    Login API Response
    """

    access_token: str
    token_type: str = "bearer"
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)