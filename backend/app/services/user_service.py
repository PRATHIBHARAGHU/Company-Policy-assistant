"""
User Service

Business logic related to users.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.role import Role


class UserService:

    @staticmethod
    def get_all_users(db: Session):

        return db.query(User).all()

    @staticmethod
    def get_user_by_id(user_id: int, db: Session):

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return user

    @staticmethod
    def assign_role(
        user_id: int,
        role_name: str,
        db: Session,
    ):

        user = UserService.get_user_by_id(
            user_id,
            db,
        )

        role = db.query(Role).filter(
            Role.name == role_name
        ).first()

        if role is None:

            raise HTTPException(
                status_code=404,
                detail="Role not found."
            )

        user.role_id = role.id

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def delete_user(
        user_id: int,
        db: Session,
    ):

        user = UserService.get_user_by_id(
            user_id,
            db,
        )

        db.delete(user)

        db.commit()

        return {
            "message": "User deleted successfully."
        }