"""
Authentication Router

Routes:
    POST   /register
    POST   /login
    GET    /me
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user,
)

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    LoginResponse,
    MessageResponse,
)

from app.schemas.user import UserResponse

from app.services.auth_service import AuthService

router = APIRouter()


@router.post(
    "/register",
    response_model=MessageResponse,
    status_code=201,
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """

    return AuthService.register(db, user)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    """
    Login user.
    """

    return AuthService.login(
        db,
        credentials,
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
def current_user(
    user=Depends(get_current_user),
):
    """
    Get current logged-in user.
    """

    return AuthService.get_current_user(user)