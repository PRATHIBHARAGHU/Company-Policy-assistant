"""
Common dependencies used across routers.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import verify_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


def get_db():
    """
    Database Dependency.
    """

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    user = db.query(User).filter(
        User.id == payload.get("user_id")
    ).first()

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


def require_role(*roles):
    """
    RBAC Dependency.
    """

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role.name not in roles:

            raise HTTPException(
                status_code=403,
                detail="Permission Denied"
            )

        return current_user

    return role_checker