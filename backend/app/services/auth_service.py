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
    def register(db: Session, user_data: UserRegister):

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

        employee_role = (
            db.query(Role)
            .filter(Role.name == "employee")
            .first()
        )

        if employee_role is None:

            employee_role = Role(
            name="employee",
            clearance_level=0
        )

            db.add(employee_role)
            db.commit()
            db.refresh(employee_role)

        user = User(
            full_name=user_data.full_name,
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
    def login(db: Session, credentials: UserLogin):

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
            full_name=user.full_name,
            role=user.role.name,
        )

    @staticmethod
    def get_current_user(user: User):

        return {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role.name,
            "is_active": user.is_active,
            "created_at": user.created_at,
        }