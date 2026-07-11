"""
Authentication Service

Purpose:
    Handles registration, login, and current user retrieval.

Business logic belongs here, not in the router.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.models.role import Role

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    LoginResponse,
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        user_data: UserRegister,
    ):
        """
        Register a new user.
        """

        # Check email
        existing_email = (
            db.query(User)
            .filter(User.email == user_data.email)
            .first()
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists."
            )

        # Check username
        existing_username = (
            db.query(User)
            .filter(User.username == user_data.username)
            .first()
        )

        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists."
            )

        # Default role
        employee_role = (
            db.query(Role)
            .filter(Role.name == "employee")
            .first()
        )

        if employee_role is None:

            employee_role = Role(
                name="employee",
                description="Default Employee Role"
            )

            db.add(employee_role)
            db.commit()
            db.refresh(employee_role)

        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
            role_id=employee_role.id,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "message": "User registered successfully."
        }

    @staticmethod
    def login(
        db: Session,
        credentials: UserLogin,
    ) -> LoginResponse:
        """
        Authenticate user.
        """

        user = (
            db.query(User)
            .filter(User.email == credentials.email)
            .first()
        )

        if user is None:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        if not verify_password(
            credentials.password,
            user.hashed_password,
        ):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        token = create_access_token(
            {
                "user_id": user.id,
                "role": user.role.name,
            }
        )

        return LoginResponse(
            access_token=token,
            token_type="bearer",
            username=user.username,
            role=user.role.name,
        )

    @staticmethod
    def get_current_user(user: User):
        """
        Return current logged-in user.
        """

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role.name,
            "is_active": user.is_active,
            "is_verified": user.is_verified,
            "created_at": user.created_at,
        }