"""
Document Service
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentService:

    @staticmethod
    def get_all_documents(
        db: Session,
    ):

        return db.query(Document).all()

    @staticmethod
    def get_document(
        document_id: int,
        db: Session,
    ):

        document = db.query(Document).filter(
            Document.id == document_id
        ).first()

        if document is None:

            raise HTTPException(
                status_code=404,
                detail="Document not found."
            )

        return document

    @staticmethod
    def delete_document(
        document_id: int,
        db: Session,
    ):

        document = DocumentService.get_document(
            document_id,
            db,
        )

        db.delete(document)

        db.commit()

        return {
            "message": "Document deleted successfully."
        }