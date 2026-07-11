"""
Role Schemas

Purpose:
    Pydantic schemas for Role CRUD operations.
"""

from pydantic import BaseModel, ConfigDict, Field


class RoleBase(BaseModel):
    """
    Base Role Schema
    """

    name: str = Field(..., min_length=2, max_length=50)
    description: str | None = Field(default=None, max_length=255)


class RoleCreate(RoleBase):
    """
    Create Role Schema
    """

    pass


class RoleUpdate(BaseModel):
    """
    Update Role Schema
    """

    name: str | None = Field(default=None, min_length=2, max_length=50)
    description: str | None = Field(default=None, max_length=255)


class RoleResponse(RoleBase):
    """
    Role Response Schema
    """

    id: int

    model_config = ConfigDict(from_attributes=True)